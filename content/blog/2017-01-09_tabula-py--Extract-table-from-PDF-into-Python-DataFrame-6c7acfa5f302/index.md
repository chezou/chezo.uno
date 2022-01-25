---
title: 'tabula-py: Extract table from PDF into Python DataFrame'
description: '(Note: Oct 7th, 2019)As of Oct. 2019, I launched a documentation site
  and Google Colab notebook for tabula-py. The FAQ would be good place…'
date: '2017-01-09T14:09:08+09:00'
categories: [OSS, tabula]
authors: [aki]
aliases: [/blog/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302,
  /blog/6c7acfa5f302]
keywords: [tabula, py, extract, json, java, pdf, tables, table, dataframe, png]
recommendations: [/blog/2017-05-28_tabula-py-now-able-to-extract-remote-pdf-and-multiple-tables-at-once-6108e24ac07c/,
  /blog/2019-02-18_a-recent-update-of-tabula-py-a923d2ab667b/, /blog/2018-04-17_use-markdown-document-on-brand-new-pypi-9723024f09c2/]
---

_(Note: Oct 7th, 2019)  
As of Oct. 2019, I launched_ [_a documentation site_](https://tabula-py.readthedocs.io/en/latest/) _and_ [_Google Colab notebook_](https://colab.research.google.com/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb) _for tabula-py. The FAQ would be good place to execute accurate extraction._

Today, I released tabula-py 0.3.0, which extracts table from PDF into Python pandas’s DataFrame.

[**chezou/tabula-py**  
_tabula-py - Simple wrapper of tabula-java: extract table from PDF into pandas DataFrame_github.com](https://github.com/chezou/tabula-py "https://github.com/chezou/tabula-py")[](https://github.com/chezou/tabula-py)

It is simple wrapper of [tabula-java](https://github.com/tabulapdf/tabula-java) and it enables you to extract table into DataFrame or JSON with Python. You also can extract tables from PDF into CSV, TSV or JSON file.

[tabula](http://tabula.technology/) is a tool to extract tables from PDFs. It is GUI based software, but tabula-java is a tool based on CUI. Though there were [Ruby](http://github.com/tabulapdf/tabula-extractor), [R](https://github.com/leeper/tabulizer), and [Node.js](https://github.com/ezodude/tabula-js) bindings of tabula-java, before tabula-py there isn’t any Python binding of it. I believe PyData is a great ecosystem for data analysis and that’s why I created tabula-py. If you are familiar with R, I highly recommend to use [tabulizer](https://github.com/leeper/tabulizer), which has the most richest bindings including rich GUI.

You can install tabula-py via pip:

pip install tabula-py

With tabula-py, you can get DataFrame with `read_pdf()` method.

{{< figure src="1_w0uPTg2qfvBbmHYEYxqjYw.png" title="example of read_pdf()" >}}
example of read\_pdf()

You can also extract tables as JSON format:

{{< figure src="1_wtSMgtCmBgy15PdP6Lq_jQ.png" title="example of JSON" >}}
example of JSON

You can extract tables into a file like JSON, CSV or TSV with `convert_into()` method.

![](1_tLQ2aqjM_zD_Ls6qNY6E0g.png)
![](1_ir9O2abAz1emEUdVqiwT0Q.png)

You can see more examples in Jupyter notebook.

[**chezou/tabula-py**  
_tabula-py - Simple wrapper of tabula-java: extract table from PDF into pandas DataFrame_github.com](https://github.com/chezou/tabula-py/blob/master/examples/tabula_example.ipynb "https://github.com/chezou/tabula-py/blob/master/examples/tabula_example.ipynb")[](https://github.com/chezou/tabula-py/blob/master/examples/tabula_example.ipynb)

I hope you will enjoy data wrangling with tabula-py. Any feedback would be welcome!

### Waiting for your collaboration!

If you have any trouble with tabula-py, please file [an issue on GitHub](https://github.com/chezou/tabula-py/issues). I don’t want to receive emails because the answer will not share with other people. Make sure to fill [the issue template](https://github.com/chezou/tabula-py/blob/master/.github/ISSUE_TEMPLATE.md), it will reduce many costs for me to solve the problem. Or, I also check StackOverflow. You can ask about it.

#### Other tabula-py articles

*   [https://blog.chezo.uno/tabula-py-now-able-to-extract-remote-pdf-and-multiple-tables-at-once-6108e24ac07c](https://blog.chezo.uno/tabula-py-now-able-to-extract-remote-pdf-and-multiple-tables-at-once-6108e24ac07c)
*   [https://blog.chezo.uno/a-recent-update-of-tabula-py-a923d2ab667b](https://blog.chezo.uno/a-recent-update-of-tabula-py-a923d2ab667b)
