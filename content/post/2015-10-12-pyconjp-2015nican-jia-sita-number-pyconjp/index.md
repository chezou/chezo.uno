---
title: "PyConJP 2015に参加した #pyconjp"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-10-12T16:24:25+00:00
lastmod: 2015-10-12T16:24:25+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
はじめてPyConJPに参加してきました。

スライドまとめは以下が詳しいです。&lt;iframe src=&quot;//hatenablog-parts.com/embed?url=https%3A%2F%2Ftechstars.jp%2Fblog%2Fpycon15-1%2F&quot; title=&quot;もう確認した？PyCon JP 2015、公開済み全スライドまとめ #pyconjp&quot; class=&quot;embed-card embed-webcard&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://techstars.jp/blog/pycon15-1/&quot;&gt;techstars.jp&lt;/a&gt;&lt;/cite&gt;

最近、会社ではJupyter notebookの伝道師として振る舞っており\*1、その結果として空前のpandasブームを巻き起こしました。 データ分析/機械学習といえばPythonだよね、というのは[1年以上も前からわかっていたのですが](http://chezou.hatenablog.com/entry/20140118/1389978078)、pandas-tdを契機に使い始めてからかなり傾倒しています。\*2

そんなpandas周りの話やデータ分析の他社事例が聞ければと思って参加したPyConですが、想像していた以上に参加者のdiversityを感じました。 海外からのスピーカーや参加者も多く、Ruby Kaigiのような国際カンファレンスに近いなという印象を受けました。 また、スタッフや登壇者含め会場の女性の割合が高いため、PyLadiesの効果が出ているんだろうなーという印象を受けました。もしかしたら、RailsGirlsよりもPyLadiesの方が範囲が広いからコミュニティとして長く続いていくのだろうか、とも思いました。

さて、参加して聞いた発表の中でも特に面白かったものを抜粋しようと思います。

## pandasによるデータ加工時の注意点やライブラリの話

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/s8lo31mVVJSQb7&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[pandasによるデータ加工時の注意点やライブラリの話](https://www.slideshare.net/c-bata/pandas-53769651 &quot;pandasによるデータ加工時の注意点やライブラリの話&quot;)** from **[Masashi Shibata](http://www.slideshare.net/c-bata)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/c-bata/pandas-53769651&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

pandasのDataFrameは便利だけど中のデータが保証されないから辛かったので、[panads-validator](https://github.com/c-bata/pandas-validator)作ったよという[c-bata](https://github.com/c-bata/)さんの話。 JSON schemaっぽいなと思いました。

## Daskの話とpandas internal

&lt;iframe allowfullscreen=&quot;true&quot; allowtransparency=&quot;true&quot; frameborder=&quot;0&quot; height=&quot;596&quot; id=&quot;talk_frame_314840&quot; mozallowfullscreen=&quot;true&quot; src=&quot;//speakerdeck.com/player/1cca96cdcee843fda18f93f8b20c9485&quot; style=&quot;border:0; padding:0; margin:0; background:transparent;&quot; webkitallowfullscreen=&quot;true&quot; width=&quot;710&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://speakerdeck.com/sinhrks/pyconjp-2015-dask-qing-liang-bing-lie-ji-suan-huremuwaku-lightning-talks&quot;&gt;speakerdeck.com&lt;/a&gt;&lt;/cite&gt;

&lt;iframe allowfullscreen=&quot;true&quot; allowtransparency=&quot;true&quot; frameborder=&quot;0&quot; height=&quot;596&quot; id=&quot;talk_frame_314858&quot; mozallowfullscreen=&quot;true&quot; src=&quot;//speakerdeck.com/player/d3fa3c6563a54ac18e321b8d01a6899c&quot; style=&quot;border:0; padding:0; margin:0; background:transparent;&quot; webkitallowfullscreen=&quot;true&quot; width=&quot;710&quot;&gt;&lt;/iframe&gt;&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;https://speakerdeck.com/sinhrks/pyconjp-2015-pandas-internals&quot;&gt;speakerdeck.com&lt;/a&gt;&lt;/cite&gt;

pandasとDaskのコミッターである[sinhrks](https://twitter.com/sinhrks)さんの発表。 pandasはSciPyの10倍以上のCythonの塊であるとかCategorical Value\*3を使ったほうが速くなるよとか、pandasの速度出すためのtipsや背景がしれたのは良かったです。また、データ量が増えてきたらDaskのDataFrameを使うと並列処理できるよ、というのも知っていたけどマイクロベンチとともに提示されると使って見たい気持ちが高まりました。

この2つの発表だけで元が取れた感じがしました。

## Pythonで作って学ぶ形態素解析

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/juSG2RLMPcdLMf&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[Pyconjp2015 - Python で作って学ぶ形態素解析](https://www.slideshare.net/tomokouchida505/pyconjp2015-python &quot;Pyconjp2015 - Python で作って学ぶ形態素解析&quot;)** from **[Tomoko Uchida](http://www.slideshare.net/tomokouchida505)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/tomokouchida505/pyconjp2015-python&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

IPADICを使って、pure pythonで実装されたMeCab互換の形態素解析器janomeについて、作者の[moco\_beta](https://twitter.com/moco_beta)さんが丁寧に解説してくれました。特にFSTの話はなるほど、図解が分かりやすく良かったです。ただ、いつもフォントサイズが小さいのはなんでだろう...。

なお、janomeの話聞いて帰ってからテンションが上がったので一人sprintして[TinySegmenter.jl](https://github.com/chezou/TinySegmenter.jl)を作ってしまいました。

## アドネットワークのデータ解析を支える技術

&lt;iframe src=&quot;https://www.slideshare.net/slideshow/embed_code/key/gJTagoecnaoT6n&quot; width=&quot;427&quot; height=&quot;356&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[アドネットワークのデータ解析チームを支える技術](https://www.slideshare.net/hagino_3000/ss-53786917 &quot;アドネットワークのデータ解析チームを支える技術&quot;)** from **[hagino 3000](http://www.slideshare.net/hagino_3000)** 
&lt;cite class=&quot;hatena-citation&quot;&gt;&lt;a href=&quot;http://www.slideshare.net/hagino_3000/ss-53786917&quot;&gt;www.slideshare.net&lt;/a&gt;&lt;/cite&gt;

Voyage groupでこの夏[MLSSにも参加された](http://techlog.voyagegroup.com/entry/mlss2015kyoto) [hagino3000](https://twitter.com/hagino3000)さんのデータ解析チームの話。

特に、14ページ目の広告の広告主、メディア、オーディエンス、Voyage groupのプレーヤーに応じた4つの取り組むべき問題が分かりやすかったので引用します。

&lt;iframe src=&quot;//www.slideshare.net/slideshow/embed_code/key/gJTagoecnaoT6n?startSlide=14&quot; width=&quot;425&quot; height=&quot;355&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot; style=&quot;border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;&quot; allowfullscreen&gt; &lt;/iframe&gt;

  **[アドネットワークのデータ解析チームを支える技術](//www.slideshare.net/hagino_3000/ss-53786917 &quot;アドネットワークのデータ解析チームを支える技術&quot;)** from **[hagino 3000](//www.slideshare.net/hagino_3000)** 

また、BigQuery版のpandas-tdである[pandas.io.gbq](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.gbq.read_gbq.html)の存在が分かったのも収穫でした。VoyageさんでもJupyter notebookをリポジトリで管理して情報を共有しているとのことなので、自分の選択は間違っていなかったなという気持ちです。

# 雑感

はじめていったPyConJPですが、600人近くの規模を少ないスタッフで取りまとめてくださっているのは感服しました。また、参加者・発表者の diversity が高かったのも良かったです。

また、普段Pythonを使わない人としてはaodagさんの[Packaging最前線](https://pycon.jp/2015/ja/schedule/presentation/46/)はありがたかったです。結構Webのドキュメントはバージョンばらばらで何をやればいいんだっけ、とかWheelなんで嬉しいの？とかわかっていなかったので、初心者には助かりました。

全般的にもう少し事例紹介よりもコアな技術的な話が増えるといいなぁという気もしていたのは、メインがPythonのユーザーじゃないからなのかな。

\*1:[同僚はpandasとdaruを使い分けています](http://techlife.cookpad.com/entry/201510-jupyter-and-rails)

\*2:その辺りは近々会社のブログに書こうと思っている

\*3:DataFrames.jlにはない！


