# Templates

Files in this folder are **not published**. Jekyll skips folders that start with `_` unless they are built-in (`_posts`, `_layouts`, ...) or listed under `collections:` in `_config.yml`.

## Adding a new blog post

1. Copy `post-template.md` to `_posts/YYYY-MM-DD-short-title.md` (the filename format is required).
2. Edit the front matter at the top (`title`, `date`, `description`, `thumbnail`, `tags`).
3. Put images in `assets/img/` (optionally a subfolder per post) and update the image paths.
4. Delete the example sections you don't need and write your post.
5. Preview locally: `bundle exec jekyll serve --livereload`, then open http://localhost:4000/blog/.
6. Commit and push to `main` to publish.
