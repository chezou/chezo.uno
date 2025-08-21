---
title: Gitlab CIを使ってSphinxのドキュメントを自動でPDFにビルドする
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2017-01-23 12:38:35+00:00
lastmod: 2017-01-23 12:38:35+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [gitlab, pdf, ci, sphinx, image, master, 生成, paths, markdown, レポジトリ]
recommendations: [/post/2017-01-22-shu-shi-ru-rinomarkdownwosphinxwoshi-tutehtml-slash-pdfnisuru/,
  /post/2017-04-08-docker-imagewoyong-yi-sitewindows-slash-macosdesumuzunitong-ren-zhi-wozuo-tutahua-sphinxbian/,
  /post/2016-09-11-pdfnobiao-wopandasnodataframenidekiru-tabula-py-zuo-tuta/]
---
gitlab.comは自前でDocker image登録できたり、CI持っていたりと便利ですね。しかも、privateレポジトリもお金かからないという太っ腹。 技術書典2に向けたレポジトリはgitlab.comで管理しています。

今回は共著者にPython使いが多いためSphinxを使って書いているんですが、Sphinxはcommon markでも書けるのでmarkdownでも文章を書くことが出来ます。

前回の記事では、数式入りのmarkdownからPDFを生成するDocker imageを作りましたが、それを使うと簡単にGitlab-CIでPDFが生成できます。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/post/2017-01-22-shu-shi-ru-rinomarkdownwosphinxwoshi-tutehtml-slash-pdfnisuru/" data-iframely-url="//iframely.net/7zd0Evy"></a></div></div><script async src="//iframely.net/embed.js" charset="utf-8"></script>

やり方は簡単、あなたのSphinxのプロジェクトに、以下のような`.gitlab-ci.yml`を書くだけ。もちろん、必要に応じてpathsは変更してください。

    image: chezou/sphinx-recommonmark:latest pdf: script: - make latexpdfja artifacts: paths: - build/latex/techbookfest02.pdf only: - master

こうすると、masterにpushしてCIが成功する度に、PDFが生成されてダウンロードできます。

![](20170123123725.png)

めっちゃ簡単。お試しあれ。
