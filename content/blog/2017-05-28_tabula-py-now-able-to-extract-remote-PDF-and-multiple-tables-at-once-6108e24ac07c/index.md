---
title: tabula-py now able to extract remote PDF and multiple tables at once
description: '(Note: Oct 7th, 2019)As of Oct. 2019, I launched a documentation site
  and Google Colab notebook for tabula-py. The FAQ would be good place…'
date: '2017-05-28T11:18:39+09:00'
categories: [OSS, tabula]
authors: [aki]
projects: [tabula-py]
aliases: [/blog/tabula-py-now-able-to-extract-remote-PDF-and-multiple-tables-at-once-6108e24ac07c,
  /blog/6108e24ac07c]
keywords: [tabula, py, pdf, add, remote, extract, path, url, oct, callout]
recommendations: [/blog/2017-01-09_tabula-py--extract-table-from-pdf-into-python-dataframe-6c7acfa5f302/,
  /blog/2019-02-18_a-recent-update-of-tabula-py-a923d2ab667b/, /blog/2023-09-09-tabula-py-280/]
---

{{% callout note %}}
(Note: Oct 7th, 2019)
As of Oct. 2019, I launched [a documentation site](https://tabula-py.readthedocs.io/en/latest/) and [Google Colab notebook](https://colab.research.google.com/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb) for tabula-py. The FAQ would be good place to execute accurate extraction.
{{% /callout %}}

tabula-py is a Python library which enables you to extract tables from PDF into pandas DataFrames. Today, I released v0.8.0. In this post, I will introduce improvements after previous post of tabula-py. If you don’t familiar with tabula-py, you can see previous one.

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/blog/2017-01-09_tabula-py--extract-table-from-pdf-into-python-dataframe-6c7acfa5f302/" data-iframely-url="//iframely.net/WEoEyU7"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

### Change Notes

*   Able to read remote PDF passing URL
*   \[Experimental\] Add `multiple_tables` mode
*   Add batch conversion method:`convert_into_by_batch()`
*   Add `encoding` option
*   Add `java_options`
*   Will deprecate `read_pdf_table()` method

I will explain important features.

#### Read remote PDF passing URL

If you want extract a DataFrame from the internet, you can extract remote PDF without downloading it manually.

```py
read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/12s0324.pdf")
```

#### \[Experimental\] Add "`multiple_tables"` mode

tabula-py is a simple wrapper of tabula-java, it was hard to handle multiple tables in a page. But now, you can extract multiple tables in a page using `multiple_tables` option.

```py
read_pdf('tests/resources/data.pdf', pages=2, multiple_tables=True)
```

This function create a list of DataFrames via JSON from tabula-java, so if tabula-java’s JSON format will change, the output could be broken. If you see `CParserError` , try to set `multiple_tables` option.

#### Add batch conversion method: "`convert_into_by_batch()"`

After tabula-java v0.9.2, we can extract tables from PDF by batch. You can use this function through `convert_into_by_batch()` method.

```py
convert_into_by_batch(path_to_dir, output_format='csv')
```

You should set directory path of PDFs, not the specific pdf path.

tabula-py extracts tables same directory as input files.

### TODOs

There are several problems those may be fixed after releasing of tabula-java 0.9.3. e.g) Handling embedded font, including Japanese…

### Waiting for your collaboration!

If you have any troubles with tabula-py, please file [an issue on GitHub](https://github.com/chezou/tabula-py/issues). I don’t want to receive emails because the answer will not share to other people. Make sure fill [the issue template](https://github.com/chezou/tabula-py/blob/master/.github/ISSUE_TEMPLATE.md), it will reduce many costs for me to solve the problem.

#### Other tabula-py articles

*   [https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302)
*   [https://blog.chezo.uno/a-recent-update-of-tabula-py-a923d2ab667b](https://blog.chezo.uno/a-recent-update-of-tabula-py-a923d2ab667b)
