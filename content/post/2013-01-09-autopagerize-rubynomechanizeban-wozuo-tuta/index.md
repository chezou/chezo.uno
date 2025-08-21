---
title: Autopagerize-rubyのMechanize版を作った
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2013-01-09 11:01:09+00:00
lastmod: 2013-01-09 11:01:09+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [http, allow, fork, client, 扱い, request, pull, 早い, そのまま, オリジナル]
recommendations: [/post/2014-12-11-julianopatukezigong-kai-hareplkaradekiru-number-juliaac-number-julialang/,
  /post/2019-12-04-r-and-td/, /post/2008-09-04-ji-dong-zhan-shi-gandamuthe-origin-16-17/]
---
[Qiita](http://qiita.com/items/ce9a52030aad51591121)にも書いたけど、Ruby向けAutopagerizeをMechanize対応してみた。

[https://github.com/chezou/autopagerize-ruby/tree/mechanized](https://github.com/chezou/autopagerize-ruby/tree/mechanized)

特徴はMechanizeのrobots.allowをそのまま流用できること。  
それ以外は正直httpclientの方が早いと思います。

いまいちよくわからないのが、forkした場合のgemspecの扱いとpull requestすべきか否か。  
オリジナルとは違うhttpのclientしてるからそのままでいいか。


