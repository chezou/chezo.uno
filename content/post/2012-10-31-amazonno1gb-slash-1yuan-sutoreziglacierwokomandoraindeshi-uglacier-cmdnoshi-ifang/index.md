---
authors: [aki]
categories: null
date: '2012-10-31 05:10:45-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2012-10-31 05:10:45-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: Amazonの1GB/1円ストレージGlacierをコマンドラインで使うglacier-cmdの使い方
keywords: [cmd, aws, upload, 利用, test, アーカイブ, domain, データ, コマンド, download]
recommendations: [/post/2017-01-19-macnojispei-lie-nokibodowokarabinershi-wazuniuspei-lie-nisuru/,
  /post/2017-05-26_public-dataset/, /post/2016-05-05-detawo-ge-suo-niji-merukotodedetahuo-yong-nomin-zhu-hua-gajin-ndahua/]
---

大分前に発表されました、Amazonの[1GB/1円でデータを保管できるGlacier](http://aws.typepad.com/aws_japan/2012/08/amazon-glacier-archival-storage-for-one-penny-per-gb-per-month.html)というサービスをLinuxサーバから使用したいと思い、Javaでわざわざ書くのも面倒だと思い色々探していたところ、glacier-cmdというツールが良い感じだったのでご紹介します。

[github:amazon-glacier-cmd-interface](https://github.com/uskudnik/amazon-glacier-cmd-interface)

ちなみに、Windowsなら[FastGlacier](http://fastglacier.com/)などのGUIソフトが楽です。

## Glacierの特徴

- Glacierは1GB/1円でデータが無制限に保管できる
- Upload以外の作業は4時間待たされる
- Download時の転送料は普通にかかる(＝そこまで安くない)

安いのには理由があります。Upload以外の作業は、大体Jobを実行してから4時間待たされるのです。  
たとえば、Downloadする前に、このファイルを落としたいんだけど、とJob投げて、準備ができたらダウンロード、という流れです。  
また、最新のファイルリストを取得するにも4時間待たされます。(なので、大体のクライアントがファイルリストをローカルでキャッシュしています)

後、Download時の転送料金は相対的に高く感じます。10TBを保管するのにはus-eastのリージョンで、月$100(約8千円)なのに対し、同量をDownloadした場合$1,228(約10万円)かかります。  
詳細は下記を参照ください。[  
http://aws.amazon.com/jp/glacier/pricing/](http://aws.amazon.com/jp/glacier/pricing/)

削除自体は無料なので、通常のデータを置くのには適さず、二度と見ないかもしれないけど念のためとっておきたいといった類のデータの保管に向いています。Amazon自身もあまり取り出さないことを想定しているようです。

まぁ、テープドライブを使って自前で管理するよりは楽できるかな、という感じなのでしょうか。

## glacier-cmdの利用前に用意するもの

- AWSのAccess Key
- AWSのSecret Key
- Amazon SimpleDBのドメイン名(後述)
そもそも、AWSのアカウントは持ってることを前提にします。そうすると、きっとAccess KeyとSecret Keyも持っていると思います。
## SimpleDBとその利用目的
SimpleDBとは、Amazonが提供するHTTPで利用可能な簡単なDBです。

Glacierはファイルダウンロードや削除時にはハッシュのようなアーカイブIDで操作をし、  
それらの情報を記憶するためにglacier-cmdはSimpleDBを利用しています。

SimpleDBはSQLのTableの概念に相当するdomainというものがあります。  
例えばこれを、ユーザごとに作成することで、各自のファイルのリストを管理します。

## SimpleDBのdomainの作成方法
私自身は、RubyからSimpleDBを扱える[right\_aws](https://github.com/rightscale/right_aws)というgemでdomainを作成したのですが、  
既存のツールで何とかしたい場合は、ブラウザベースのものを使うのが簡単かと思います。

なお、right\_awsの利用には下記を参考にさせていただきました。  
[AmazonWebServiceのSimpleDBをrubyでパフォーマンスチェック - 三並慶佐 - hi-fi-Net Blog](http://www.hi-fi-net.com/blog/blogs/minami/show/104)

1.    下記ツールを解凍し、index.htmlを開く(Chromeでは動作できず。Firefoxは動作確認済み)

[http://aws.amazon.com/code/1137](http://aws.amazon.com/code/1137)

2.     Explore APIからCreateDomainを選択し、Domain Nameにmy-glacier-dbなど適当な名前を入れて、Invoke Requestをクリックする  
参考：[http://docs.amazonwebservices.com/AmazonSimpleDB/latest/GettingStartedGuide/CreatingADomain.html](http://docs.amazonwebservices.com/AmazonSimpleDB/latest/GettingStartedGuide/CreatingADomain.html)

## glacier-cmdのインストール

     $ mkdir ~/env $ cd ~/env $ virtualenv glacier $ source ~/env/glacier/bin/activate (glacier)$ git clone https://github.com/uskudnik/amazon-glacier-cmd-interface.git (glacier)$ cd amazon-glacier-cmd-interface (glacier)$ python setup.py install

今回はvirtualenvを使っているのですが、globalな場所にインストールしたい場合は、適当な場所にインストールするのが良いでしょう。  
基本的に、次回以降glacier-cmdを利用する際は source ~/env/glacier/bin/activateをしましょう。

## glacier-cmdの初期設定
1.  ~/.glacier-cmdに設定を書き込む  
例)

    [aws] access\_key=AWSアクセスキーを書く secret\_key=AWSシークレットキーを書く [glacier] region=us-east-1 bookkeeping=True bookkeeping-domain-name=作成したSimpleDBのdomain名を書く logfile=~/.glacier-cmd.log loglevel=INFO output=print

2.     Glacierのvaultと呼ばれるデータの保管場所を作成する  
$ glacier-cmd mkvault Test

3.     vaultの作成結果を確認する  
$ glacier-cmd lsvault

 以上でGlacierの使用準備は完了です。

## 利用するコマンド群
後は必要に応じて以下のコマンドを利用してください。

下記のコマンドを利用時は毎回

    $ source ~/env/glacier/bin/activate

を実行してください。

- データをuploadする。(upload時に発行されるアーカイブIDが今後の利用に重要)

    $ glacier-cmd upload Test /path/somefile –description “Test data”

- ファイルリストを取得する(ためのjobを発行する。実際に取得するには4時間後、再度実行する)

    $ glacier-cmd inventory Test

- SimpleDBに格納されたファイルリストを取得する

    $ glacier-cmd search Test

- データをダウンロードする

    $ glacier-cmd getarchive Test アーカイブID

…4時間後

    $ glacier-cmd download Test アーカイブID –o outfilename

- データを消去する

    $ glacier-cmd rmarchive Test アーカイブID

- Jobの実行状況を調べる

    $ glacier-cmd listjobs

ちなみに、searchコマンドはglacier-cmdが利用しているSimpleDBにファイルリストをキャッシュしているものを取得するだけです。なので、FastGlacierなど別のツールでUpload,Downloadした際には齟齬がでてしまいます。  
その場合は、inventoryコマンドを2度4時間程度の間隔を空けて行うと反映されると思います。

結構面倒ですが、とにかくいつ使うか分からないデータや、手元の外付けHDDにとりあえず保管してあるけど一応冗長性を持たせたい、とかいう用途には良いでしょう。