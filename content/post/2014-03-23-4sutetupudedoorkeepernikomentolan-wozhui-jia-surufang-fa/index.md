---
title: 4ステップでDoorkeeperにコメント欄を追加する方法
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-03-23 22:06:15+00:00
lastmod: 2014-03-23 22:06:15+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [doorkeeper, '383', '382', site, 入力, 情報, add, アカウント, クリック, '22']
recommendations: [/post/2014-01-24-kawasaki-dot-rb-number-008-wokai-cui-simasita-number-kwskrb/,
  /post/2015-12-25-juliadede-raretamainayan-yu-wosheng-rishang-gerufang-fa-number-juliaac/,
  /post/2011-03-04-googlekarendanochang-suo-qing-bao-wogooglematupunibiao-shi-surufang-fa/]
---

![画像](e382b9e382afe383aae383bce383b3e382b7e383a7e38383e38388-2014-03-23-22-22-17.png)

Doorkeeperはコミュニティなどのイベントを行うのに便利ですよね。  
そんなDoorkeeperですが、他のzusaarなどのサイトと比較してコメント欄がデフォルトでついていないので、  
Disqusと連携してコメント欄を追加する方法を書きます。

僕がやった時は日本語で情報が見つからなかったのですが、  
@yumu19ですらはまっていたので、結構挫折している人がいるのかも...、と思いブログに書くことにします。

# 1. Disqusのアカウントをとる

[http://disqus.com/](http://disqus.com/)

アカウントの取り方はメモを取っていないのですが、多分普通にメール認証すれば良いはず...。

# 2. "Add Disqus to Your Site"をクリック

ログインした後のtop右下の"Add Disqus to Your Site"をクリックする

{{< figure src="e382b9e382afe383aae383bce383b3e382b7e383a7e38383e38388-2014-03-23-22-18-30.png" title="" >}}

# 3. 必要な情報を埋めていく

"Site name"はdescriptionなので適当に決めればOK。

"Choose your unique Disqus URL"で入力する情報が、後のDoorkeeperで入力する情報。  
"Category"も適宜入力すればOK

"Finish registration"を押せば、完了。

その後に出てくるscriptの生成画面はdoorkeeperには関係ないので、気にしなくて良い。

[{{< figure src="e382b9e382afe383aae383bce383b3e382b7e383a7e38383e38388-2014-03-23-22-00-36.png)](e382b9e382afe383aae383bce383b3e382b7e383a7e38383e38388-2014-03-23-22-00-36.png" title="" >}}

# 4. Doorkeeperのコミュニティ管理画面の"連携機能"を開く

"Disqus shortname"に、さっき作ったDisqus URLの`.disqus.com`の前の文字列を入れる。  
今回の例だと"kawasakirbtest"を入れて保存する

[{{< figure src="e382b9e382afe383aae383bce383b3e382b7e383a7e38383e38388-2014-03-23-22-04-25.png)](e382b9e382afe383aae383bce383b3e382b7e383a7e38383e38388-2014-03-23-22-04-25.png" title="" >}}


これで、冒頭のようなコメント欄がイベントページの下部にできます！
