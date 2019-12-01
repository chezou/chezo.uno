---
title: "Googleフォームで作った申請フォームからSlackに通知をする方法"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2015-03-04T00:31:31+00:00
lastmod: 2015-03-04T00:31:31+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
Slackは連絡先を知っている人が参加することが多いですが、ゲームのコミュニティ等相手の連絡先がわからない場合もあると思います。(IngressとかIngressとかIngressとか)

そういう時のために申請フォームを作って、Slackに通知をするための方法をまとめます。

## 1. SlackのIncoming Webhookを設定する

Slackの[Incoming Webhook](https://my.slack.com/services/new/incoming-webhook)を新規作成する。 デフォルトの部屋は適当に選べば良い。

`Webhook URL`のURLを記録しておく。

## 2. Googleフォームを作る

今回想定している項目は、以下の4点

- 紹介者名
- 名前
- あなたのG+プロフィールページ
- メールアドレス

## 3. Slack通知用のスクリプトを作成する

フォームの`ツール -&gt; スクリプト エディタ`を開く

![f:id:chezou:20150304002603p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150304/20150304002603.png &quot;f:id:chezou:20150304002603p:plain&quot;)

通知するためのコードを書く。 以下の例では、public channel(`#public_notify`)にメールアドレス以外の情報を、private group(`private`)にすべての情報を通知しています。

urlのところには先ほど取得した`Webhook URL`を設定します。

    function sendToSlack(body, channel) { var url = &quot;https://hooks.slack.com/services/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&quot;; var data = { &quot;channel&quot; : channel, &quot;username&quot; : &quot;invitation bot&quot;, &quot;text&quot; : body, &quot;icon\_emoji&quot; : &quot;:gohst:&quot; }; var payload = JSON.stringify(data); var options = { &quot;method&quot; : &quot;POST&quot;, &quot;contentType&quot; : &quot;application/json&quot;, &quot;payload&quot; : payload }; var response = UrlFetchApp.fetch(url, options); } function test() { sendToSlack(&quot;It&#39;s a test message&quot;, &quot;#public\_notify&quot;) } function onFormSubmit(e){ var body = &quot;公開版申請が来たよ\n&quot;; var introducer = &quot;&quot;; var applicant = &quot;&quot;; var plusUrl = &quot;&quot;; var itemResponse = e.response.getItemResponses(); for (var j = 0; j \&lt; itemResponse.length; j++){ var formData = itemResponse[j]; var title = formData.getItem().getTitle(); var response = formData.getResponse(); body += &quot;【&quot; + title + &quot;】\n&quot;; body += response + &quot;\n\n&quot;; switch (title) { case &quot;紹介者名&quot;: introducer = response; break; case &quot;名前&quot;: applicant = response; break; case &quot;あなたのG+プロフィールページ&quot;: plusUrl = response; break; default: break; } } var bodyPublic = &quot;@&quot; + introducer + &quot;さ〜ん\n&quot; + applicant + &quot;さんがお呼びよ！\n&quot;; bodyPublic += &quot;確認したら「&quot; + applicant + &quot;さん確認しました！」と発言してね\n【Google+】&quot; + plusUrl; sendToSlack(bodyPublic, &quot;#public\_notify&quot;); sendToSlack(body, &quot;private&quot;); }

Slackへの通知が動くかどうかは、`test()`を実行してみると良い。

最後に、フォームが送信された時にこのスクリプトが動くように`onFormSubmit()`のトリガーを設定します。

![f:id:chezou:20150304002636p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150304/20150304002636.png &quot;f:id:chezou:20150304002636p:plain&quot;)

![f:id:chezou:20150304002721p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150304/20150304002721.png &quot;f:id:chezou:20150304002721p:plain&quot;)

![f:id:chezou:20150304002736p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150304/20150304002736.png &quot;f:id:chezou:20150304002736p:plain&quot;)

このとき、スクリプトからドキュメントへのアクセス権限を求められるので承認します。(これがないと、設定できない)

なお、デバッグの時は最後の`通知`に`今すぐ`という設定を追加するとエラーが分かりやすくなってよいです。

うまくいけば、こういう通知がでることになります。

![f:id:chezou:20150304002942p:plain](http://cdn-ak.f.st-hatena.com/images/fotolife/c/chezou/20150304/20150304002942.png &quot;f:id:chezou:20150304002942p:plain&quot;)

## 参考URL

- [gas - スプレッドシートで作ったtodoリストでステータスを変更するとslackに流す - Qiita](http://qiita.com/mito_log/items/6457dc110b3478e3e530)

