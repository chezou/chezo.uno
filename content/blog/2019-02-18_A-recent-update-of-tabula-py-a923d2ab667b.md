---
title: A recent update of tabula-py
description: >-
  This article is a repost of Patreon article published last December. I’m
  planning to bump up next version of tabula-py within few weeks.
date: '2019-02-18T01:26:00.242Z'
categories: [OSS]
keywords: [tabula-py]
---

![Photo by [Joshua Rawson-Harris](https://unsplash.com/@joshrh19?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](/img/0__9HRqzqcWldOqKJCK.jpg)
Photo by [Joshua Rawson-Harris](https://unsplash.com/@joshrh19?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

_This article is_ [_a repost of Patreon article_](https://www.patreon.com/posts/23407263) _published last December. I’m planning to bump up the next version of tabula-py within few weeks._

_(Note: Oct 7th, 2019)  
As of Oct. 2019, I launched_ [_a documentation site_](https://tabula-py.readthedocs.io/en/latest/) _and_ [_Google Colab notebook_](https://colab.research.google.com/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb) _for tabula-py. The FAQ would be good place to execute accurate extraction._

This is my first post on patreon. Apologies for delayed announcement of recent update of tabula-py. I will introduce the key features of updates.

### Use Tabula app template

Tabula app has [**template exporting**](https://github.com/tabulapdf/tabula/pull/711) feature to reuse same bounding box for extraction. tabula-py now load and extract with tabula app’s template.

> _dfs =_ [**_tabula.read_**](http://tabula.read/)_\_pdf\_with\_template(‘./examples/data.pdf’, ‘./examples/data.tabula-template.json’, pandas\_options={‘header’: 0})_

### Support file-like object

Like many python libraries, tabula-py has been able to [**extract from file-like object**](https://github.com/chezou/tabula-py/pull/105).

> _\# With file-like object  
> pdf\_path = ‘tests/resources/data.pdf’  
> with open(pdf\_path, ‘rb’) as f:  
>  df =_ [**_tabula.read_**](http://tabula.read/)_\_pdf(f)_

> _\# With pathlib  
> from pathlib import Path  
> pdf\_path = ‘tests/resources/data.pdf’  
> df =_ [**_tabula.read_**](http://tabula.read/)_\_pdf(Path(pdf\_path))_

### Allow multiple area option

As of tabula-java v1.0.2, tabula can handle multiple area option.

> _pdf\_path = ‘tests/resources/MultiColumn.pdf’  
> \# Relative area  
> df\_relative =_ [**_tabula.read_**](http://tabula.read/)_\_pdf(  
>  pdf\_path, pages=1, area=\[\[0, 0, 100, 50\], \[0, 50, 100, 100\]\], relative\_area=True)  
> \# Absolute area  
> df\_absolute =_ [**_tabula.read_**](http://tabula.read/)_\_pdf(  
>  pdf\_path, pages=1, area=\[\[0, 0, 451, 212\], \[0, 212, 451, 425\]\])_

### Tip: Get table position

This is not a new feature, but I think it might be helpful for some PDFs.  
Detailed post: [**https://github.com/chezou/tabula-py/issues/102**](https://github.com/chezou/tabula-py/issues/102)

read\_pdf with JSON contains position info, so you can get the table position as follows:

> _In \[5\]: tables = read\_pdf(“./examples/data.pdf”, output\_format=”json”, page=2)  
> In \[9\]: top = tables\[0\]\[‘top’\]  
> In \[10\]: left = tables\[0\]\[‘left’\]  
> In \[11\]: bottom = tables\[0\]\[‘height’\] + top  
> In \[12\]: right = tables\[0\]\[‘width’\] + left  
> In \[13\]: top, bottom, left, right  
> Out\[13\]: (0.0, 528.8800048828125, 0.0, 564.8800048828125)_

If you have any question, ask on [**Stack Overflow**](https://stackoverflow.com/search?q=tabula-py)!

### Other tabula-py articles

*   [https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302)
*   [https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302)