---
title: "数式入りのmarkdownをSphinxを使ってhtml/pdfにする"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2017-01-22T16:11:24+00:00
lastmod: 2017-01-22T16:11:24+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
Sphinxでmarkdown拡張を扱うためのrecommonmarkというライブラリがあります。 これを使うとreSTではなく、markdownを書いてhtmlやPDFが吐けるようになります。

詳細は以下のエントリにやり方がまとまっています。

&lt;iframe src=&quot;http://tech.3rd-p-zombie.net/embed/2015/12/02/023732&quot; title=&quot;MarkdownでSphinxできるようになったので試してみた（後編） - 意識の高いLISPマシン&quot; class=&quot;embed-card embed-blogcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://tech.3rd-p-zombie.net/entry/2015/12/02/023732&quot;&gt;tech.3rd-p-zombie.net&lt;/a&gt;&lt;/cite&gt;

実は、このrecommonmarkはconfigに設定を書くだけで、数式をmarkdownの中に埋め込めるのでした。

conf.pyの上の方に以下をimportし、

    import recommonmark from recommonmark.parser import CommonMarkParser from recommonmark.transform import AutoStructify

`source_suffix`の修正、`source_parsers`の追加

    source\_suffix = [&#39;.rst&#39;, &#39;.md&#39;] #source\_suffix = &#39;.rst&#39; source\_parsers = { &#39;.md&#39; : &#39;recommonmark.parser.CommonMarkParser&#39; }

最後尾に以下を追加します。

    def setup(app): app.add\_config\_value(&#39;recommonmark\_config&#39;, { &#39;enable\_math&#39;: True, &#39;enable\_inline\_math&#39;: True, }, True) app.add\_transform(AutoStructify)

すると、

     ```math (a + b)^2 = a^2 + 2ab + b^2 ```

とかくと、以下の数式の部分のようになります。([document](http://recommonmark.readthedocs.io/en/latest/auto_structify.html?highlight=language#math-formula))

![](/img/2017/01/22/161124/20170122160632.png)

また、inlineの数式も以下のように書けます。 ([document](http://recommonmark.readthedocs.io/en/latest/auto_structify.html?highlight=language#inline-math))

    This formula `$ y=\sum_{i=1}^n g(x_i) $`

ただ、残念ながら式番号を出す方法はわかりませんでした。

[追記]

&gt; [@chezou](https://twitter.com/chezou) 数式番号ですが、conf.py に math\_number\_all = True を入れるとどうなりますか [https://t.co/tH2ouf7Hk6](https://t.co/tH2ouf7Hk6)
&gt; 
&gt; — shirou - しろう (@r\_rudi) [2017年1月22日](https://twitter.com/r_rudi/status/823117959572832257)

&lt;script async src=&quot;//platform.twitter.com/widgets.js&quot; charset=&quot;utf-8&quot;&gt;&lt;/script&gt;

conf.pyに`math_number_all = True`を足せば数式がでました。ですが、参照はできないと思うので参照が必要な場合はreSTで書く必要があると思います。

[![](https://bot.gyazo.com/c1685a433683cd99590bba5cb6748bae.png)](https://bot.gyazo.com/c1685a433683cd99590bba5cb6748bae.png)&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://gyazo.com/c1685a433683cd99590bba5cb6748bae&quot;&gt;gyazo.com&lt;/a&gt;&lt;/cite&gt;

[/追記]

    $ make latexpdfja

とすれば、PDFが、

    $ make html

とすればhtmlが生成されます。

さくっと書くときにはmarkdownで行けるのはありがたいですね。

Sphinxとlatex環境を用意するのが面倒な人向けに、docker imageも作りましたので活用してみてください。

[https://hub.docker.com/r/chezou/sphinx-recommonmark/](https://hub.docker.com/r/chezou/sphinx-recommonmark/)

### 参考

- [MoreCat Web](http://morec.at/blog/2015/02/24/sphinx-on-docker)

