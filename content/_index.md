---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography
    id: about
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: aki
      text: "AI Product Engineer"
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: aki_ariga_cv.pdf
    # design:
    #   css_class: dark
    #   background:
    #     color: black
    #     image:
    #       # Add your image background to `assets/media/`.
    #       filename: top_cover.webp
    #       filters:
    #         brightness: 0.3
    #       size: cover
    #       position: center
    #       parallax: false
  - block: markdown
    content:
      title: "Hello, I'm Aki👋"
      text: |-
        As a Vancouver-based Staff Software Engineer at LayerX, I specialize in Human-in-the-loop systems, ML product development, and MLOps. I am driven by the mission to use machine learning and AI to make a meaningful difference for both businesses and society.
  - block: collection
    id: blogs
    content:
      title: Recent Posts
      filters:
        folders:
          - blog
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: posts
    content:
      title: Recent Posts (Japanese)
      filters:
        folders:
          - post
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: publications
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2

---
