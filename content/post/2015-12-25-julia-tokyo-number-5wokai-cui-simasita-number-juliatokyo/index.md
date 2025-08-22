---
authors: [aki]
categories: null
date: '2015-12-25 13:02:48-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2015-12-25 13:02:48-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: 'Julia Tokyo #5を開催しました #JuliaTokyo'
keywords: [julia, jl, .com, mxnet, juliatokyo, github, そう, 線形, オンライン, julialang]
recommendations: [/post/2015-09-23-mecab-dot-jlwojulia-v0-dot-4-0-rc2nidui-ying-sita/,
  /post/2015-12-10-julianoqing-bao-woshou-ji-situdukeruniha/, /post/2014-12-11-julianopatukezigong-kai-hareplkaradekiru-number-juliaac-number-julialang/]
---

さる12/19に[JuliaTokyoの第五回](http://juliatokyo.connpass.com/event/21715/)を開催しました。[^1] 

togetterのまとめはこちら。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Ftogetter.com%2Fli%2F914680" title="#JuliaTokyo 05 まとめ" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://togetter.com/li/914680">togetter.com</a></cite>

資料はまだいくつかしかアップロードされていませんが、今回は機械学習の話やDeep Learningの話が多かったように思います。

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fjuliatokyo.connpass.com%2Fevent%2F21715%2Fpresentation%2F" title="JuliaTokyo #5 - 資料一覧 - connpass" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://juliatokyo.connpass.com/event/21715/presentation/">juliatokyo.connpass.com</a></cite>

個人的に印象的だったのは、hshindoさんのMerlin.jlです。さくっとDeep Learning用のフレームワークを実装できるのは驚きでした。

また、今回運営サイドとしては、[esa.io](https://esa.io/)さまのスポンサードをいただいており、Slackとの連携出来て嬉しい感じです。

# 本編

## [@sorami](https://twitter.com/sorami) さんのイントロ

<iframe allowfullscreen="true" allowtransparency="true" frameborder="0" height="463" id="talk_frame_323691" mozallowfullscreen="true" src="//speakerdeck.com/player/8a33b8868e974c218084ab559884c579" style="border:0; padding:0; margin:0; background:transparent;" webkitallowfullscreen="true" width="710"></iframe><cite class="hatena-citation"><a href="https://speakerdeck.com/sorami/juliatokyo-number-5-introduction">speakerdeck.com</a></cite>

## [@bicycle1885](https://twitter.com/bicycle1885)さん Juliaチューニングハンズオン

[nelder meadアルゴリズム](https://ja.wikipedia.org/wiki/%E3%83%8D%E3%83%AB%E3%83%80%E3%83%BC%E2%80%93%E3%83%9F%E3%83%BC%E3%83%89%E6%B3%95)を題材に、Juliaのボトルネックをprofileしながら高速化していくハンズオンでした。

[JuliaTokyo#5 ハンズオン (佐藤建太) · GitHub](https://gist.github.com/bicycle1885/626f59ff9e0375573470)

## oyamadさん QuantEcon.jl の DiscreteDP の紹介[^2] 

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Foyamad%2Fpresentations%2Ftree%2Fmaster%2FJuliaTokyo05" title="oyamad/presentations" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/oyamad/presentations/tree/master/JuliaTokyo05">github.com</a></cite>

oyamad先生のゼミ（経済学部）では来年からJuliaが必須になるそうです！

## [kimrin](https://twitter.com/kimrin)さん メカジョさんとジュリアたん

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/8jh4GpSk2RvCjR" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[メカジョさんとジュリアたん♡ (Mechajyo and Julia-tan) #JuliaTokyo #JuliaLang](https://www.slideshare.net/kimrinjp/mechajyo-and-juliatan-juliatokyo-julialang "メカジョさんとジュリアたん♡ (Mechajyo and Julia-tan) #JuliaTokyo #JuliaLang")** from **[Takeshi Kimura](http://www.slideshare.net/kimrinjp)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/kimrinjp/mechajyo-and-juliatan-juliatokyo-julialang">www.slideshare.net</a></cite>

MITのJuliaの研究室ではジュリアたんステッカーがマシンに貼られているそうです。世界を股にかける！

## [@QuantixResearch](https://twitter.com/quantixresearch)さん MXNet.jl+AWS GPU: DeepLearning Super Powers from ~ $0.35hr

Mocha.jlの作者はMXNet.jlに移行したそうです。 というわけで、GPUもCPUも分散で行けるMXNetに移行しよう！という話でした。 AndreさんがAMIも作ったそうです。

> Releasing an [#AWS](https://twitter.com/hashtag/AWS?src=hash) AMI with everything you need to run GPU enabled MXNet.jl[#julialang](https://twitter.com/hashtag/julialang?src=hash)[https://t.co/F0q99h39gR](https://t.co/F0q99h39gR)
> 
> — Andre Pemmelaar (@QuantixResearch) [2015, 12月 19](https://twitter.com/QuantixResearch/status/678179767414222848)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
## [hshindo](https://github.com/hshindo)さん Neural POS-Tagging with Julia

NAISTの松本研では、Pythonを使う学生とF#を使うhshindo先生が共通の言語としてJuliaを使い始めているそうです。 紹介のあったMerin.jlは、characterベースのPOS taggingをNNを使ってやりたかったから作ったとのこと。 パット見たかんじChainerっぽい書き方で、DLができます。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fhshindo%2FMerlin.jl" title="hshindo/Merlin.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/hshindo/Merlin.jl">github.com</a></cite>

資料はこちら。[http://www.hshindo.com/data/shindo-JuliaTokyo5.pdf](http://www.hshindo.com/data/shindo-JuliaTokyo5.pdf)

# LT

## bicycle1885さん v0.5に入りそうな気がする変更

資料

## [いしたー](https://twitter.com/sonicair)さん Juliaでオンライン線形分類器つくった

Exact Soft Confidence Weightedを実装したよ、という話。会場からも実装が綺麗と評判でした。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2FIshitaTakeshi%2FSoftConfidenceWeighted.jl" title="IshitaTakeshi/SoftConfidenceWeighted.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/IshitaTakeshi/SoftConfidenceWeighted.jl">github.com</a></cite>

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/7YVZPx8vmmvpmL" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[Juliaでオンライン線形分類器つくった](https://www.slideshare.net/TakeshiIshita/julia-56356347 "Juliaでオンライン線形分類器つくった")** from **[Takeshi Ishita](http://www.slideshare.net/TakeshiIshita)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/TakeshiIshita/julia-56356347">www.slideshare.net</a></cite>
## [iizukak](https://twitter.com/iizukak)さん Hierarchical Temporal Memory どうでしょう

次回、HTM.jl作ってみた、乞うご期待。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fdocs.google.com%2Fpresentation%2Fd%2F1F6jYDOgXNkbXqqyovXuNksS54Rlbn45aXg98D0H53_g%2Fhtmlpresent" title="Hierarchical Temporal Memory どうでしょう" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://docs.google.com/presentation/d/1F6jYDOgXNkbXqqyovXuNksS54Rlbn45aXg98D0H53_g/htmlpresent">docs.google.com</a></cite>

## [kazoo04](https://twitter.com/kazoo04)さん AROW

[人工知能アドベントカレンダー](http://qiita.com/advent-calendar/2015/ai)でも有名なkazoo04さんのAROW.jlの話。 SCWにAROWにとオンライン学習アルゴリズムが一通り揃った感ありますね。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fkazoo04%2FAROW.jl" title="kazoo04/AROW.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/kazoo04/AROW.jl">github.com</a></cite>

## [olanleed](https://twitter.com/olanleed)さん JuliaでCUDAを扱うのはらく～だ

全然楽じゃなさそうです...。maleadtさんのCUDA.jlが理想に近いそうですが、上手く動かないという...

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fmaleadt%2FCUDA.jl" title="maleadt/CUDA.jl" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/maleadt/CUDA.jl">github.com</a></cite>

<iframe src="https://www.slideshare.net/slideshow/embed_code/key/74PF7HHKo1xvTs" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

  **[JuliaでCUDAを扱うのはらく〜だ](https://www.slideshare.net/tomohiromito/julia-tokyo "JuliaでCUDAを扱うのはらく〜だ")** from **[Tomohiro Mito](http://www.slideshare.net/tomohiromito)** 
<cite class="hatena-citation"><a href="http://www.slideshare.net/tomohiromito/julia-tokyo">www.slideshare.net</a></cite>
## [ysekky\_](https://twitter.com/ysekky_)さん テキスト分析

MeCab.jlとTextAnalysis.jlを使ったテキスト分析の話でした。JMW仕事しろ案件

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fysekky%2Fitems%2Fcdb6ed28b903e4719bea" title="Juliaでテキスト分析をしてみる - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://qiita.com/ysekky/items/cdb6ed28b903e4719bea">qiita.com</a></cite>

## [ohtaman](https://twitter.com/ohtaman)さん 声質変換

福山雅治が歌う関白宣言を、さだまさしが歌うように声質変換する！ということで胸熱な話でした。 続編があるようで、期待大です。

# まとめと雑感

懇親会では、[@sfchaos](https://twitter.com/sfchaos)さん寄贈「データサイエンティスト養成読本　機械学習入門編」争奪じゃんけん大会がありました。

まさか、遠方からの参戦があるなど日本全国にJuliaが広がっている機運が高まっています。Advent Calendarも無事終わって、時代はJuliaですね！

<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fqiita.com%2Fadvent-calendar%2F2015%2Fjulialang" title="Julia Advent Calendar 2015 - Qiita" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://qiita.com/advent-calendar/2015/julialang">qiita.com</a></cite>

[^1]: 週3勉強会開催のフィニッシュdayでした

[^2]: どうでもいいけど、はてなブログPDFをgithub上の埋め込むすべがないな。。。