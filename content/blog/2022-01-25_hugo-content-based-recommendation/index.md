---
title: 3 configs add recommend articles into your Hugo blog by GitHub Actions
subtitle: Leverage prelims to do content-based recommendations
summary: ''
authors: [aki]
tags: [recommendation, hugo, github actions]
categories: [tech, ML]
date: 2022-01-25 19:37:52-08:00
lastmod: 2022-01-25 19:37:52-08:00
featured: false
draft: false
image: {caption: 'Recommendation example of https://chezo.uno/blog/2017-07-24_simple-way-to-distribute-your-private-python-packages-within-your-organization-fb7af5dbd4c9/',
  focal_point: Smart, preview_only: false}
projects: []
keywords: [articles, blog, recommendation, hugo, cli, yaml, content, based, post,
  write]
recommendations: [/blog/2025-08-24-configured-pages-cms/, /blog/2024-02-02-migrated-from-netlify-to-cloudflare-pages/,
  /blog/2017-05-02_an-easy-way-to-get-url-list-of-your-medium-publication-c60c61244101/]
---

Hugo has a feature to show keyword based related articles.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://gohugo.io/content-management/related/" data-iframely-url="//iframely.net/q1grvUY?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

Yeah, keyword based articles might be useful, for people who can manage keyword, category, etc, constantly.
I'd love to add content based recommendation that doesn't require to write explicit keywords by myself. Then, I found an open source named "Prelims" which is developed by [takuti](https://twitter.com/takuti).

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/takuti/prelims" data-iframely-url="//iframely.net/omDBVa8?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

Prelims is a post-processing tool for Front matter of Hugo/Jekyll, that is a metadata of an article.
The recommendation method which is implemented for now is classical, create a TF-IDF based word vector and find similar articles by consign similarity.

The reason why I love Prelims is it's simple and flexible. Post-processing of front matter doesn't break your articles nor blog system at all. You can remove extra meta data Prelims generated whenever you want.

Isn't it practical, right?

One downside of Prelims is it requires to implement Python code for tokenizing or vectorizing TF-IDF. I don't want to bring my laptop for blog writing and wanna use Netlify CMS and iPad without having Python environment.

So, I built a CLI tool for Prelims, named [prelims-cli](https://github.com/chezou/prelims-cli), which enables to add recommended articles just writing 1 configuration YAML file. It also runs with GitHub Actions.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/prelims-cli" data-iframely-url="//iframely.net/m9C9uKt?card=small"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

The three things you need to prepare are:

1. Configuration YAML file for prelims-cli. e.g., `scripts/config/myconfig.yaml`
2. Hugo HTML partial layout, e.g., `layouts/partials/page_related.html`
3. GitHub Actions workflow for prelims-cli

Here is the example gist what you need to write.

{{< gist chezou a9cb0ab2a086b3ce9ce9bf1abbc5b347 >}}

where `content/blog` is the directory for English articles and `content/post` is the directory for Japanese articles.

Putting three files enables you to show recommended articles into your Hugo blog, like the screenshot in the top of this article.

Internally, for Japanese tokenization, it uses SudachiPy. Since `keywords` prelims generates are a-bit noisy and didn't wanted to cleanup, so I stopped using it.

The good things I feel are, I can use my blog articles for my hobby recommendation project, and I don't need to manage tags and categories seriously.

You can enjoy your recommendation without having Python environment, so you can write your articles on iPad with Netlify CMS!
