---
authors:
- aki
categories: null
date: '2015-12-24 16:00:00-08:00'
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
keywords:
- julia
- 言語
- 開催
- 情報
- エヴァンジェリスト
- advent
- juliatokyo
- 日本語
- 負荷
- calendar
lastmod: '2015-12-24 16:00:00-08:00'
projects: []
recommendations:
- /post/2015-12-10-julianoqing-bao-woshou-ji-situdukeruniha/
- /post/2014-12-13-number-japanr-dehua-ti-datuta-detasaienteisutoyang-cheng-du-ben-rhuo-yong-bian-tong-cheng-juliaru-men-ben-wodu-mimasita-number-juliaac/
- /post/2015-04-26-number-juliatokyo-de-number-juliawakaran-toiuza-narepozitoriwoli-tetahua-wositara-julia-dot-tokyo-gadekiteta/
subtitle: ''
summary: ''
tags: []
title: 'Juliaで得られたマイナー言語を盛り上げる方法 #JuliaAC'
---

この記事は[Julia Advent Calender 2015](http://qiita.com/advent-calendar/2015/julialang)の最終日です。

Juliaは大分マイナーな言語で、日本語による情報が殆ど無かったのですが、以下の要因で大分盛り上がってきていると思います。

1. イベント（JuliaTokyo）を年数回開催している
2. Advent Calendarを毎年開催している
3. エヴァンジェリスト(a.k.a bicycle1885)が宣伝し続ける

# 1. イベントを年に何回か開催する

最近は大分3つ目の要素がでかいなと思ってきているのですが、 そもそものJuliaTokyoのスタートとしては僕がMachine Learning Casual Talksを開催したところ、偶々来ていたbicycle1885さんがいたということと、Tokyo.RでJuliaの宣伝をしていた[sorami](https://twitter.com/sorami)さんとで意気投合して始めました。

この手のマイナー言語の通例としては英語圏でなんだか盛り上がっているらしいぞ、でも日本語の情報もないし何が嬉しいんだっけ？というケースが圧倒的に多いと思うのですが、やる気のある人が3人いれば勉強会を継続的に開催できます。[^1] 負荷分散大事。

最近は、[esa.io様](http://esa.io/)にスポンサードもしていただいて、情報の共有も少しずつすすめております。[^2] 

# 2. Advent Calendarを毎年開催する

かなり広がりを感じたのがQiitaで開催した[2014年のAdvent Calendar](http://qiita.com/advent-calendar/2014/julialang)です。 きっかけは同僚の[gfx](https://twitter.com/ __gfx__ )氏に煽られてはじめたのですが、何とか25日埋まって良かったです。[^3] 

Qiitaは最近情報が溢れてきて質が云々とかいう議論がたまに出てくるのを見かけるのですが、ことJuliaに関して言えば「試してみた」「installしてみた」とかでも全然情報としては価値がありますし、投稿していただけるととてもうれしいです。  
JuliaTokyo名物「Juliaはじめて24時間以内枠」というLT枠がいつもなんとなくあるのですが、こうした気軽にやってみた/作ってみた/試してみたという行為が日本語の情報を増やすことにつながるので、正の連鎖がつながっていきます。  
また、Julia自体が変化の速い言語なので、過去の記事と同じ事をやっても実行できないということがざらにあります。ですので、「最新の入門情報」というのは非常にありがたいわけです。

もちろん、ガチ勢は放っておいても英語の情報を取ってくるのですが、日本で裾野を広げるためには日本語の情報が欠かせません。

今年は名古屋方面にもJuliaが広まっているのを実感して、とてもうれしい限りです。

# 3. エヴァンジェリストを確保する

最後のエヴァンジェリストを確保するという話は、結構大変かも知れません。我々の場合、エネルギーもある程度の時間もある優秀な大学院生がJSoCというグラントも取って開発しちゃったり研究に使っているのですが、彼が常に「Julia良いよJulia」「これからはJuliaの時代」と言い続けている[^4] ことで、じわじわと広がっているように見受けられます。 そのおかげで、ウサギィさんやNAISTの松本研にまでJuliaが広がっていると聞き、やはり良いと言い続けることと情報を蓄積し続けることは大事だなと通関しています。

無論、そもそもの言語としてのウリ（NumPy, SciPyでできない行列計算以上のことをやるときに速さが欲しい）がなければこれも無意味ではあります。しかし、いかに良い言語であっても広まらない時は広まらないし、そこまで良いと思っていない言語でもデファクトになるという時はあります。 であれば、自分の好きな言語を広めると幸せになれるんじゃないか、と思います。

後は[ベンチマーク](https://chezo.uno/post/2015-10-21-tinysegmenterwojuliayi-zhi-sitaramitnoxian-sheng-nizhi-dao-sitemoraetahua)など、他言語との比較を行うことができると、より他言語のユーザーに認知が広まるのではないでしょうか。

# まとめ

最後にテクニカルではない話になってしまいましたが、Juliaの事例を通じていろいろな言語が盛り上がっていけばなと思います。

[^1]: この辺僕が死んだら開催されなさそうなkawasaki.rbとは対称的ですね :p

[^2]: コミュニティ運営で重要なのはSPOFを作らないことだと思っているので、esaなりSlackでのchat opsなりは負荷分散のために非常に重要。負荷の集中を舐めてはいけない

[^3]: 途中までだいぶ一人カレンダーの様相を呈していた

[^4]: 壊れたロボットの用に同じ言葉を繰り返す作戦にしか思えない