---
title: How to release Python package from GitHub Actions
description: Recently, I changed my CI from Travis to GitHub Actions. GitHub Actions
  is handy and useful for testing, publishing Python packages.
date: '2019-11-26T01:42:11+09:00'
categories: [Python]
authors: [aki]
aliases: [/blog/how-to-release-python-package-from-github-actions-d5a1d8edba6e/, /blog/d5a1d8edba6e/]
keywords: [pypi, github, actions, api, workflow, python, package, testing, syntax,
  recently]
recommendations: [/blog/2018-04-17_use-markdown-document-on-brand-new-pypi-9723024f09c2/,
  /blog/2017-08-30_python-basics--package-management-462918458f96/, /blog/2022-01-25_hugo-content-based-recommendation/]
---

![](./0__hOksODxf9TX1BkS0.jpg)
Photo by [Hitesh Choudhary](https://unsplash.com/@hiteshchoudhary?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Recently, I changed my CI from Travis to GitHub Actions. GitHub Actions is handy and useful for testing, publishing Python packages.

### Testing Python code on GitHub Actions

Migration from Travis is super easy, just writing a simple workflow like:

[https://github.com/chezou/tabula-py/blob/master/.github/workflows/pythontest.yml](https://github.com/chezou/tabula-py/blob/master/.github/workflows/pythontest.yml)


The benefits of GitHub Actions for Python are:

*   We can use build matrix (e.g., OS and Python versions) like Travis
*   Launch time of GitHub is faster than Travis
*   Easy for additional dependency installation by using `uses` syntax, which uses another workflow

For example, installing JDK can be written as:

```
- uses: actions/setup-java@v1  
     with:  
      java-version: '12'  
      java-package: jdk  
      architecture: x64
```

The downside of GitHub Actions are:

*   Unable to [write Windows temp directory](https://github.community/t5/GitHub-Actions/TEMP-is-broken-on-Windows/m-p/30432)
*   Hard to find the resources for debugging on the internet and unable to ssh to the instance

### Releasing Python package from GitHub Actions to PyPI

I created the workflow like the following sequence:

1.  Push a tag from local, or create a tag on GitHub. Using [setuptools-scm](https://pypi.org/project/setuptools-scm/) enables you to make a new version from Git tag
2.  GitHub Actions creates GitHub release from the tag
3.  GitHub Actions publishes wheel to PyPI by using PyPI API Token

You can see the actual workflow on GitHub:

[https://github.com/chezou/tabula-py/blob/master/.github/workflows/pythonpublish.yml](https://github.com/chezou/tabula-py/blob/master/.github/workflows/pythonpublish.yml)

The key points are:

1.  Triggering the workflow from Git tag

```
on:  
   push:  
     tags:  
       - 'v\*'
```

2\. Adding dependency for deploy task

```
deploy:  
     needs: release
```

`needs` syntax supports to write dependency. In this case, I describe `release` job for creating GitHub release, and then `deploy` job publishes the package to PyPI.

3\. Preparation secrets for PyPI

Recently, PyPI provides API tokens for package publishments so that you can get an API token for the specific project. See details on the official document since it is under beta, and spec might change.

[https://pypi.org/help/#apitoken](https://pypi.org/help/#apitoken)

After getting API Token from PyPI, you can set secrets on GitHub by clicking “Settings” -> “Secrets” on the project page. Using my example workflow, you should set `__token__` for `PYPI_USERS` , and a token starting with `pypi-` got on PyPI configuration for `PYPI_PASSWORD` .

Now, you can publish Python package to PyPI by just tagging on GitHub.
