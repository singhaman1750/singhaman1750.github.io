# Plan

Working notes for planned changes to this site. Not published — `plan.md` is in
the `exclude:` list in `_config.yml`.

---

## Collaborators page

**Goal:** add a "Friends and Collaborators" page, modelled on
<https://joshrackers.owlstown.net/people>.

### What the reference page does

Josh Rackers' page is a flat directory of ~12 people, grouped by **research
area** rather than by institution or seniority. Three groups:

- Euclidean Neural Networks
- Next-Generation Force Fields
- Ion Channel Simulations

Each person is a compact card: profile photo, name (linked to their own site),
and one line of affiliation + role — e.g. "Tess Smidt — Professor, MIT".
Professors, postdocs, grad students, and national-lab staff are mixed together
within a group, not separated by rank. No prose bios.

### Why not al-folio's built-in `profiles` layout

The theme ships `_layouts/profiles.liquid` with `_pages/profiles.md`
(`permalink: /people/`, currently `nav: false`). It is the wrong shape for this:
it renders one profile per row as a large floated image plus a full markdown bio
from a separate file in `_pages/`. That suits a lab page with 3–4 people and
real bios; it becomes very long and repetitive at 12+ people with one line each.

### Recommended approach

Reuse the pattern already built for `/resources/`:

- `_data/collaborators.yml` — hand-maintained list, grouped into sections.
- `_pages/collaborators.md` — renders it as a responsive card grid, reusing the
  card CSS in `_pages/resources.md` (`.resource-index` styles — worth factoring
  the shared bits into `_sass/` if both pages use them).
- Photos in `assets/img/people/`, rendered through `figure.liquid` so the theme's
  responsive-image and WebP pipeline applies.

Rough data shape:

```yaml
- group: Legged Robot Design
  people:
    - name: Some Person
      role: PhD Student
      affiliation: IISc Bengaluru
      url: https://example.com
      image: people/some-person.jpg
```

This is ordinary hand-maintained site content — unlike `/resources/`, there is no
upstream repo to sync from, so no generation step and nothing to gitignore.

### Decisions to make first

1. **Who goes on it.** The actual list of people — this is the main blocker.
2. **How to group them.** Options: by research theme (as Rackers does — e.g.
   actuator design / legged locomotion / co-design optimization), by institution,
   or by relationship (advisor, lab mates, external collaborators). Theme-based
   grouping reads best and matches the reference.
3. **Photos or no photos.** Photos look better but mean sourcing and hosting an
   image for each person, and keeping them current. A name + affiliation grid
   with no images is a legitimate fallback and much lower maintenance.
4. **Page title and URL.** `/people/` is currently taken by the unused stock
   `profiles.md`. Either repurpose that permalink and delete the stock page, or
   use `/collaborators/`.
5. **Nav placement.** `nav_order` values in use: research 2, publications 3,
   blog 4, repositories 4, teaching 5, resources 6. Note blog and repositories
   both sit at 4 — worth fixing while in there.

### Implementation steps

1. Settle decisions 1–5 above.
2. Delete or repurpose `_pages/profiles.md` and `_pages/about_einstein.md`
   (both stock al-folio demo content).
3. Create `_data/collaborators.yml`.
4. Create `_pages/collaborators.md` with the card grid.
5. Add photos to `assets/img/people/` if going that route.
6. Check the page at phone width — the card grid needs to stack.

### Related cleanup spotted while planning

- `_data/coauthors.yml` is still stock al-folio demo data (Einstein's
  coauthors — Podolsky, Rosen, the Bachs). It is used by jekyll-scholar to turn
  coauthor names in the publication list into links. Populating it with real
  coauthors from `_bibliography/papers.bib` would improve the publications page,
  and overlaps with whoever ends up on the collaborators page.
