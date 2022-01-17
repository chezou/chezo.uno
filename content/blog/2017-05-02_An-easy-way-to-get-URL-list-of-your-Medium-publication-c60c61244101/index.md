---
title: An easy way to get URL list of your Medium publication
description: I imported blog posts from own Wordpress but I have to redirect old articles
  to Medium manually. There is Wordpress plugin which enables…
date: '2017-05-02T11:01:01+09:00'
categories: []
keywords: [publication, articles, list, url, medium, wordpress, redirect, posts, showing,
  scrolling]
authors: [aki]
recommendations: [/blog/2017-05-28_tabula-py-now-able-to-extract-remote-PDF-and-multiple-tables-at-once-6108e24ac07c/,
  /blog/2016-12-01_Text-to-speech-based-on-deep-learning-for-Web-site-using-Amazon-Polly-and-Ruby-adc1923212cb/,
  /blog/py-operator-development-guide-for-python-users/]
---

I imported blog posts from own Wordpress but I have to redirect old articles to Medium manually. There is Wordpress plugin which enables you to redirect articles, but it requires URL mapping in CSV format. When you want to get Medium publication’s URL list, you may use [official APIs](https://github.com/Medium/medium-api-docs), but officially, it [lacks the function to get list of posts](https://github.com/Medium/medium-api-docs/issues/30). We need [some other choices](https://github.com/enginebai/PyMedium), but I couldn’t get the post list. In this article, I will show you how to get URL list of your Medium publication easily.

**Note: I tried this method with under 150 articles publication. It might not work with huge number of articles.**

#### How-to

You can use following Python script, after showing whole articles with accesing `/latest` of a publication. For example, after opening [https://blog.chezo.uno/latest](https://blog.chezo.uno/latest), you can get whole contents with scrolling down and down and down…