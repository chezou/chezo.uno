---
title: "TinySegmenterをJulia移植したらMITの先生に指導してもらえた話"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-10-21T23:43:17+00:00
lastmod: 2015-10-21T23:43:17+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
先日、工藤さんがJavaScript向けに作った日本語のコンパクトな分かち書きツール、TinySegmenterをJuliaに移植した[TinySegmenter.jl](https://github.com/chezou/TinySegmenter.jl)を作りました。 もともとは、PyconJPで[janomeの話](http://mocobeta-backup.tumblr.com/post/131025586072/pyconjp-janome)を聞いたら居ても立っても居られなくなって、簡単なTinySegmenterを移植したんですが、そしたら思いもよらぬ展開が待っていました。

[2015/10/22 23:38 追記] 計測の問題を [@repeatedly](https://twitter.com/repeatedly) さんから指摘いただいたので再計測しました。

## パッケージ登録時にMITの先生からツッコミが入る

Juliaのパッケージは[METADATA.jl](https://github.com/JuliaLang/METADATA.jl)というセントラルなレポジトリで管理されています。 ここに登録されたパッケージは`Pkg.add(&quot;TinySegmenter&quot;)`とREPLで実行するだけでパッケージが導入できます。\*1

ここに登録をしようとした時に、「日本語の分かち書きツールなのに、パッケージ名が一般的すぎるのでは」という[指摘](https://github.com/JuliaLang/METADATA.jl/pull/3718#issuecomment-147277044)をMITの[@stevengj](https://github.com/stevengj/)先生(以下、SGJ先生)からいただきます。Juliaのパッケージの命名規則は[ドキュメント](http://docs.julialang.org/en/latest/manual/packages/#guidelines-for-naming-a-package)にもあるのですが、portingの時はそのまま名前を付けても良さそうなので反論をして、翌日マージされました。

## パッケージ登録後、1週間ほぼ毎日issueが立つ

僕の初期実装はmhagiwaraさんの[Python実装](https://github.com/mhagiwara/nltk/blob/master/jpbook/tinysegmenter.py)を参考に、割とベタに実装をしていました。

ですが、LLっぽい書き方で書いていたため、多くのツッコミどころがあったので、最適化したらどう？的なissueがぼっこぼこ立ちました。 プライベートのコードでこんなにissueもらったのは初めてだったのですごい嬉しい反面、一番多い時で夜寝る前に一個こなしては朝起きると次のissueが立ち、出社前に一つ片付けたら昼にもう一個増えるみたいな、時差をフル活用したハードな指導が始まりました。

最適化としては主に以下のような最適化をしました。

- const使おう
- RegexやめてCharに展開しよう
- DictのkeyはCharのTuple使おう
- Stringはコピーが発生するのでStringBuf使おう

## 日本語が読めないSGJ先生、オリジナル実装のバグを見つける

面白かったのは、途中で日本語が全くわからないSGJ先生\*2がオリジナルの実装にバグを見つけたところ。半角カタカナの&quot;ｸﾞ&quot;がUnicodeでは二文字になるはずなのに、それを考慮した実装になってないからスコアが反映されてない、という点。工藤さんにも確認しましたが、ご本人も昔のことなので詳細は覚えていないが今の実装は間違っていそうだという事を確認しました。 気づいた原因は、DictのkeyをCharのTupleで表現する関係で、文字数応じた型宣言をしていたからなんです。\*3

実際には、日本語の中で半角カタカナはほとんど出てこないのでそこまで影響は出ませんが、ASCII圏の力を思い知らされました。なお、ここの議論で日本語知らない人に英語で半角カタカナ全角カタカナの議論をする必要があり、泣きそうでした。 この頃にはPRも来ていたのですが、[半角カタカナの&quot;ｸﾞ&quot;は二文字だから&quot;ｸ&quot;じゃねーの？](https://github.com/chezou/TinySegmenter.jl/pull/6#issuecomment-148142520)とか来ていたのも、今となっては良い思い出です。

## SGJ先生の狙いは

「なんでこの人はこんなマニアックな日本語の分かち書きプログラムに、熱心にissue立てるんだ？」と謎に思いながら、毎日の宿題のようにこなしていたのですが、最後の課題 issueを見て納得します。

そう、ベンチマークだったのです。

おそらく、最初のパッケージ名反論の時に、「TinySegmenterは多数の言語で実装されており日本人には一般的な名前だ」と主張した時に調査し、気づいたのだと思います。

というわけで、Python実装のバグを見つけて直したり、Python3対応したり、Node.jsのファイルの読み込み方調べたりしながら、ベンチマークとりました。

その結果がこちら。(詳細は[issueを見て下さい](https://github.com/chezou/TinySegmenter.jl/issues/8#issuecomment-149621354))

**[2015/10/22 23:38 追記]**

@repeatedly 先生が色々指摘をしてくれて、Pythonのループ回数が10分の1だったり、Juliaのコードが足りなかったり、Rubyの実装も高速化していただいたので計測しなおしました。 なお、D言語でのベンチはこれからです。

[TinySegmenterのベンチマーク + D言語版 - Go ahead!](http://repeatedly.github.io/ja/2015/10/tinysegmenter-benchmark-and-d/)

| JavaScript | Python2 | Python3 | Julia | Ruby |
| --- | --- | --- | --- | --- |
| 9.62 | 93.08 | 23.94 | 1.46 | 19.44 |

![](/img/2015/10/21/234317/20151022234902.png)

**[追記ここまで]**

| JavaScript | Python2 | Python3 | Julia | Ruby |
| --- | --- | --- | --- | --- |
| 121.04 | 92.85 | 29.64 | 12.36 | (933+) |

メタメタした実装で遅すぎたRubyを外したグラフはこちら。

![](/img/2015/10/21/234317/20151021232829.png)

最適化をしたJuliaは確かに速いです。 そして、意外だったのはPython 3.5.0の速度。Unicode周りの実装が刷新されたという話は聞いていましたが、Juliaの二倍程度に肉薄してくるとは。条件にもよるかもしれないけど、文字列処理するNLPerは3系に今すぐ移行したほうが良いのでは？と思いました。

最後に、SGJ先生はjulia-usersのMLに成果を[投稿していただきました](https://groups.google.com/forum/#!topic/julia-users/afA_ZfoOUdU)。 なんか、一人JSoCって感じですね。

## まとめ

- Juliaでパッケージを作ると、MITの先生が指導してくれる
- Julia速いけどCharacter辛い
- Pythonは3.5.0に今すぐ移行しないと！

というわけで、今後はC++やgoと比較するために[TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker/)のJulia template作って比較したいね、と話しています。[TinySummarizer](https://github.com/hitoshin/tiny_summarizer)にもtryしたいなぁ。

12/19(土)に Julia Tokyoの[第5回ミートアップ](http://juliatokyo.connpass.com/event/21715/)が開催されます！ いつもJuliaはじめて24時間枠の発表もあるので、お気軽に参加・発表しに来て下さい！

\*1:METADATAに登録しないで、githubからcloneすることもできます

\*2:なお、ご専門は最適化の様子でNLP関係ない

\*3:この頃には、2015年にもなって日本人がChar型のある言語を触るのしんどい心折れそうでした


