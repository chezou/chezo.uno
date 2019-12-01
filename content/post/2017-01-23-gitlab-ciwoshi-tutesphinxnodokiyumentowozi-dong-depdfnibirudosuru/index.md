---
title: "Gitlab CIを使ってSphinxのドキュメントを自動でPDFにビルドする"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2017-01-23T12:38:35+00:00
lastmod: 2017-01-23T12:38:35+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
gitlab.comは自前でDocker image登録できたり、CI持っていたりと便利ですね。しかも、privateレポジトリもお金かからないという太っ腹。 技術書典2に向けたレポジトリはgitlab.comで管理しています。

今回は共著者にPython使いが多いためSphinxを使って書いているんですが、Sphinxはcommon markでも書けるのでmarkdownでも文章を書くことが出来ます。

前回の記事では、数式入りのmarkdownからPDFを生成するDocker imageを作りましたが、それを使うと簡単にGitlab-CIでPDFが生成できます。

&lt;iframe src=&quot;http://chezou.hatenablog.com/embed/2017/01/22/161124&quot; title=&quot;数式入りのmarkdownをSphinxを使ってhtml/pdfにする - once upon a time,&quot; class=&quot;embed-card embed-blogcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 190px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://chezou.hatenablog.com/entry/2017/01/22/161124&quot;&gt;chezou.hatenablog.com&lt;/a&gt;&lt;/cite&gt;

やり方は簡単、あなたのSphinxのプロジェクトに、以下のような`.gitlab-ci.yml`を書くだけ。もちろん、必要に応じてpathsは変更してください。

    image: chezou/sphinx-recommonmark:latest pdf: script: - make latexpdfja artifacts: paths: - build/latex/techbookfest02.pdf only: - master

こうすると、masterにpushしてCIが成功する度に、PDFが生成されてダウンロードできます。

![](/img/2017/01/23/123835/20170123123725.png)

めっちゃ簡単。お試しあれ。


