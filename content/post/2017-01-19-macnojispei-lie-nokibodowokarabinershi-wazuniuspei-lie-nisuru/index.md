---
authors: [aki]
categories: null
date: '2017-01-19 14:17:07-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2017-01-19 14:17:07-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: macのJIS配列のキーボードをKarabiner使わずにUS配列にする
keywords: [配列, キーボード, cmd, 英数, 単体, jis, international, keyboard, ime, anker]
recommendations: [/post/2008-06-01-nantoiunu-li-noren/, /post/2012-10-31-amazonno1gb-slash-1yuan-sutoreziglacierwokomandoraindeshi-uglacier-cmdnoshi-ifang/,
  /post/2016-12-30-2016nian-mai-tuteyokatutamono-10xuan/]
---

macOS Sierraに上げる前に、Karabinerが動かない問題をなんとかしたいと思っていました。 El capitanでちゃんと検証してから上げないと、色んな人みたいに死ぬなと思って[Karabiner-Elements](https://github.com/tekezo/Karabiner-Elements)に移行できるか検証しました。

## 今回の要件

1. JIS配列の本体のキーボードをUS配列で使いたい
2. 外付けのUS配列のキーボードで右cmd単体でかな（IME ON）、左cmd単体で英数（IME OFF）として使いたい

とくに、1.についての情報がみつからなかったので、実際に試してみた。

## Karabiner-ElementsでUS配列にする

最近のKarabiner-ElementsはGUIがついているので、かなり楽ちんで、設定項目は2つ。

1つ目は"Virtual Keyboard"のKeyboard Type: ANSIを設定すること。これで大体USキーボードの配列になります。

![](20170119221149.png)

2つ目の設定は、"Simple Modifications"で`international3`を`grave_accent_and_tilde`に変えれば行けた。これでかつる！KarabinerのJIS-\>USと揃えるには`international1`も同様に割り当てれば良さそう。

![](20170119221202.png)

ちなみに、検証はAnkerのBTキーボードで試しました。安いUSキーボードとしてはそこそこ使えます。

{{< amazon asin="B00U260UR0" title="Anker ウルトラスリム Bluetooth ワイヤレスキーボード iOS/Android/Mac/Windows に対応 ホワイト" >}}


- 出版社/メーカー: Anker
- メディア: エレクトロニクス
- [この商品を含むブログを見る](http://d.hatena.ne.jp/asin/B00U260UR0/chezou-22)

## cmd-\>英数,かな

これは、[英かな](https://ei-kana.appspot.com/)使えば大丈夫。

しばらくこれで試してみようと思います。問題なければSierraにあげてみます。