---
title: PyConJP 2017に参加した
description: 2年ぶりにPyConJPに参加しました。2日間参加してきたので、メモがてら書いていきます。
date: '2017-09-09T12:24:23+09:00'
categories: [conference]
keywords: [python, データ, 発表, jupyter, 更新, pandas, 入門, and, 編成, janome]
authors: [aki]
recommendations: [/post/2014-01-18-ke-xue-ji-suan-niokerujun-zhi-hua-aruihanazepythongazhao-shi-nita-yan-yu-nosieawoduo-tuteiruka/,
  /post/2015-10-12-pyconjp-2015nican-jia-sita-number-pyconjp/, /post/2018-10-25_RISECamp------ee65c2ef0c9e/]
---

2年ぶりにPyConJPに参加しました。2日間参加してきたので、メモがてら書いていきます。

### 興味深かった話

pandasとdaskのコミッターの[shinhrks](https://twitter.com/sinhrks)さんの基調講演。pandasに対してどうコントリビュートしているかという話を中心に、OSS活動をしていこうと思わせる（1日目とは打って変わって）良い基調講演でした。

特に印象的だったのが、pandasの中ではAirspeed Velocityを使ってCIでベンチマークを取りコミット間の処理速度が低下していないかを検出しているという点です。Pythonのパッケージなので、他の言語では難しいかもしれないということです。ともすると速度のデグレは気づきにくいことも多いですが、OSSでそこまできっちり見ているのは素晴らしいと思いました。

[**spacetelescope/asv**  
_asv — Airspeed Velocity: A simple Python benchmarking tool with web-based reporting_github.com](https://github.com/spacetelescope/asv "https://github.com/spacetelescope/asv")[](https://github.com/spacetelescope/asv)

なお、pandasやビジュアライズに入門するには昨日でたJupyter本が良いです。

[**PythonユーザのためのJupyter\[実践\]入門**  
_Amazonで池内 孝啓, 片柳 薫子, 岩尾 エマ はるか, @drillerのPythonユーザのためのJupyter\[実践\]入門。アマゾンならポイント還元本が多数。池内 孝啓, 片柳 薫子, 岩尾 エマ はるか,…_amzn.to](https://amzn.to/2wODd2J "https://amzn.to/2wODd2J")[](https://amzn.to/2wODd2J)

リクルートテクノロジーズの[yuzutas0](https://twitter.com/yuzutas0)さんによる分析基盤とカルチャーを作っていく話。どの話も、あーあーあるあるという感じで会場も共感の嵐でした。結局、現場のユーザが使うためには、独りよがりな基盤を作っても使われなければ無いから、コミュニケーションを取っていって必要なものを作っていこう、という泥臭さしかない話でした。こうしてデータドリブンで仮説を作っていく話はとても良いと思います。

Cookpadの[ayemos\_y](https://twitter.com/ayemos_y)さんの発表。自分が課題感感じているところかなと思ったら少し違った話でした。通常、ソースコードはgitなどでバージョン管理をするのに対して、モデルは比較的バージョン管理をしやすいけど、入力データのスナップショットをとることが難しいので、repeatabilityを確保するのは難しいよなと思っていたのですがその問題提起の話でした。

モバイルやセンサーからくるデータは遅延して到達したり、後で更新したりするみたいな時があったときや、データの欠損があったりしたときに、そのまましれっとモデルの更新をすると、データが原因なのかモデルがダメなのか何がダメなのかがぱっと切り分けられなくて、モデルの更新をしにくくなるという状況なのは辛いなという認識です。例えるならば、バージョン管理もテストもない状態でコード変更をして神に祈ってデプロイするイメージに近いです。（ゴールデンスタンダード使ったりなにか悪くなってることは検出できますが…）

解決方法はまだまだ発展途上だなというか、PySparkでETLしてS3上にHive形式のテーブル作ってそれをImpalaでもPrestoでも叩けばええやんという気持ちでいっぱいだったのですが、問題自体は重要な話であり、Googleなんかはどうにかしてクリアしているポイントのようなので、僕自身もなんとかしたいと思っている場所だったりします。良い解決方法考えていきたいところです。

[**プレゼンテーション：Why you should do text analysis with Python (even if you don't want to) | PyCon JP 2017…**  
_The explosion in Artificial Intelligence and Machine Learning is unprecedented now - and text analysis is likely the…_pycon.jp](https://pycon.jp/2017/ja/schedule/presentation/5/ "https://pycon.jp/2017/ja/schedule/presentation/5/")[](https://pycon.jp/2017/ja/schedule/presentation/5/)

もう一件、テキスト処理をPythonでやる話がありました。話の殆どは知ってる話だったのですが、spaCyが日本語対応したらしいよという話を聞いて、実はjanomeがTokenizerに使われているのをしりました。

[**explosion/spaCy**  
_spaCy - 💫 Industrial-strength Natural Language Processing (NLP) with Python and Cython_github.com](https://github.com/explosion/spaCy "https://github.com/explosion/spaCy")[](https://github.com/explosion/spaCy)

なお、RからもspacyRというwrapperを使えるようでopenNLPとrJavaに疲弊している人は使うと良いようです。

[**kbenoit/spacyr**  
_spacyr - R wrapper to spaCy NLP_github.com](https://github.com/kbenoit/spacyr "https://github.com/kbenoit/spacyr")[](https://github.com/kbenoit/spacyr)

### 感想

PyConはあまり知り合いも少なく、アウェイ感があるのですが、なんか地味に知り合いが増えてきたこともあり色々と話しをできてよかったなと思います。

実は一番印象に残ったのは、shimizukawaさんやtakuan\_oshoさんなどインターネッツの中でしか見たことがない方とお会い出来たりお話できたことでした。また、色々とお話をしていると「ああ、aodagさんの文章を翻訳した人ですね」と言われて、地道な活動をしてきてよかったなと思います（虎の威を借る何とやらとも言う）

また、英語セッションで質問をしたら、何故か英語圏の人に囲まれて日本語のテキスト処理とコーパスが辛いんだけど、とか言う話を議論できたのは良かったです。

一方で発表は、今回初日のキーノートがただの会社の紹介に終止したマーケティングで終わったり、海外勢のデータ系がやってみた系が多かったりと結構辛かった一方で、日本人の発表者は非常に濃い良い発表が多く良かったなぁと思いました。特にcondaとwheelのfragmentationについてはなんとかならんかなと思って質問しましたが、お茶を濁されたのが悲しかったです。

ただ、自腹で1万円払って来年も行くかというとプログラム編成がデータ系が横に並んで厳しかったり、発表のクオリティの分散が激しかったりと悩ましいなぁというところです。自分はデータ系しかほぼ見てないのですが、2年前に参加したときはjanomeの話とか濃い話がありそう思わなかったのですが、RubyKaigiの方が講演のクオリティの平均が高い（ハズレを引きにくい）のかなと思いました。aodagさんのパッケージングの話とか（資料しか見てないけど）昔からの人の発表は安定感あったのですが…。

とはいえ、プログラム編成も投稿が山のようにきたりしている現状、SciPyあるいはScientific Programming, Data Analysis & MLみたいな言語を絞らないカンファレンスを日本でやって、それでガス抜きをしないとPyConには荷が重いだろうなぁと思います。イメージ的には、[Polycon](http://polycon.io/)みたいな言語非依存なカンファレンスの科学計算版で、industrial trackとbeginner trackとresearch trackの3本立てでちょっと学会よりはゆるい感じの集まりかなぁ。

いずれにせよ、Pythonは今後もお世話になっていくので、PyCon JPの運営の皆さんに感謝しつつ燃え尽きないよう継続してって頂きたいなぁと思います。