---
title: Migrated from Pages CMS to Sveltia CMS
subtitle: ''
summary: ''
date: 2026-03-19 16:41:00-07:00
lastmod: ''
categories: [blog]
tags: [CMS, blog]
draft: false
featured: true
image:
  filename: pasted-image-1773964049625.png
  focal_point: Smart
  preview_only: false
  alt_text: Warning notification of GitHub issue on Sveltia CMS
recommendations: [/blog/2024-02-02-migrated-from-netlify-to-cloudflare-pages/, /blog/2025-08-24-configured-pages-cms/,
  /blog/2017-07-24_simple-way-to-distribute-your-private-python-packages-within-your-organization-fb7af5dbd4c9/]
---

I [introduced Pages CMS last summer](https://chezo.uno/blog/2025-08-24-configured-pages-cms/), but after encountering several concerns, I migrated to Sveltia CMS.

## Motivation

As I wrote in [this comment on GitHub](https://github.com/chezou/chezo.uno/pull/96#issuecomment-4078902665), the move was triggered by the following issues with Pages CMS:

- It handled time zones poorly (essentially forcing everything to +00:00), and even after [I carefully provided use cases](https://github.com/pages-cms/pages-cms/issues/247#issuecomment-4071771738), there didn't seem to be much interest in fixing it.

- It was quite troublesome to achieve the directory structure recommended by Hugoblox, where content (index.md) and images are placed in the same folder. I ended up having to upload images manually.

## What I did

- Deployed Sveltia CMS Auth to Cloudflare Workers for authentication.

- Had Claude migrate the .pages.yml from Pages CMS to static/admin/config.yml.

- Copy-pasted static/admin/index.html from the documentation.

- Used Claude to restore the time zone data that Pages CMS had dropped.

The biggest hassle was deploying Sveltia CMS Auth, but since I was already using Cloudflare Pages, all I had to do was click the deploy button in the README at https://github.com/sveltia/sveltia-cms-auth and follow the instructions. It was simple. It reminded me of Heroku.

For details, please refer to the following PRs:

- https://github.com/chezou/chezo.uno/pull/96

- https://github.com/chezou/chezo.uno/pull/99

## Impressions

Pages CMS had been bothering me with a few minor annoyances, and it was great to see them resolved here. For instance, loading 400+ posts takes over 10 seconds in Pages CMS, but Sveltia CMS handles it in about 2. It's fast enough, isn't it?

The `M↓` button is a lifesaver too. Being able to drop into raw Markdown when the editor misbehaves means I no longer have to open GitHub and edit files directly, which was a nightmare, especially on mobile.

The attention to detail really shows. While writing this post, a minor GitHub outage hit, and I actually got a warning about it. Impressive for something that runs entirely client-side.

![Warning notification of GitHub issue on Sveltia CMS](pasted-image-1773964049625.png)

Uploading this screenshot straight from the clipboard was seamless as well. In Pages CMS, getting a screenshot into the right folder alongside the content was a real pain, so this one stood out. (This feature [was just released yesterday](https://bsky.app/profile/britegrid.io/post/3mhh36afjcp2i). What a sense of speed!)

The author, kyoshino, is a Japanese speaker, it is clear that they are mindful of the IME input issues that we CJK (Chinese, Japanese, Korean) users often encounter. Being able to type without stress is truly important.

I plan to enjoy trying it out for a while, and unless any major issues arise, I think I will stick with it for the foreseeable future.
