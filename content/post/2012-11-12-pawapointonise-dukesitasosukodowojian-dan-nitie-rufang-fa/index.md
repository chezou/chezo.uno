---
title: "パワーポイントに色づけしたソースコードを簡単に貼る方法"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2012-11-12T09:11:33+00:00
lastmod: 2012-11-12T09:11:33+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
パワーポイントに色づけしたコードを貼るのって、皆どうやってるのか不思議に思っていたのですが、どれもちょっと面倒だなという感じでした。

- GNU Source-highlightを使う方法：[覚え書き：色づけしたソースコードをPowerPointなどに貼り付ける方法 - C++Builder好きの秘密基地](http://d.hatena.ne.jp/A7M/20090205/1233842500)
- SCiTEを使う方法：[Syntax highlighting source code in Word and PowerPoint with | fauskes.net](http://www.fauskes.net/nb/syntaxms/)
- Visual Studioを使う方法など:[How to: C# source with syntax highlighting on PowerPoint slides - Stack Overflow](http://stackoverflow.com/questions/825353/how-to-c-sharp-source-with-syntax-highlighting-on-powerpoint-slides)
色々ある中で、その本質が「HTML等の形式でクリップボードに保持して、パワーポイントに貼り付ける」、ということに気づいたので、試しにGithubにGistで書いてみたら見事成功しました。

手順は至って簡単、

1. **色づけしたいコードを[Gist](https://gist.github.com/)で作成(ものによってはPrivateにしておく）**
2. **Gistからコピーして、パワーポイントで「形式を選択して貼り付け」で「HTML形式」で貼る**
2．は最近のPPTだと、貼った後に横に出現するアイコンから、「元の書式を保持する」を選ぶともっと楽かもしれません。

これは便利だ！


