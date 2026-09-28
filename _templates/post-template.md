---
# HOW TO USE: copy this file to _posts/YYYY-MM-DD-short-title.md (e.g. _posts/2026-09-28-my-new-post.md),
# then edit the fields below and replace the body. This file itself is never published.
layout: post # keep as is
title: Your Post Title # shown as the heading and in the blog list
date: 2026-09-28 10:00:00 +0530 # posts dated in the future are hidden unless you serve with --future
description: One-line summary shown under the title in the blog list
thumbnail: assets/img/1.jpg # optional: preview image in the blog list; delete the line if not needed
tags: [research, phd life] # existing tags: research, phd life, writing, robotics, actuators, conferences, life outside the lab
---

Opening paragraph. Say what the post is about and why it matters. You can use **bold**, _italics_, and [links](https://example.com).

## A Section Heading

Regular paragraph text. Use `##` for sections and `###` for subsections.

- A bullet point
- Another bullet point

1. A numbered step
2. Another numbered step

> A quote or an important takeaway.

## Images

Put images in `assets/img/` (tip: a subfolder per post, e.g. `assets/img/my-new-post/`), then reference them by path. The images below use theme sample files as placeholders; replace the paths with your own.

### Single image

{% include figure.liquid loading="eager" path="assets/img/1.jpg" class="img-fluid rounded z-depth-1" %}

### Image with a caption

{% include figure.liquid loading="eager" path="assets/img/2.jpg" class="img-fluid rounded z-depth-1" caption="A short caption describing the image." %}

### Image that enlarges when clicked

{% include figure.liquid loading="eager" path="assets/img/3.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}

### Two images side by side

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    One caption for both images.
</div>

### Three images side by side

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/6.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/7.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/8.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    One caption for all three images.
</div>

### Image that links somewhere

{% include figure.liquid loading="eager" path="assets/img/9.jpg" class="img-fluid rounded z-depth-1" url="https://example.com" %}

## Code

```python
print("Hello, world")
```

## Closing

Wrap up with the main takeaway.
