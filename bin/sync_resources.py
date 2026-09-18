#!/usr/bin/env python3
"""Mirror the Legged-Robots content repo into this site.

Reads a checkout of https://github.com/singhaman1750/Legged-Robots and writes:

  _data/resources.yml   the index, parsed from that repo's README
  _resources/**.md      one Jekyll page per topics/**.md file

Both outputs are generated, gitignored, and rebuilt from scratch on every run:
in CI by the "Sync resources" step of deploy.yml, and locally with

    python bin/sync_resources.py

before `jekyll serve`. Never edit them by hand -- edit the Legged-Robots repo.

Deliberately dependency-free (stdlib only) so it runs in the deploy workflow
without installing anything.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

REPO_URL = "https://github.com/singhaman1750/Legged-Robots"
REPO_CLONE = REPO_URL + ".git"
REPO_BLOB = REPO_URL + "/blob/main"

SITE = Path(__file__).resolve().parent.parent
OUT_PAGES = SITE / "_resources"
OUT_INDEX = SITE / "_data" / "resources.yml"

# Markdown link: [label](target)
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
# A line that is nothing but "back to ..." links, optionally joined by a
# separator. The site has its own navigation, so these are dropped.
BACK_NAV = re.compile(
    r"^\s*\[\s*(?:←|<-)[^\]]*\]\([^)]*\)"
    r"(?:\s*[·|,]\s*\[[^\]]*\]\([^)]*\))*\s*$"
)
# A line that is nothing but shields.io-style badges.
BADGE = re.compile(r"^\s*(?:\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)\s*)+$")
# Stray <content> / </content> tags left in a few files in the source repo.
STRAY_TAG = re.compile(r"^\s*</?content>\s*$", re.IGNORECASE)

HEADING = re.compile(r"^(#{2,6})\s+(.*?)\s*#*\s*$")
BULLET = re.compile(r"^\s*[-*]\s+\[([^\]]*)\]\(([^)]+)\)\s*(?::\s*)?(.*)$")


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #


def yq(value):
    """Quote a string as a YAML double-quoted scalar."""
    out = value.replace("\\", "\\\\").replace('"', '\\"')
    out = out.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    return '"' + out + '"'


def site_url(repo_path):
    """Map a repo-root-relative path to its URL on the site, or None."""
    path = PurePosixPath(repo_path)
    if path.as_posix() == "README.md":
        return "/resources/"
    parts = path.parts
    if len(parts) >= 2 and parts[0] == "topics" and path.suffix == ".md":
        return "/resources/" + "/".join(parts[1:-1] + (path.stem,)) + "/"
    return None


def rewrite_links(text, src_dir):
    """Point repo-relative links at the site, or at GitHub if unmirrored.

    src_dir is the source file's directory relative to the repo root.
    """

    def replace(match):
        label, target = match.group(1), match.group(2)
        url, sep, frag = target.partition("#")
        if not url or "://" in url or url.startswith(("/", "#", "mailto:")):
            return match.group(0)
        resolved = os.path.normpath(os.path.join(src_dir, url)).replace(os.sep, "/")
        mapped = site_url(resolved)
        if mapped is None:
            # Not mirrored onto the site (an image, a file outside topics/, a
            # link to the repo itself): send the reader to GitHub rather than
            # leave a relative link that would 404 here.
            mapped = REPO_BLOB + "/" + resolved
        return "[" + label + "](" + mapped + sep + frag + ")"

    return LINK.sub(replace, text)


def clean_lines(text):
    return [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]


# --------------------------------------------------------------------------- #
# topic pages
# --------------------------------------------------------------------------- #


def build_page(src_rel, text):
    """Return (title, body) for one topics/**.md file."""
    title = None
    kept = []
    for line in clean_lines(text):
        if STRAY_TAG.match(line) or BADGE.match(line) or BACK_NAV.match(line):
            continue
        if title is None and line.startswith("# "):
            title = line[2:].strip()  # rendered by the layout, not the body
            continue
        kept.append(line)

    body = rewrite_links("\n".join(kept).strip("\n"), str(PurePosixPath(src_rel).parent))
    fallback = PurePosixPath(src_rel).stem.replace("-", " ").title()
    return title or fallback, body


def write_pages(repo):
    topics = repo / "topics"
    if not topics.is_dir():
        sys.exit("error: no topics/ directory in " + str(repo))

    if OUT_PAGES.exists():
        shutil.rmtree(OUT_PAGES)

    written = []
    for src in sorted(topics.rglob("*.md")):
        src_rel = src.relative_to(repo).as_posix()
        url = site_url(src_rel)
        if url is None:
            continue
        title, body = build_page(src_rel, src.read_text(encoding="utf-8"))

        dest = OUT_PAGES / src.relative_to(topics)
        dest.parent.mkdir(parents=True, exist_ok=True)
        # {% raw %} keeps any {{ }} or {% %} in the source content from being
        # evaluated -- and from breaking the build -- when Jekyll renders it.
        dest.write_text(
            "---\n"
            "layout: resource\n"
            "title: " + yq(title) + "\n"
            "permalink: " + url + "\n"
            "source_path: " + yq(src_rel) + "\n"
            "source_url: " + yq(REPO_BLOB + "/" + src_rel) + "\n"
            # Excerpts are unused here, and auto-generating one cuts through the
            # {% raw %} block below and warns on every build.
            'excerpt_separator: ""\n'
            "---\n\n"
            "{% raw %}\n" + body + "\n{% endraw %}\n",
            encoding="utf-8",
        )
        written.append(url)

    return written


# --------------------------------------------------------------------------- #
# index
# --------------------------------------------------------------------------- #


def write_index(repo, known_urls):
    readme = repo / "README.md"
    if not readme.is_file():
        sys.exit("error: no README.md in " + str(repo))

    intro = []
    entries = []
    pending = []
    missing = 0
    seen_heading = False

    def flush():
        if pending:
            entries.append({"kind": "items", "items": list(pending)})
            del pending[:]

    for line in clean_lines(readme.read_text(encoding="utf-8")):
        if STRAY_TAG.match(line) or BADGE.match(line) or line.startswith("# "):
            continue

        heading = HEADING.match(line)
        if heading:
            flush()
            entries.append(
                {
                    "kind": "heading",
                    "level": len(heading.group(1)),
                    "title": heading.group(2),
                }
            )
            seen_heading = True
            continue

        bullet = BULLET.match(line)
        if bullet:
            label, target, description = bullet.groups()
            url = site_url(os.path.normpath(target).replace(os.sep, "/"))
            if url is None:
                url = target if "://" in target else REPO_BLOB + "/" + target
            elif url not in known_urls and url != "/resources/":
                print("  warning: README links to a missing topic: " + target)
                missing += 1
            pending.append(
                {"title": label, "url": url, "description": description.strip()}
            )
            continue

        if not seen_heading and line.strip() and line.strip() != "---":
            intro.append(line.strip())

    flush()

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out = [
        "# Generated by bin/sync_resources.py from the Legged-Robots repo.",
        "# Do not edit and do not commit -- your changes will be overwritten.",
        "repo_url: " + yq(REPO_URL),
        "generated: " + yq(generated),
        "intro: " + yq(" ".join(intro)),
        "entries:",
    ]
    for entry in entries:
        if entry["kind"] == "heading":
            out += [
                "  - kind: heading",
                "    level: " + str(entry["level"]),
                "    title: " + yq(entry["title"]),
            ]
        else:
            out += ["  - kind: items", "    items:"]
            for item in entry["items"]:
                out += [
                    "      - title: " + yq(item["title"]),
                    "        url: " + yq(item["url"]),
                    "        description: " + yq(item["description"]),
                ]

    OUT_INDEX.parent.mkdir(parents=True, exist_ok=True)
    OUT_INDEX.write_text("\n".join(out) + "\n", encoding="utf-8")
    return missing


# --------------------------------------------------------------------------- #


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        nargs="?",
        help="path to a Legged-Robots checkout (default: shallow-clone it)",
    )
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        if args.source:
            repo = Path(args.source).resolve()
            if not repo.is_dir():
                sys.exit("error: " + str(repo) + " is not a directory")
        else:
            repo = Path(tmp) / "Legged-Robots"
            print("Cloning " + REPO_CLONE + " ...")
            subprocess.run(
                ["git", "clone", "--depth", "1", REPO_CLONE, str(repo)],
                check=True,
                stdout=subprocess.DEVNULL,
            )

        print("Syncing resources from " + str(repo))
        urls = write_pages(repo)
        missing = write_index(repo, set(urls))

    print("  " + str(len(urls)) + " topic pages -> " + str(OUT_PAGES.relative_to(SITE)))
    print("  index -> " + str(OUT_INDEX.relative_to(SITE)))
    if missing:
        sys.exit(
            "error: " + str(missing) + " README link(s) point at missing topic files"
        )


if __name__ == "__main__":
    main()
