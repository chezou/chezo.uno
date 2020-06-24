---
title: "機械学習の分類の話を損失関数と決定境界を中心に整理してみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2016-05-09T00:06:39+00:00
lastmod: 2016-05-09T00:06:39+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
機械学習の分類の話を、主に決定境界と損失関数の観点から整理してみました。 とはいっても、k-NNとか損失関数関係ないのもいます。

最初ははてなブログに書こうとしたのですが、数式を埋め込むのが辛かったのでjupyter notebookにしました。

<iframe src="//hatenablog-parts.com/embed?url=https%3A%2F%2Fgithub.com%2Fchezou%2Fnotebooks%2Fblob%2Fmaster%2Fclassification.ipynb" title="chezou/notebooks" class="embed-card embed-webcard" scrolling="no" frameborder="0" style="display: block; width: 100%; height: 155px; max-width: 500px; margin: 10px 0px;"></iframe><cite class="hatena-citation"><a href="https://github.com/chezou/notebooks/blob/master/classification.ipynb">github.com</a></cite>

[追記]

githubだと日本語を含む数式のレンダーが壊れるので、nbviewerの方がいいかもしれません。[https://nbviewer.jupyter.org/github/chezou/notebooks/blob/master/classification.ipynb](https://nbviewer.jupyter.org/github/chezou/notebooks/blob/master/classification.ipynb)

[/追記]

パーセプトロンが見直されたのはなんでだっけ、SVMってどういう位置づけだっけ、というのを確認できればなぁと思っています。 多層パーセプトロンまでに至るところの流れがうまく伝わればなぁと思っています。 間違いなどがあれば、是非ご指摘いただければ嬉しいです。

本当はcourseraのMachine Learningのコース前の人に届けば嬉しいんですが、きっと修了した人にしか伝わらないかなぁ。 もし、まだNgのコース終わっていない人がいたら、感想聞いてみたいです。


