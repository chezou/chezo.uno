---
title: PDFの表をpandasのDataFrameにできる tabula-py 作った
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2016-09-11 22:19:54+00:00
lastmod: 2016-09-11 22:19:54+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [tabula, pdf, py, java, rubykaigi, 実装, table, read, pip, python]
recommendations: [/post/2019-11-25-github actions-issue template/, /post/2016-12-31-2016nian-wozhen-rifan-tute/,
  /post/2018-04-17_---pypi-markdown-----------14e40d90ff3f/]
---
RubyKaigiに参加するとコード書きたいという気持ちが高まって良いのですが、今回はPDFの表を読み込んで pandas の DataFrame に変換できる [tabula-py](https://github.com/chezou/tabula-py)を作りました。 これをもってRubyKaigiの参加報告とさせていただければと思います。

# tabula-pyとは

[tabula](http://tabula.technology/) というJavaで書かれたPDFから表を抽出するライブラリをPythonでうすーくラップしたものです。実装を見てもらえばわかると思いますが、本当にsubprocessでJavaのプログラムを叩いて標準出力で受け取るというだけしかやっていません。

もともとは、Rのtabula実装がかなり色々できるのを知ってPythonがないらしいというので作りました。Rの実装はマジでJavaをごりごり書いていて尊敬の念を抱いています。

[tabulizerパッケージによるPDF表データからのデータ取得](http://suryu.me/20160824_tabulizer_fantastic_extract_data_from_pdf)

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fropenscilabs%2Ftabulizer" title="ropenscilabs/tabulizer" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/ropenscilabs/tabulizer">github.com</a></cite>

# 使い方

インストールは`pip`で入ります。

    pip install tabula-py

こんな感じで使えます。

    from tabula import read\_pdf\_table df = read\_pdf\_table("data.pdf")

詳細はnotebookを見てください。

<iframe src="https://nbviewer.jupyter.org/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb" width="800" height="600"> </iframe>
# RubyKaigiの成果と感想

- rubyist.clubで[@mirakui](https://twitter.com/mirakui)さんをゲストに[収録](https://rubyist.club/10/)した
- tabula-pyを作った
- 個人的には、Julianの[MIDIをdRubyで制御する話](http://rubykaigi.org/2016/presentations/juliancheal.html)が一番おもしろかった。事前にまつださんに聞いていたからこそ辿りつけたのであった
- daru周りは色々と頑張っているけど、visualization周りをどうするかが肝だろうなと思いながら作者と飲めたので良かった
- 機械学習の話は個人的には、sklearnのモデルを読み込んでpredictするとかが良いのかなと思っているので、[Apache Arrow](http://japan.zdnet.com/article/35078163/)とか[feather](https://github.com/wesm/feather)とかみたいにinter-languageな方向を強化していくのがいいんじゃないかなと思いながら聞いていた

# 今後の展望

Py4jを使えばRと同じことができるのは確認ができたのですが、JavaをPythonの上で書かされている感が半端無いので困ったら考えようと思います。


