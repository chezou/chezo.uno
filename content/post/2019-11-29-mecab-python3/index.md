---
authors: [aki]
summary: mecab-python3を捨ててnatto-pyにしよう
tags: [NLP]
date: November 29, 2019 2:58 PM
lastmod: August 9, 2020 1:40 AM
keywords: ['83', mecab, natto, '81', windows, py, ipadic, spacy, wheel, ginza]
recommendations: [/post/2018-12-01_windows-64bit-mecab--kytea-------2018-b283b6c7b33c/,
  /post/2019-11-17-spacy-ginza/, /post/2010-10-13-mecabworuby-1-dot-9-2-on-windows7-64bitban-deshi-ufang-fa/]
---

![](https://images.unsplash.com/photo-1516675457768-db513e191dcc?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

# tl;dr

- ~~mecab-python3は使い勝手が悪いのでやめよう~~ 後述するPaulがメンテナになってWindowsも含めたwheelが提供されたので今はだいぶマシです
    - IPAdicを使う場合にpip installで辞書を入れる必要があるのは注意（なんでwheelに辞書混入してたんや)
- 代わりは[natto-py](https://github.com/buruzaemon/natto-py/wiki/%E3%81%A8%E3%82%8A%E3%81%82%E3%81%88%E3%81%9A%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86%EF%BC%81)がおすすめ
    - fugashiも選択肢としてあります（が、デフォルトUnidic推しなのでIPAdic使いたい人は説明読んでね）

# mecab-python3を止める理由

メンテナが変わってDebianのパッケージを書いている人になったため、ユーザ寄りというよりは開発側の理屈が強く優先されるようになった。良くも悪くもUNIX的な思想？（一つ一つのやれる事は小さくというパイプ的なアレ）なんだが、これがすこぶるwheelのfat binary packageの方向性と相性が悪いと思う。具体的には

- Source build時にswig必須に
- WheelもIPAdicのみサポートでLinuxとmacOS向けのみ

つまり、Neologdがデファクトとなった現代では使いづらさしかないのでやめたほうがいい。機械学習の教科書的な本では必ずmecab-python3が出てくるが、あれは古い話と思ったほうがいい。

MacとLinuxのユーザは迷わずnatto-pyを使いましょう。nattoシリーズはFFIベースでmecabを使うので、余計なバインディングのビルドは必要ありません。また、作者にお話を聞いたところ、Windows環境で動かすことを一つのモチベーションにしているとのことなので、割とWindowsユーザにも良いかと思います。

Windowsユーザは以下の記事を読んで、libmecab.dllを手に入れてnatto-pyを使いましょう。

[Windows 64bitでMeCab(とKyTea)を使う方法 2018](https://link.medium.com/HdqI8Xer11)

余談だが、最近spaCyがfugashiというMeCabのCython wrapperに依存するように変わったが、これは今のところUniDic専用だ。この背景はmecab-python3がほぼIPAdic専用になったからだろう。なお、韓国語はnatto-pyを使っている。

natto-pyは作者に聞いたところ、もうmecabがメンテナンスされていないのでnatto自身もあまり大きな変更はしないだろうとのこと。

natto-pyの簡単な使い方はこれを見るといいと思う

[backspace_stats_2.ipynb](https://gist.github.com/chezou/fff39a2575946cf248d6ab54e60e9c58)

# mecab以外の方向性

sudachiPyとGiNZA, spaCy の組み合わせに期待している。これは、マストドンのトレンドワードの記事を読んでもらえれば使い方はわかるだろう。

[spaCyとGiNZAでマストドンのトレンドワード抽出をしてみた](spaCy%E3%81%A8GiNZA%E3%81%A7%E3%83%9E%E3%82%B9%E3%83%88%E3%83%89%E3%83%B3%E3%81%AE%E3%83%88%E3%83%AC%E3%83%B3%E3%83%89%E3%83%AF%E3%83%BC%E3%83%89%E6%8A%BD%E5%87%BA%E3%82%92%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F%20f0f13bcd4a9a4682b698ac4630eaa1a3.md)

ただ、sudachiPyはmecabと比較すると速度的に遅いことと、sym linkを使っている関係でまだWindowsでは動かないというネックがある。Windowsで動かすの自体は対応してもらえそうな雰囲気を感じているので、手伝っていきたい。

[SudachiPy doesn't work with Windows with "OSError: symbolic link privilege not held" · Issue #107 · WorksApplications/SudachiPy](https://github.com/WorksApplications/SudachiPy/issues/107)

SentencePieceはNN向けの前処理にはいいと思うけど、語彙数を決めて分割しにいく性格から、トレンドワードをとりにいく的なのには向かないんだろうなと思っている（教えて詳しい人）。

---

mecab-python3はオリジナルのクリエーターが、もう使ってないんじゃないかなー。彼の最初に作ったモチベーションは簡便なパッケージを用意すると言うところだと思うのにどうしてこうなった。

[20191217追記]

[https://twitter.com/polm23/status/1206809665692000256](https://twitter.com/polm23/status/1206809665692000256)

[/追記]

[20191225追記]

どうやら、fugashiの作者のpolmさんが新オーナーになる方向で進んでるらしい。新しいrepoは下記になる予定。

[https://github.com/polm/mecab-python3](https://github.com/polm/mecab-python3)

[Memory leak: delete PyObjects when those are not needed anymore by akorobko · Pull Request #37 · SamuraiT/mecab-python3](https://github.com/SamuraiT/mecab-python3/pull/37#issuecomment-568516091)

[/追記]

---

[Back to home](https://memo.chezo.uno)
