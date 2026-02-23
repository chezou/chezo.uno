---
authors: [aki]
categories: null
date: '2010-02-21 13:58:11-08:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2010-02-21 13:58:11-08:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: アカペラのイベント情報とかをつぶやく@acappella_eventの使い方
keywords: [event, acappella, 合唱, アカペラ, リツイート, 情報, bot, カレンダー, 予定, 検索]
recommendations: [/post/2010-01-19-he-chang-toakaperanokarendawogoogle-calendardezuo-tutemita/,
  /post/2010-12-17-wu-liao-deiphonenobiao-zhun-karendaniakapera-slash-he-chang-karendawobiao-shi-surufang-fa/,
  /post/2011-03-03-dropboxgahtmlgong-kai-wojian-dan-nisuru-at-acappella-eventguan-lian-matomesaitozuo-cheng-sitemita/]
---

[以前の記事](https://chezo.uno/post/2010-01-19-he-chang-toakaperanokarendawogoogle-calendardezuo-tutemita/)でも少し書いていたんですが、twitterで[@acappella\_event](http://twitter.com/acappella_event)というbotを作りました。前から少しずつ色々試していたのですが、ようやく基本的なところができたので使い方を簡単にまとめたものを残しておきます。

> @[acappella\_event](http://twitter.com/acappella_event)は  
> 1)合唱/アカペラについて検索して投稿  
> 2)@を飛ばされるとそれをリツイート  
> 3) [http://bit.ly/caTSPZ](http://bit.ly/caTSPZ) のアカペラ/合唱カレンダーから当日のイベント情報を投稿(する予定)  
> の3つをするbotです。

[http://twitter.com/chezou/status/9383246402](http://twitter.com/chezou/status/9383246402) より抜粋。

もう少し詳しく説明すると、

1)は、twitter検索した情報をつぶやきます。「アカペラ or 合唱」と「情報 or 告知 or 開催 or 募」あたりのクエリを使ってます。なので、変な情報も拾ってきますし、漏れもありますがこの辺はまぁ今くらいでいいかなと思っています。  
(20100829追記：公式リツイートで検索した情報をつぶやくように修正しました 参考：[Perlでキーワード検索＆公式リツイートを行うbot](http://firegoby.theta.ne.jp/archives/1141) firegoby)  
2)は、「@acappella\_event ○○」とつぶやくと、その発言自体を公式RTします。まだまだfollowerが少ないのですが、広めたい情報や告知したい情報は@で飛ばしていただければ5分程度でRTされるはずです。なお、つぶやきの頭に@acappella\_eventと書かないとRTされないのでご注意ください。  
3)は、試験運転状態なので上手くいっているか少し不安ですが、細々と更新しています[アカペラ/合唱カレンダー](http://bit.ly/caTSPZ)から以下の3種の情報をつぶやきます(願望)。

1. 当日の予定を朝6時につぶやきます。
2. 翌日の予定も午後11時くらいにつぶやきます。
3. 新規登録されたイベントもつぶやきます。
今のところ3.の新規イベントは安定しているのですが、1,2が様子見な形で怪しいですTwitterの調子がよければ動いています(20100711追記)。

以上が@acappella\_eventの機能です。どちらかというと、他力本願なbotなので色々な人に活用していただければ盛り上がって嬉しいなぁと思っています。特に、[アカペラ/合唱カレンダー](http://bit.ly/caTSPZ)の編集に協力してくださる方大募集中です。ダイレクトメッセージなどでgmailのアドレスをお教えいただければ、登録いたします。[twicco](http://twicco.jp/)ではなんか面倒くさそうな感じがしたので、GAEの練習がてらbotを作ってみた感じです。そんなにたいしたことはしていないのですが、備忘録がてらそのうち参考にしたサイトなどをまとめたいと思います。