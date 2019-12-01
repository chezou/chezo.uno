---
title: "pip install kyteaできるようになりました"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-06-06T17:14:41+00:00
lastmod: 2015-06-06T17:14:41+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
先月のkawasaki.rbで、Rubyistなのにgemより先にPypiデビューしましたという話をしました。

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/nzuS2SusU9LaBR&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[Rubyistがgemの前にPypiデビューするのは間違っているだろうか](https://www.slideshare.net/chezou/py-48654458 &quot;Rubyistがgemの前にPypiデビューするのは間違っているだろうか&quot;)** from **[康顕 有賀](http://www.slideshare.net/chezou)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/chezou/py-48654458&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

中身は、kyteaをpipから入れられるようにしたよということですが、ちょっとsetup.pyへの恨み節も入ってます。 SWIGに対応している[雰囲気を醸し出して](http://docs.python.jp/2/distutils/setupscript.html)、実は[カスタムビルドしてね](http://stackoverflow.com/questions/12491328/python-distutils-not-include-the-swig-generated-module)とか、しかもその[issue 6年前にできて最近1年位放置](https://bugs.python.org/issue7562)とか...。 SWIGオワコンなんですかねぇ。

`bundle gem`みたいな方法が確立してないから、ディレクトリ構成もよくわからないんですよね。

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Fkytea%2F0.1.0&quot; title=&quot;kytea 0.1.0 : Python Package Index&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;a href=&quot;https://pypi.python.org/pypi/kytea/0.1.0&quot;&gt;kytea 0.1.0 : Python Package Index&lt;/a&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://pypi.python.org/pypi/kytea/0.1.0&quot;&gt;pypi.python.org&lt;/a&gt;&lt;/cite&gt;

一応、gem化も進めていますがあまり需要がなさそうなので、真面目にやっていません。

### 参考

[setup スクリプトを書く — Python 2.7ja1 documentation](http://docs.python.jp/2/distutils/setupscript.html)

[はじめの一歩 — Pythonパッケージ ヒッチハイク・ガイド v1.0 documentation](http://shimizukawa.bitbucket.org/python-distribute-ja/quickstart.html)

&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fedvakf%40github%2Fitems%2Fd82cd7ab77ea2b88506c&quot; title=&quot;Python - PyPIにパッケージ登録する - Qiita&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;a href=&quot;http://qiita.com/edvakf@github/items/d82cd7ab77ea2b88506c&quot;&gt;Python - PyPIにパッケージ登録する - Qiita&lt;/a&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://qiita.com/edvakf@github/items/d82cd7ab77ea2b88506c&quot;&gt;qiita.com&lt;/a&gt;&lt;/cite&gt;


