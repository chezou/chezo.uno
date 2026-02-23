---
authors: [aki]
categories: null
date: '2015-10-12 09:24:25-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2015-10-12 09:24:25-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: 'PyConJP 2015に参加した #pyconjp'
keywords: [pandas, データ, hagino, 解析, pyconjp, '3000', slideshare, python, 技術, www]
recommendations: [/post/2017-09-09_pyconjp-2017------5fa5f59b9bde/, /post/2014-07-05-number-juliatokyo-01de-julia100ben-notuku-wofa-biao-sitekimasita/,
  /post/2015-08-23-yapc-asia-tokyo-2015can-jia-sitekita-number-yapcasia/]
---

はじめてPyConJPに参加してきました。

スライドまとめは以下が詳しいです。<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Ftechstars.jp%2Fblog%2Fpycon15-1%2F" title="もう確認した？PyCon JP 2015、公開済み全スライドまとめ #pyconjp" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://techstars.jp/blog/pycon15-1/">techstars.jp</a></cite>

最近、会社ではJupyter notebookの伝道師として振る舞っており[^1] 、その結果として空前のpandasブームを巻き起こしました。 データ分析/機械学習といえばPythonだよね、というのは[1年以上も前からわかっていたのですが](https://chezo.uno/post/2014-01-18-ke-xue-ji-suan-niokerujun-zhi-hua-aruihanazepythongazhao-shi-nita-yan-yu-nosieawoduo-tuteiruka)、pandas-tdを契機に使い始めてからかなり傾倒しています。[^2] 

そんなpandas周りの話やデータ分析の他社事例が聞ければと思って参加したPyConですが、想像していた以上に参加者のdiversityを感じました。 海外からのスピーカーや参加者も多く、Ruby Kaigiのような国際カンファレンスに近いなという印象を受けました。 また、スタッフや登壇者含め会場の女性の割合が高いため、PyLadiesの効果が出ているんだろうなーという印象を受けました。もしかしたら、RailsGirlsよりもPyLadiesの方が範囲が広いからコミュニティとして長く続いていくのだろうか、とも思いました。

さて、参加して聞いた発表の中でも特に面白かったものを抜粋しようと思います。

## pandasによるデータ加工時の注意点やライブラリの話

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/s8lo31mVVJSQb7" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[pandasによるデータ加工時の注意点やライブラリの話](https://www.slideshare.net/c-bata/pandas-53769651 "pandasによるデータ加工時の注意点やライブラリの話")** from **[Masashi Shibata](http://www.slideshare.net/c-bata)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/c-bata/pandas-53769651">www.slideshare.net</a></cite>

pandasのDataFrameは便利だけど中のデータが保証されないから辛かったので、[panads-validator](https://github.com/c-bata/pandas-validator)作ったよという[c-bata](https://github.com/c-bata/)さんの話。 JSON schemaっぽいなと思いました。

## Daskの話とpandas internal

<iframe allowfullscreen="true" allowtransparency="true" frameborder="0" height="596" id="talk_frame_314840" mozallowfullscreen="true" src="//speakerdeck.com/player/1cca96cdcee843fda18f93f8b20c9485" style="border:0; padding:0; margin:0; background:transparent;" webkitallowfullscreen="true" width="710"></iframe><cite class="hatena-citation"><a href="https://speakerdeck.com/sinhrks/pyconjp-2015-dask-qing-liang-bing-lie-ji-suan-huremuwaku-lightning-talks">speakerdeck.com</a></cite>

<iframe allowfullscreen="true" allowtransparency="true" frameborder="0" height="596" id="talk_frame_314858" mozallowfullscreen="true" src="//speakerdeck.com/player/d3fa3c6563a54ac18e321b8d01a6899c" style="border:0; padding:0; margin:0; background:transparent;" webkitallowfullscreen="true" width="710"></iframe><cite class="hatena-citation"><a href="https://speakerdeck.com/sinhrks/pyconjp-2015-pandas-internals">speakerdeck.com</a></cite>

pandasとDaskのコミッターである[sinhrks](https://twitter.com/sinhrks)さんの発表。 pandasはSciPyの10倍以上のCythonの塊であるとかCategorical Value[^3] を使ったほうが速くなるよとか、pandasの速度出すためのtipsや背景がしれたのは良かったです。また、データ量が増えてきたらDaskのDataFrameを使うと並列処理できるよ、というのも知っていたけどマイクロベンチとともに提示されると使って見たい気持ちが高まりました。

この2つの発表だけで元が取れた感じがしました。

## Pythonで作って学ぶ形態素解析

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/juSG2RLMPcdLMf" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Pyconjp2015 - Python で作って学ぶ形態素解析](https://www.slideshare.net/tomokouchida505/pyconjp2015-python "Pyconjp2015 - Python で作って学ぶ形態素解析")** from **[Tomoko Uchida](http://www.slideshare.net/tomokouchida505)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/tomokouchida505/pyconjp2015-python">www.slideshare.net</a></cite>

IPADICを使って、pure pythonで実装されたMeCab互換の形態素解析器janomeについて、作者の[moco\_beta](https://twitter.com/moco_beta)さんが丁寧に解説してくれました。特にFSTの話はなるほど、図解が分かりやすく良かったです。ただ、いつもフォントサイズが小さいのはなんでだろう...。

なお、janomeの話聞いて帰ってからテンションが上がったので一人sprintして[TinySegmenter.jl](https://github.com/chezou/TinySegmenter.jl)を作ってしまいました。

## アドネットワークのデータ解析を支える技術

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/gJTagoecnaoT6n" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[アドネットワークのデータ解析チームを支える技術](https://www.slideshare.net/hagino_3000/ss-53786917 "アドネットワークのデータ解析チームを支える技術")** from **[hagino 3000](http://www.slideshare.net/hagino_3000)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/hagino_3000/ss-53786917">www.slideshare.net</a></cite>

Voyage groupでこの夏[MLSSにも参加された](http://techlog.voyagegroup.com/entry/mlss2015kyoto) [hagino3000](https://twitter.com/hagino3000)さんのデータ解析チームの話。

特に、14ページ目の広告の広告主、メディア、オーディエンス、Voyage groupのプレーヤーに応じた4つの取り組むべき問題が分かりやすかったので引用します。

<iframe src="//www.slideshare.net/slideshow/embed_code/key/gJTagoecnaoT6n?startSlide=14" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[アドネットワークのデータ解析チームを支える技術](//www.slideshare.net/hagino_3000/ss-53786917 "アドネットワークのデータ解析チームを支える技術")** from **[hagino 3000](//www.slideshare.net/hagino_3000)** 

また、BigQuery版のpandas-tdである[pandas.io.gbq](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.gbq.read_gbq.html)の存在が分かったのも収穫でした。VoyageさんでもJupyter notebookをリポジトリで管理して情報を共有しているとのことなので、自分の選択は間違っていなかったなという気持ちです。

# 雑感

はじめていったPyConJPですが、600人近くの規模を少ないスタッフで取りまとめてくださっているのは感服しました。また、参加者・発表者の diversity が高かったのも良かったです。

また、普段Pythonを使わない人としてはaodagさんの[Packaging最前線](https://pycon.jp/2015/ja/schedule/presentation/46/)はありがたかったです。結構Webのドキュメントはバージョンばらばらで何をやればいいんだっけ、とかWheelなんで嬉しいの？とかわかっていなかったので、初心者には助かりました。

全般的にもう少し事例紹介よりもコアな技術的な話が増えるといいなぁという気もしていたのは、メインがPythonのユーザーじゃないからなのかな。

[^1]: [同僚はpandasとdaruを使い分けています](https://techlife.cookpad.com/entry/201510-jupyter-and-rails)

[^2]: その辺りは近々会社のブログに書こうと思っている

[^3]: DataFrames.jlにはない！