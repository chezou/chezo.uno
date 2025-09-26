---
aliases: [/blog/a-recent-update-of-tabula-py-a923d2ab667b, /blog/a923d2ab667b]
authors: [aki]
categories: [OSS, tabula]
date: '2019-02-17 08:26:00-08:00'
description: This article is a repost of Patreon article published last December.
  I’m planning to bump up next version of tabula-py within few weeks.
projects: [tabula-py]
title: A recent update of tabula-py
keywords: [tabula, py, app, template, oct, extraction, callout, '2019', note, weeks]
recommendations: [/blog/2017-01-09_tabula-py--extract-table-from-pdf-into-python-dataframe-6c7acfa5f302/,
  /blog/2017-05-28_tabula-py-now-able-to-extract-remote-pdf-and-multiple-tables-at-once-6108e24ac07c/,
  /blog/2023-09-09-tabula-py-280/]
---

{{< figure src="./0__9HRqzqcWldOqKJCK.jpg" title="Photo by [Joshua Rawson-Harris](https://unsplash.com/@joshrh19?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)" >}}
Photo by [Joshua Rawson-Harris](https://unsplash.com/@joshrh19?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

_This article is_ [_a repost of Patreon article_](https://www.patreon.com/posts/23407263) _published last December. I’m planning to bump up the next version of tabula-py within few weeks._

> [!NOTE]
> (Note: Oct 7th, 2019)
> As of Oct. 2019, I launched [a documentation site](https://tabula-py.readthedocs.io/en/latest/) and [Google Colab notebook](https://colab.research.google.com/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb) for tabula-py. The FAQ would be good place to execute accurate extraction.

This is my first post on patreon. Apologies for delayed announcement of recent update of tabula-py. I will introduce the key features of updates.

### Use Tabula app template

Tabula app has [**template exporting**](https://github.com/tabulapdf/tabula/pull/711) feature to reuse same bounding box for extraction. tabula-py now load and extract with tabula app’s template.

```py
dfs = tabula.read_pdf_with_template(
  './examples/data.pdf',
  './examples/data.tabula-template.json',
  pandas_options={'header': 0})
```

### Support file-like object

Like many python libraries, tabula-py has been able to [**extract from file-like object**](https://github.com/chezou/tabula-py/pull/105).

```py
# With file-like object  
pdf\_path = ‘tests/resources/data.pdf’  
with open(pdf\_path, ‘rb’) as f:  
  df = tabula.read_pdf(f)

# With pathlib  
from pathlib import Path  
pdf_path = 'tests/resources/data.pdf'
df = tabula.read_pdf(Path(pdf_path))
```

### Allow multiple area option

As of tabula-java v1.0.2, tabula can handle multiple area option.

```py
pdf_path = 'tests/resources/MultiColumn.pdf'
# Relative area  
df_relative = tabula.read_pdf(  
  pdf_path, pages=1,
  area=[[0, 0, 100, 50], [0, 50, 100, 100]], relative_area=True)  

# Absolute area  
  df_absolute = tabula.read_pdf(  
    pdf_path, pages=1, area=[[0, 0, 451, 212], [0, 212, 451, 425]])
```

### Tip: Get table position

This is not a new feature, but I think it might be helpful for some PDFs.  
Detailed post: [**https://github.com/chezou/tabula-py/issues/102**](https://github.com/chezou/tabula-py/issues/102)

`read_pdf` with JSON contains position info, so you can get the table position as follows:

```py
In [5]: tables = read_pdf("./examples/data.pdf", output_format="json", page=2)  
In [9]: top = tables[0]['top']  
In [10]: left = tables[0]['left']
In [11]: bottom = tables[0]['height'] + top  
In [12]: right = tables[0]['width'] + left  
In [13]: top, bottom, left, right  
Out[13]: (0.0, 528.8800048828125, 0.0, 564.8800048828125)
```

If you have any question, ask on [**Stack Overflow**](https://stackoverflow.com/search?q=tabula-py)!

### Other tabula-py articles

*   [https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302)
*   [https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302)
