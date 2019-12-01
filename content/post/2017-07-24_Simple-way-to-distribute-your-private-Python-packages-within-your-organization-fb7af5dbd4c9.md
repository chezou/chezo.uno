---
title: Simple way to distribute your private Python packages within your organization
description: >-
  This article is a translation of this article, originally written by aodag in
  Japanese. I translated it with his permission. This article…
date: '2017-07-24T01:21:40.424Z'
categories: [python]
keywords: []
authors: [aki]
---

![[http://www.irasutoya.com/2017/05/blog-post\_22.html](http://www.irasutoya.com/2017/05/blog-post_22.html)](/img/0__YSlLMz01REAp__q__y.png)
[http://www.irasutoya.com/2017/05/blog-post\_22.html](http://www.irasutoya.com/2017/05/blog-post_22.html)

_This article is a translation of_ [_this article_](https://gist.github.com/aodag/9a8118d06998b674e2d9597c6d02a6db)_, originally written by_ [_aodag_](https://github.com/aodag) _in Japanese. I translated it with his permission. This article is aimed to know simple ways to prepare internal Python package host like a_ [_local gem server on Ruby_](http://guides.rubygems.org/run-your-own-gem-server/)_._

### Methods

*   Include your packages in your git repository
*   Publish a directory including your packages via HTTP server
*   Build a local PyPI-equivalent server

It is a high-cost way to create a local PyPI-equivalent server _(translator note: like_ [_devpi_](http://doc.devpi.net/latest/)_)_, and I don’t think there is no need to do so, I will describe first two options.

#### Include your packages in your Git repository

If your packages are required for a particular project, it is straightforward to contain them in the Git repository. You can put them in the directory named `wheelhouse`, which comes from the name of the previous default directory created by `pip wheel`. (_translator note: this method is assumed you to know wheel. If not,_ [_this story_](http://wheel.readthedocs.io/en/latest/story.html) _and_ [_this JIRA_](https://issues.apache.org/jira/browse/SPARK-16367) _would be helpful._)If you put the private package `foo` in the `wheelhouse`, you can install as follows:

$ pip install foo -f wheelhouse

Note that `-f` is the short option for `--find-links`, with that option, pip will search packages in the directory first, then fall back to `pypi`.

#### Publish a directory including your packages via HTTP server

We can use`--find-link` option to search not only local directory but also a remote server via `http`. If you have a package used by multiple projects, this method will help you.

The easiest way to distribute your packages with this method is executing `python -m http.server` with Python 3.x (or `python -m SimpleHTTPServer` with Python 2.7) on the `wheelhouse` directory. This simple server provides directory listings so that we can just use`--find-links` to use the directory. Make sure to open `http://localhost:8000` that you can see the list of files under the `wheelhouse` directory via a web browser.

To install `foo` package via HTTP server you launched, you can execute as follows:

$ pip install foo -f http://localhost:8000

Since this is a simple server, for production, it is good to put them in cloud storage such as AWS S3, you should check the way for directory listings, or you can use Apache with `DirectoryIndex` enabled.

### Conclusion

I recommend these methods because they are simple and no need to prepare the dedicated application server.