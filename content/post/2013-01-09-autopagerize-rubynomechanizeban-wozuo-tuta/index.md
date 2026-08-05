---
authors:
  - aki
categories: null
date: 2013-01-09 03:01:09-08:00
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2013-01-09 03:01:09-08:00
projects: []
subtitle: ''
summary: ''
tags: []
title: Autopagerize-rubyのMechanize版を作った
keywords:
  - そのまま
  - http
  - allow
  - fork
  - client
  - 扱い
  - request
  - pull
  - 早い
  - 特徴
recommendations:
  - /post/2012-01-07-mercurialtoqin-he-xing-nogao-iripozitoriburauzarhodecodewoinsutorusitemita/
  - /post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/
  - /post/2015-08-30-number-tqrk09-de-accept-lt-sitehazimeteno-gem-woraiburirisunishi-bai-simasita/
---


[Qiita](http://qiita.com/items/ce9a52030aad51591121)にも書いたけど、Ruby向けAutopagerizeをMechanize対応してみた。

[https://github.com/chezou/autopagerize-ruby/tree/mechanized](https://github.com/chezou/autopagerize-ruby/tree/mechanized)

特徴はMechanizeのrobots.allowをそのまま流用できること。  
それ以外は正直httpclientの方が早いと思います。

いまいちよくわからないのが、forkした場合のgemspecの扱いとpull requestすべきか否か。  
オリジナルとは違うhttpのclientしてるからそのままでいいか。