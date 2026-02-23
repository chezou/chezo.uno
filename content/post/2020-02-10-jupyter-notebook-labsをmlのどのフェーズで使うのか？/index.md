---
aliases: [/post/jupyter-notebook-labsをmlのどのフェーズで使うのか？, /post/jupyter-notebook-labsをmlのとのフェースて使うのか？,
  /post/2020-02-10-jupyter-notebook-labsをmlのどのフェーズで使うのか？]
date: '2020-02-09 22:34:01-08:00'
draft: false
featured: {caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/5fNmWej4tAA)',
  filename: featured.jpg, focal_point: Center, placement: 1}
summary: ''
title: Jupyter Notebook/LabsをMLのどのフェーズで使うのか？
keywords: [プロダクション, eda, ml, 用途, 結果, jupyter, 全部, 一概, アンケート, 愛用]
recommendations: [/post/2017-09-09_pyconjp-2017------5fa5f59b9bde/, /post/2018-05-17_mlse-kickoff/,
  /post/2014-06-21-julia100ben-notuku/]
---

機械学習ではよく使われるJupyter Notebookですが、これを使ってプロダクションで動くコードを書くのは非常に難しいなと思い、皆どのように使っているのかを知りたくてアンケートをとってみました。

{{< x user="chezou" id="1226303290129797121" >}}

結果としては、多少拮抗しているのですが、EDAから予測までJupyter派が多かったようです。ついで、学習のプロトタイプまで、EDAだけ派と続いています。

この質問で失敗したなと思ったのは、「MLの開発」と書いたものの、研究・実験用途で使っている人とプロダクションまで持っていく用途で使っている人が混ざってしまったであろうという気がしています。
ただ、1000票以上集まったので面白い結果となったのではないでしょうか。

その他の回答としては、Emacs派や全部.py派、全部C++派などがいることがわかりました。

{{< x user="h_okumura" id="1226499591496818693" >}}

{{< x user="yellowshippo" id="1226409670442651648" >}}

{{< x user="yellowshippo" id="1226416584450658304" >}}

{{< x user="TJO_datasci" id="1226460366911131648" >}}

この結果が一概にML Ops的なプロダクション運用のことを考えた最適とは言えませんが、少なくとも現状でMLを取り組む人はかなりJupyterを愛用していることが伺えます。