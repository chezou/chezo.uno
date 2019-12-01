---
title: "NLTKからKyTeaでコーパスを読み込むJPKyteaTokenizer作りました"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2011-09-14T22:02:18+00:00
lastmod: 2011-09-14T22:02:18+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
KyteaをPythonから使うMykytea-pythonを使って、NLTKラッパーを書いてみました。

## NLTKって？
[NLTK](http://www.nltk.org/)といえば、オライリーでも「[入門 自然言語処理](http://www.oreilly.co.jp/books/9784873114705/)」という日本語の書籍が出ているくらいメジャーなPythonの自然言語処理用ライブラリです。ちなみに、日本語の処理の12章は[Webで公開されています](http://nltk.googlecode.com/svn/trunk/doc/book-jp/ch12.html)。  
手っ取り早くエッセンスを掴みたい場合は、nokunoさんの以下の記事がよくまとまっていると思います。

[NLTKで日本語コーパスを扱う方法](http://d.hatena.ne.jp/nokuno/20110821/1313884599)

入門自然言語処理自体は、言語系の人でも自然言語処理に取り組めるように、具体的な事例ベースで書いてあるので、取っつきやすいです。初めて自然言語処理を学ぶ人にも、形態素解析からナイーブベイズや最大エントロピー法といった機械学習の話とそれらを体験できるライブラリの使い方があり、コーパスに対して実際にどう処理されるかを感じることが出来ます。また、Pythonの入門書としても具体例ベースなので、ジェネレータやリスト内包表現などがわかりやすいと思いました。

## JPKyteaTokenizerって？
さて、KyTeaは入門自然言語処理の12章でも名前は紹介されているのですが、Pythonから使えるわけではなかったためか、名前の紹介にとどまっています。

そこで、Mykytea-pythonを使ってnltkでコーパスを読み込むJPKyteaTokenizerを作りました。

ソースはいつも通りgithubにあります。  
[github:JPKyteaTokenizer](https://github.com/chezou/JPKyteaTokenizer)

あらかじめ[KyTea](http://www.phontron.com/kytea/index-ja.html)と[Mykytea-python](http://chezou.wordpress.com/2011/07/15/kytea%e3%82%92ruby-python%e3%81%8b%e3%82%89%e4%bd%bf%e3%81%88%e3%82%8bmykytea%e3%82%92%e4%bd%9c%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/ &quot;KyTea:京都テキスト解析ツールキット をRuby, Pythonから使えるMykyteaを作ってみた&quot;)をインストールしてください。  
使い方は、test\_kyteatokenizer.pyを見ればだいたいわかるとは思いますが、青空文庫の[銀河鉄道の夜](http://www.aozora.gr.jp/cards/000081/files/456_15050.html)をdata/ginga.txtに保存してTokeizeしています。

    #!/usr/bin/env python# -\*- coding: utf-8 -\*-from nltk\_jp import \*from nltk.corpus.reader import \*from nltk.corpus.reader.util import \*import kyteatokenizer jp\_sent\_tokenizer = nltk.RegexpTokenizer(u&#39;[^ 「」！？。]\*[！？。]&#39;) reader = PlaintextCorpusReader(&quot;data/&quot;,r&quot;ginga.txt&quot;, encoding = &#39;utf-8&#39;, para\_block\_reader = read\_line\_block, sent\_tokenizer = jp\_sent\_tokenizer, word\_tokenizer = kyteatokenizer.JPKyteaTokenizer())print &#39; &#39;.join(reader.words()[20:80])

実行すると、こんな感じになります。

    $ python test\_kyteatokenizer.py ふう に 川 だ と 云 （ い ） わ れ たり 、 乳 の 流れ た あと だ と 云 わ れ たり し て い た この ぼんやり と 白 い もの が ほんとう は 何 か ご 承知 で す か 。 」 先生 は 、 黒板 に 吊 （ つる ） し た 大きな 黒 い

本当は、tagged\_words()で品詞とれたり読みもとれたり出来るようにすると嬉しいんだろうけれど。。。

### (蛇足)入門 自然言語処理の誤植
Amazonで買ったのに、第1刷を手に入れることが出来たのですが、[オフィシャル](http://www.oreilly.co.jp/books/9784873114705/)の正誤表に無い誤植がちらほらあるんですね。まだ、全部は目を通していないのですが、気がついたものだけ書いていきます。
- P.88 3.1.4 RSSフィードの処理、1つめのソースコード13行目 nltk.html\_clean → nltk.clean\_html
- P.89 3.1.5 ローカルファイルの読み込み 4つめのソースコード1行目 f 7= open → f = open
- P.224 5.5.7 性能の限界 ソースコード 4行目 nltk.ConfusionMatrix(gold, test) → nltk.ConfusionMatrix(gold\_tags, test\_tags)
- P.228 5.7.3 意味的な手がかり 6行目 「verjaardag」というドイツ語 →&amp;nbsp; 「verjaardag」というオランダ語

