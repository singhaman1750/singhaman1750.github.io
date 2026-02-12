# Personal Academic Website

This repository contains the source code for my personal academic website, built with Jekyll and customized from the al-folio theme. It hosts my bio, research interests, publications, projects, news, and blog posts.

## Site Structure (high level)

- Content: `_pages/`, `_posts/`, `_projects/`, `_news/`, `_books/`
- Data: `_data/` (CV, social links, venues, citations, coauthors)
- Publications: `_bibliography/`
- Layouts & components: `_layouts/`, `_includes/`
- Styling & assets: `_sass/`, `assets/`

## Customize Content

- Update site metadata and settings in `_config.yml`.
- Edit pages in `_pages/` and posts in `_posts/`.
- Add or update publications in `_bibliography/papers.bib`.
- Maintain structured data in `_data/` (CV, socials, repositories, venues).

## Build & Preview

See [INSTALL.md](INSTALL.md) for local setup and build instructions.

## License & Credits

The site is based on the al-folio theme with local modifications. Please check [LICENSE](LICENSE) for licensing details.
  {% for repo in site.data.repositories.github_repos %} {% include repository/repo.liquid repository=repo %} {% endfor %}
</div>
{% endif %}
```

---

#### Theming

A variety of beautiful theme colors have been selected for you to choose from. The default is purple, but you can quickly change it by editing the `--global-theme-color` variable in the `_sass/_themes.scss` file. Other color variables are listed there as well. The stock theme color options available can be found at [\_sass/\_variables.scss](_sass/_variables.scss). You can also add your own colors to this file assigning each a name for ease of use across the template.

---

#### Social media previews

**al-folio** supports preview images on social media. To enable this functionality you will need to set `serve_og_meta` to `true` in your [\_config.yml](_config.yml). Once you have done so, all your site's pages will include Open Graph data in the HTML head element.

You will then need to configure what image to display in your site's social media previews. This can be configured on a per-page basis, by setting the `og_image` page variable. If for an individual page this variable is not set, then the theme will fall back to a site-wide `og_image` variable, configurable in your [\_config.yml](_config.yml). In both the page-specific and site-wide cases, the `og_image` variable needs to hold the URL for the image you wish to display in social media previews.

---

#### Atom (RSS-like) Feed

It generates an Atom (RSS-like) feed of your posts, useful for Atom and RSS readers. The feed is reachable simply by typing after your homepage `/feed.xml`. E.g. assuming your website mountpoint is the main folder, you can type `yourusername.github.io/feed.xml`

---

# Aman Singh — Personal Academic Website

I am a PhD researcher in Robotics at the [IISc, Bengaluru](https://iisc.ac.in/), working with the [Stochastic Robotics Lab](https://www.stochlab.com/) in the Centre for Cyber-Physical Systems. My research focuses on robotic actuator design, planetary gearbox optimization, and hardware-centric co-design for legged robots.

Highlights
- Research interests: robotic actuators, planetary gearboxes, legged-robot hardware design
- Approach: computational optimization, automated CAD, and experimental validation

Quick links
- CV: /assets/pdf/Aman_s_Resume.pdf
- Google Scholar: https://scholar.google.com/citations?user=7PzY75AAAAAJ&hl=en
- GitHub: https://github.com/singhaman1750
- LinkedIn: https://www.linkedin.com/in/aman-singh-21782212b/
- ResearchGate: https://www.researchgate.net/profile/Aman-Singh-201
- X (Twitter): https://x.com/singhaman1750

Development
- This site is built with Jekyll using a customized al-folio theme. See `INSTALL.md` for local build and preview instructions.

License & credits
- The site is based on the al-folio theme; please see `LICENSE` for licensing details.

If you'd like a different README format (more project-oriented, shorter bio, or include badges), tell me which style you prefer and I will update it.

