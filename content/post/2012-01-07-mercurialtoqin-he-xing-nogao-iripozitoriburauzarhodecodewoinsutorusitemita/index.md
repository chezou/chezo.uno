---
title: "Mercurialと親和性の高いリポジトリブラウザRhodeCodeをインストールしてみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2012-01-07T09:01:19+00:00
lastmod: 2012-01-07T09:01:19+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
[![](https://chezou.files.wordpress.com/2012/01/rhodecode.png?w=300 &quot;rhodecode&quot;)](http://rhodecode.org/)

Mercurialと連動するブラウザベースのリポジトリ管理システム、[RhodeCode](http://rhodecode.org/)を導入したのでその際のメモを書き残します。  
一言で言うと、githubみたいなものを社内などで運用したいというニーズに応えるものです。  
gitlabとかも試してみましたが、ドツボにはまったので結局RhodeCodeに落ち着きました。

デモは[こちら](http://demo.rhodecode.org/)

### RhodeCodeの特徴

- ブラウザ上でリポジトリを作成できる(これ重要)
- diffやコミットログがブラウザ上で見られる
- ブランチも可視化してくれる
- プロジェクトをグループでまとめることもできる
- 意外と導入、運用は簡単だった
- そのうちgitにも対応する予定らしい
- あまり日本語で情報が少ないかも

### 

### Rhodecodeのインストール
基本的にオフィシャルに従う方針で行きました。  
ただし、virtualenvを使った方が環境を汚さないと思うので、そうすることにしました。

[http://packages.python.org/RhodeCode/installation.html](http://packages.python.org/RhodeCode/installation.html)

[http://packages.python.org/RhodeCode/setup.html](http://packages.python.org/RhodeCode/setup.html)  
ユーザは、適当にadduserで作ってください。  
今回はhgというユーザを作りました。

    adduser&amp;nbsp;--system&amp;nbsp;--home&amp;nbsp;/home/hg/ --group&amp;nbsp;--shell&amp;nbsp;/bin/bash hg sudo&amp;nbsp;mkdir&amp;nbsp;&amp;nbsp;/var/www/rhodecode-venv sudo&amp;nbsp;chown hg:hg /var/www/rhodecode-venv virtualenv&amp;nbsp;--no-site-packages&amp;nbsp;/var/www/rhodecode-venv # hgが一般権限で利用できるようにする必要がある source&amp;nbsp;/var/www/rhodecode-venv/bin/activate sudo&amp;nbsp;mkdir&amp;nbsp;/var/www/rhodecode sudo&amp;nbsp;chown hg:hg /var/www/rhodecode cd&amp;nbsp;/var/www/rhodecode pip&amp;nbsp;install&amp;nbsp;rhodecode

#### RabbitMqの導入
一応入れました(結局使ってないかも？)

    sudo&amp;nbsp;apt-get&amp;nbsp;install&amp;nbsp;rabbitmq-server

#### Rhodecodeの設定

    cd&amp;nbsp;/var/www/rhodecode paster make-config RhodeCode production.ini paster setup-app production.ini

途中で、リポジトリの場所、adminユーザの名前、パスワード、メールアドレスが求められる  
実行する

    paster serve production.ini

#### 問題点
・UnicodeDecodeErrorが出る  
hgユーザの言語設定を下記で解決。  
日本語ja\_JP.UTF-8にしてMercurialをインストールすると、どうやらRhodeCodeがこける模様。

    export&amp;nbsp;LC\_ALL=C

rhodecode-init.shを作成。

./rhodecode-init.sh

    #!/bin/bash export&amp;nbsp;LC\_ALL=C source&amp;nbsp;/var/www/rhodecode-venv/bin/activate cd&amp;nbsp;/var/www/rhodecode paster serve production.ini

#### 実行方法
とりあえず、起動時にrhodecode-init.shを実行することで運用しています。  
本格的に動かすならinit.dなどに書いた方がいいかも。

    sudo -u hg ./rhodecode-init.sh


