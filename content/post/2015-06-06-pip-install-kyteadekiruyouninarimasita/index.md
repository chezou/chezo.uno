---
authors: [aki]
categories: null
date: '2015-06-06 10:14:41-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2015-06-06 10:14:41-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: pip install kyteaできるようになりました
keywords: [gem, pypi, デビュー, python, rubyist, documentation, setup, swig, kytea, パッケージ]
recommendations: [/post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/,
  /post/2019-11-25-github actions-api token-pypi release/, /post/2017-08-26_python------------------dc8d8f2fe989/]
---

先月のkawasaki.rbで、Rubyistなのにgemより先にPypiデビューしましたという話をしました。

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/nzuS2SusU9LaBR" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Rubyistがgemの前にPypiデビューするのは間違っているだろうか](https://www.slideshare.net/chezou/py-48654458 "Rubyistがgemの前にPypiデビューするのは間違っているだろうか")** from **[康顕 有賀](http://www.slideshare.net/chezou)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/chezou/py-48654458">www.slideshare.net</a></cite>

中身は、kyteaをpipから入れられるようにしたよということですが、ちょっとsetup.pyへの恨み節も入ってます。 SWIGに対応している[雰囲気を醸し出して](http://docs.python.jp/2/distutils/setupscript.html)、実は[カスタムビルドしてね](http://stackoverflow.com/questions/12491328/python-distutils-not-include-the-swig-generated-module)とか、しかもその[issue 6年前にできて最近1年位放置](https://bugs.python.org/issue7562)とか...。 SWIGオワコンなんですかねぇ。

`bundle gem`みたいな方法が確立してないから、ディレクトリ構成もよくわからないんですよね。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Fkytea%2F0.1.0" title="kytea 0.1.0 : Python Package Index" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="https://pypi.python.org/pypi/kytea/0.1.0">kytea 0.1.0 : Python Package Index</a></iframe><cite class="hatena-citation"><a href="https://pypi.python.org/pypi/kytea/0.1.0">pypi.python.org</a></cite>

一応、gem化も進めていますがあまり需要がなさそうなので、真面目にやっていません。

### 参考

[setup スクリプトを書く — Python 2.7ja1 documentation](http://docs.python.jp/2/distutils/setupscript.html)

[はじめの一歩 — Pythonパッケージ ヒッチハイク・ガイド v1.0 documentation](http://shimizukawa.bitbucket.org/python-distribute-ja/quickstart.html)

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fedvakf%40github%2Fitems%2Fd82cd7ab77ea2b88506c" title="Python - PyPIにパッケージ登録する - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"><a href="http://qiita.com/edvakf@github/items/d82cd7ab77ea2b88506c">Python - PyPIにパッケージ登録する - Qiita</a></iframe><cite class="hatena-citation"><a href="http://qiita.com/edvakf@github/items/d82cd7ab77ea2b88506c">qiita.com</a></cite>