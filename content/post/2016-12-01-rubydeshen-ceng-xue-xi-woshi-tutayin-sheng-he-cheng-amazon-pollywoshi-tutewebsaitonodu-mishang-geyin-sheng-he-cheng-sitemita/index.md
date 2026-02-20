---
authors: [aki]
categories: null
date: '2016-12-01 15:10:05-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2016-12-01 15:10:05-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: Rubyで深層学習を使った音声合成Amazon Pollyを使ってWebサイトの読み上げ音声合成してみた
keywords: [音声, amazon, 英語, dl, aws, api, 話題, 追記, '2016', 米国]
recommendations: [/post/2025-12-09-2025-12-09-principal-engineer-in-the-gene-of-ai/,
  /post/2016-12-31-2016nian-wozhen-rifan-tute/, /post/2022-01-09-vancouver-engineer-podcast/]
---

![](20161201230818.png)

今日のre:InventでDeep Learningを使った音声合成サービスのAmazon Pollyが発表されました。 正直、DLを使ったの音声合成が話題になったのなんて今年に入ってからだと思っていたのに、もう商用化したんか！という気持ちでいっぱいです。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://aws.amazon.com/jp/blogs/news/polly-text-to-speech-in-47-voices-and-24-languages/" data-iframely-url="//cdn.iframe.ly/2rv5lYs?card=small"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script></br>

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://aws.amazon.com/jp/polly/" data-iframely-url="//cdn.iframe.ly/mY21nZH?card=small"></a></div></div><script async src="//cdn.iframe.ly/embed.js" charset="utf-8"></script>

**[2016/12/02追記]**

PollyがDLベースという話は [https://aws.amazon.com/jp/polly/](https://aws.amazon.com/jp/polly/) に、"Polly is an Amazon AI service that uses advanced deep learning technologies to synthesize speech that sounds like a human voice. "と書かれていますが、DNNを一部のモジュールとして使っている波形接続型じゃないの？とのことです。なので、「DLを使った」という表現に修正しました。

{{< x user="heiga_zen" id="804202482780008448" >}}

{{< x user="heiga_zen" id="804503598675750913" >}}

なので、[DeepMindのWaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/)のように音声を直接生成しているわけではなさそうです。

**[/追記]**

Amazon Pollyは[Amazon AI](http://www.publickey1.jp/blog/16/amazon_ai3aws_reinvent_2016.html)のサービスとして展開していますが、画像認識(Amazon Rekognition)、音声合成(Amazon Polly)、音声認識と自然言語理解という対話用のコンポーネント(Amazon Lex)が使えるようになりました。 画像認識についてはGoogleのVision APIで話題になりましたが、その他の2つはちょっと変わっていると思いますがこれはおそらくSiriのような対話エージェントである[Amazon Alexa](http://japan.zdnet.com/article/35081512/)のバックエンドを切り売りしているんだと思います。

Pollyが凄いのは、AWS CLIで簡単に音声合成がされるということです。しかも、お値段は月500万字までは無料で、その後も$0.000004/文字と非常に安く、本一冊で$2.4くらいという驚異的な安さです。なので、ちょっと前にrebuild.fmでスクリプト書くだけで音声合成でpodcastできるんじゃないみたいな話題がありましたが、[おもったより速くその現実が来るのかもしれません](https://twitter.com/chezou/status/804132362472681472)。

AWS CLIを使ったbashのサンプルコードはこんな感じです。かんたんでしょ？

```sh
$ aws polly synthesize-speech \
  --output-format mp3 --voice-id Joanna \
  --text "Hello my name is Joanna." \
  joanna.mp3
```

また、サポートしている言語数も2016/12/01現在で、ヨーロッパ言語を中心に以下の24言語をサポートしています。

- アイスランド語
- イタリア語
- ウェールズ語
- オランダ語
- スウェーデン語
- スペイン語 (カスティリヤ)
- スペイン語 (米国)
- デンマーク語
- トルコ語
- ドイツ語
- ノルウェー語
- フランス語
- フランス語 (カナダ)
- ポルトガル語
- ポルトガル語 (ブラジル)
- ポーランド語
- ルーマニア語
- ロシア語
- 日本語
- 英語 (インド)
- 英語 (ウェールズ)
- 英語 (オーストラリア)
- 英語 (米国)
- 英語 (英国)

日本語も聞いていて結構自然に聞こえており、ちょいちょい単語の認識に失敗するときは変なアクセントになりますが、レキシコンで単語を登録すれば自分で改善もできそうです。 サンプル音声はこんな感じです。

[http://chezou.tumblr.com/post/153883804175/amazon](http://chezou.tumblr.com/post/153883804175/amazon)
<script async src="https://assets.tumblr.com/post.js"></script><cite class="hatena-citation"><a href="http://chezou.tumblr.com/post/153883804175/amazon">chezou.tumblr.com</a></cite>

[2016/12/02追記] Google翻訳に手伝ってもらって[英語版をMediumに書きました](https://chezo.uno/blog/2016-12-01_text-to-speech-based-on-deep-learning-for-web-site-using-amazon-polly-and-ruby-adc1923212cb/)。それの生成した音声も貼っておきます。

<iframe width="100%" height="400" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?visual=true&amp;url=https%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F295800373&amp;show_artwork=true"></iframe><cite class="hatena-citation"><a href="https://soundcloud.com/chezou/amazon-polly-tts-demo-from-medium-article">soundcloud.com</a></cite>

[/追記]

で、Mediumなんかの記事の中に面白い記事をよく見るのですが、英文だとなかなか途中で挫折するので、音声にすれば聞くんじゃないかと思い、記事を音声に変換するコードをRubyで書いてみました。 以下にコードがあります。

<script src="https://gist.github.com/chezou/9919f5065cbc52f8d0349d3084ac3616.js"> </script><cite class="hatena-citation"><a href="https://gist.github.com/chezou/9919f5065cbc52f8d0349d3084ac3616">gist.github.com</a></cite>

ポイントとしては、幾つか重要な制約があります。

- API一回あたりの文字数が1500字[^1]（なので、catでmp3を結合している）
- 長い音声は、5分以降が切り捨てられる

詳細は以下を参考にしてください。<iframe src="//hatenablog-parts.com/embed?url=http%3A%2F%2Fdocs.aws.amazon.com%2Fpolly%2Flatest%2Fdg%2Flimits.html" title="Limits in Amazon Polly - Amazon Polly" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="http://docs.aws.amazon.com/polly/latest/dg/limits.html">docs.aws.amazon.com</a></cite>

実際には、ちょうどHckr newsで見つけた以下の記事の音声を聞いてみました。意外と聞けます。

[How the Circle Line rogue train was caught with data](https://blog.data.gov.sg/how-we-caught-the-circle-line-rogue-train-with-data-79405c86ab6a#.pm0eotghk)

もうちょっと頑張ってRSSを取得すれば、特定のサイトの最新の記事の音声を生成して、Dropboxに保存した音声をモバイルから再生するということもできそうですね。

正直、安くて多言語でそれなりに自然で何よりAPIが使いやすいということで、既存の日本の音声合成を頑張ってきた企業は大変だなぁという気持ちになりますが、いろいろな使い方ができそうで楽しみです。

[^1]: 厳密には、"1500 billed characters (3000 total characters)"と書いてあるけど"billed characters"がわからない