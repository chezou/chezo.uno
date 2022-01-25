---
title: Jupyter Notebook/LabsをMLのどのフェーズで使うのか？
date: 2020-02-10 06:34:01.727000+00:00
summary: ''
draft: false
featured: {placement: 1, caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/5fNmWej4tAA)',
  focal_point: Center, filename: featured.jpg}
keywords: [プロダクション, ml, 用途, 結果, jupyter, 全部, アンケート, 愛用, プロトタイプ, ops]
recommendations: [/post/2018-10-25_risecamp------ee65c2ef0c9e/, /post/2018-10-19_treasure-data-------plazma-tech-talk-------3c901d92e973/,
  /post/2016-10-29_homebrew-----iruby---------------6a02e5194ff2/]
---


機械学習ではよく使われるJupyter Notebookですが、これを使ってプロダクションで動くコードを書くのは非常に難しいなと思い、皆どのように使っているのかを知りたくてアンケートをとってみました。

{{< tweet user="chezou" id="1226303290129797121" >}}

結果としては、多少拮抗しているのですが、EDAから予測までJupyter派が多かったようです。ついで、学習のプロトタイプまで、EDAだけ派と続いています。

この質問で失敗したなと思ったのは、「MLの開発」と書いたものの、研究・実験用途で使っている人とプロダクションまで持っていく用途で使っている人が混ざってしまったであろうという気がしています。
ただ、1000票以上集まったので面白い結果となったのではないでしょうか。

その他の回答としては、Emacs派や全部.py派、全部C++派などがいることがわかりました。

{{< tweet user="h_okumura" id="1226499591496818693" >}}

{{< tweet user="yellowshippo" id="1226409670442651648" >}}

{{< tweet user="yellowshippo" id="1226416584450658304" >}}

{{< tweet user="TJO_datasci" id="1226460366911131648" >}}

この結果が一概にML Ops的なプロダクション運用のことを考えた最適とは言えませんが、少なくとも現状でMLを取り組む人はかなりJupyterを愛用していることが伺えます。
