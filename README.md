# 💻 My Academic Website

Welcome to my academic website, where I showcase my projects and research. This site is built using the Jekyll framework and utilizes the **Academic Pages** template, which can be found at [academicpages.github.io](https://academicpages.github.io).

## ✏️ Todo List
Here are some features I plan to add:
- [ ] **Project Portfolio**: A dedicated section to display my projects.
- [ ] **Sketches Tab**: A space for my sketches and artistic explorations.
- [ ] **GitHub Repositories**: A tab for selected GitHub repositories and resources I've collected over the years.
- [ ] **Course Syllabus**: Information about the **Unconstrained Optimization** course.
- [ ] **Patents Tab**: A section on the home page to highlight any patents.

## 🔨 Create Your Own Website
If you're interested in creating your own academic website, follow these steps:

### Instructions
1. **Register a GitHub Account**: If you don’t have one, sign up and confirm your email.
2. **Fork the Repository**: Click the "fork" button on the [Academic Pages repository](https://github.com/academicpages/academicpages.github.io).
3. **Rename Your Repository**: In the repository settings, rename it to `[your GitHub username].github.io`, which will be your website's URL.
4. **Configure Your Site**: Set site-wide configurations and create and edit content as needed. 
(see see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
5. **Upload Files**: Place any files (like PDFs) in the `files/` directory; they will be accessible at `https://[your GitHub username].github.io/files/example.pdf`.
6. **Check Status**: Go to the repository settings in the "GitHub Pages" section to verify everything is set up correctly.

### To Run Locally
To preview your site locally before pushing changes:
1. **Clone the Repository**: Make updates as detailed above.
2. **Install Dependencies**: Ensure you have `ruby-dev`, `bundler`, and `nodejs` installed:
   ```bash
   sudo apt install ruby-dev ruby-bundler nodejs
3. **Clean Up Directory**: Run `bundle clean`.
4. **Install Ruby Dependencies**: Execute `bundle install`.
5. **Serve Locally**: Use `bundle exec jekyll serve` to generate HTML and serve it from `localhost:4000`.

### Note: 
If you receive a notification about a security vulnerability while using this repository, delete the Gemfile.lock file. For more detailed information, refer to Academic Pages Documentation.

## 🙏 Credits
1. **GitHub Repository**: I forked from [Academic Pages](https://github.com/academicpages/academicpages.github.io).
2. **YouTube Tutorial**: I followed Boris Meinardus's video tutorial available [here](https://youtu.be/8lJhXJCUYCc?feature=shared).
