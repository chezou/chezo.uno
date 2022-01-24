---
title: Use Markdown document on brand new PyPI
description: Yesterday, PyPI was renewed to the next-generation site. It is modern
  and stylish one.
date: '2018-04-17T13:21:33+09:00'
categories: [python]
authors: [aki]
aliases: [/blog/use-markdown-document-on-brand-new-pypi-9723024f09c2, /blog/9723024f09c2]
keywords: [pip, pypi, packages, py, document, aodag, python, site, setup, description]
recommendations: [/blog/2017-08-30_Python-basics--package-management-462918458f96/,
  /blog/2019-11-26_How-to-release-Python-package-from-GitHub-Actions-d5a1d8edba6e/,
  /blog/2017-07-24_Simple-way-to-distribute-your-private-Python-packages-within-your-organization-fb7af5dbd4c9/]
---

Yesterday, PyPI was renewed to the next-generation site. It is modern and stylish one.

[@aodag](http://twitter.com/aodag "Twitter profile for @aodag") told me that [PEP 566](https://www.python.org/dev/peps/pep-0566/#description-content-type-optional), which was accepted Feb. 2018, allows us for a document on PyPI to use not only reStructuredText but also other formats such as Markdown.

So I enabled my Markdown document on brand-new PyPI.

### Upgrade Python packages (if necessary)

We can use Markdown with setuptools [as of v.38.6.0](http://setuptools.readthedocs.io/en/latest/history.html#v38-6-0). Let’s upgrade you python packages if needed. Without that, Markdown description will not be rendered appropriately.

$ python -m pip install --upgrade pip  
$ pip install --upgrade wheel  
$ pip --version  
pip 10.0.0 from c:\\users\\chezo\\documents\\source\\tabula-py\\venv\\lib\\site-packages\\pip (python 3.6)  
$ pip list  
Package           Version     Location  
\----------------- ----------- --------------------------------------  
(...snip...)  
setuptools        38.1.0  
(...snip...)  
wheel             0.31.0

### Modify setup.py

If you’ve already used README.md as a long description on PyPI, all you have to do is to add `long_description_content_type` to setup.py as follows:

```py
long_description=open('README.md').read(),
long_description_content_type="text/markdown",
```

You can see the full description of the PR :

[**Handle markdown long description for Pypi by chezou · Pull Request #85 · chezou/tabula-py**  
_Thanks for PEP 566, as of setuptools v38.6.0, PyPI can render long description written in markdown. This PR allows…_github.com](https://github.com/chezou/tabula-py/pull/85 "https://github.com/chezou/tabula-py/pull/85")[](https://github.com/chezou/tabula-py/pull/85)

### Build a wheel and upload with twine

Now, you can build a wheel and upload with twine.

```sh
$ python setup.py bdist_wheel  
$ twine upload dist/*
```

{{< figure src="1__TsTQiTt6wOa5zxTxQzpTsQ.png" title="The Markdown document was rendered!" >}}
The Markdown document was rendered!

CAVEAT: I didn’t upgrade PyPI because it is too much to bump up for just rendering Markdown. I [tested on test.pypi.org](https://test.pypi.org/project/tabula-py/1.0.0/).

### References

*   [PEP 566](https://www.python.org/dev/peps/pep-0566/#description-content-type-optional)
*   [https://github.com/pypa/readme\_renderer](https://github.com/pypa/readme_renderer)
*   [https://github.com/pypa/sampleproject/pull/66](https://github.com/pypa/sampleproject/pull/66)
