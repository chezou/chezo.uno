---
title: 数式入りのmarkdownをSphinxを使ってhtml/pdfにする
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2017-01-22 16:11:24+00:00
lastmod: 2017-01-22 16:11:24+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [markdown, recommonmark, html, sphinx, 3rd, conf, 拡張, rest, latex, 以下]
recommendations: [/post/2017-01-23-gitlab-ciwoshi-tutesphinxnodokiyumentowozi-dong-depdfnibirudosuru/,
  /post/2017-04-08-docker-imagewoyong-yi-sitewindows-slash-macosdesumuzunitong-ren-zhi-wozuo-tutahua-sphinxbian/,
  /post/2018-04-17_---pypi-markdown-----------14e40d90ff3f/]
---
Sphinxでmarkdown拡張を扱うためのrecommonmarkというライブラリがあります。 これを使うとreSTではなく、markdownを書いてhtmlやPDFが吐けるようになります。

詳細は以下のエントリにやり方がまとまっています。

<iframe src="https://sky-y.hatenablog.jp/embed/2015/12/02/023732" title="MarkdownでSphinxできるようになったので試してみた（後編） - 意識の高いLISPマシン" class="embed-card embed-blogcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://sky-y.hatenablog.jp/entry/2015/12/02/023732">tech.3rd-p-zombie.net</a></cite>

実は、このrecommonmarkはconfigに設定を書くだけで、数式をmarkdownの中に埋め込めるのでした。

conf.pyの上の方に以下をimportし、

```py
import recommonmark from recommonmark.parser
import CommonMarkParser from recommonmark.transform
import AutoStructify
```

`source_suffix`の修正、`source_parsers`の追加

```py
source_suffix = [".rst", ".md"]
#source_suffix = ".rst"
source_parsers = { ".md" : "recommonmark.parser.CommonMarkParser" }
```

最後尾に以下を追加します。

```py
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        { "enable_math": True, "enable_inline_math": True, },
        True)
    app.add_transform(AutoStructify)
```

すると、

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

とかくと、以下の数式の部分のようになります。([document](http://recommonmark.readthedocs.io/en/latest/auto_structify.html?highlight=language#math-formula))

![](20170122160632.png)

また、inlineの数式も以下のように書けます。 ([document](http://recommonmark.readthedocs.io/en/latest/auto_structify.html?highlight=language#inline-math))

```rst
This formula `$ y=\sum_{i=1}^n g(x_i) $`
```

ただ、残念ながら式番号を出す方法はわかりませんでした。

[追記]

{{< tweet user="r_rudi" id="823117959572832257" >}}

conf.pyに`math_number_all = True`を足せば数式がでました。ですが、参照はできないと思うので参照が必要な場合はreSTで書く必要があると思います。

{{< figure src="https://bot.gyazo.com/c1685a433683cd99590bba5cb6748bae.png" title="math_number_all=True" >}}

[/追記]

```sh
$ make latexpdfja
```

とすれば、PDFが、

```sh
$ make html
```

とすればhtmlが生成されます。

さくっと書くときにはmarkdownで行けるのはありがたいですね。

Sphinxとlatex環境を用意するのが面倒な人向けに、docker imageも作りましたので活用してみてください。

[https://hub.docker.com/r/chezou/sphinx-recommonmark/](https://hub.docker.com/r/chezou/sphinx-recommonmark/)

### 参考

- [MoreCat Web](http://morec.at/blog/2015/02/24/sphinx-on-docker)
