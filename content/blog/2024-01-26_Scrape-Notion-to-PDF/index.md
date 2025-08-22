---
authors: []
categories:
- python
date: '2024-01-26 17:40:00-08:00'
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
keywords:
- provide
- pages
- pdfs
- originally
- actions
- japanese
- github
- script
- repository
- image
lastmod: '2024-01-26 17:40:00-08:00'
projects: []
recommendations:
- /blog/2019-10-06_how-to-test-a-new-docker-image-for-digdag-workflow-on-circleci--c8bb92987877/
- /blog/2019-11-26_how-to-release-python-package-from-github-actions-d5a1d8edba6e/
- /blog/2024-02-02-migrated-from-netlify-to-cloudflare-pages/
subtitle: ''
summary: ''
tags: []
title: Scrape Notion and convert into PDF
---

I love [VanGohan](https://www.vangohan.com/), who is a Japanese meal kits provider in Vancouver. Their meal kits are really tasty and authentic Japanese foods. I can't live without them. When I visited Japan last year, I wasn't too eager to find nice Japanese restaurants because of them.

## Recipe on Notion is good, if it's printable

They provide a recipe on Notion. Seeing the recipes on it is great since they can fix recipes quite quickly.

However, there's one caveat of Notion. They don't provide printable pages. It's super annoying to copy and past the recipes to the memo app, and print it out. I asked Notion's support team, but they answered it isn't a prioritized item implicitly.

Ok, it's automation time!

## Scrape Notion with Python

As my handy tool, I have been using Python for this kind of automation for years. Originally, I used beautifulsoup, which is great package for web scraping, but I gave it up to use it. Contents of Notion is rendered by JavaScript dynamically.

I chose [Selenium](https://selenium-python.readthedocs.io/) and it works like a charm.

Here is the GitHub repository:

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/vangohan-pdf" data-iframely-url="//iframely.net/cP0eFmn?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

They key takeaways are:

- `chromedriver-autoinstaller` package is useful to avoid extra efforts of Chrome driver installation.
- Selenium is easy enough to export PDF [code](https://github.com/chezou/vangohan-pdf/blob/004eaa83a45f2a238b5065a0474903a60838a94d/fetch_vangohan.py#L200-L212).
- Running the script on GitHub Actions is easy. Don't forget to install fonts if it's not English page.

Originally, I thought I had to prepare a Docker image, but I was aware it was not mandatory. Managing a Docker image for this kind of hobby script would be costly. So, I'm going to keep this approach and will look back if it is the right way.

Currently, I scheduled the [GitHub Actions workflow](https://github.com/chezou/vangohan-pdf/blob/main/.github/workflows/selenium_action.yaml). It will update the PDFs on the repository automatically.

https://github.com/chezou/vangohan-pdf/tree/main/docs

Edit: Now I use Cloudflare Pages to host the PDFs. You can check at https://vangohan.chezo.uno/.

No Python environment on a local machine is needed anymore.

Yay, automation is completed! 😁