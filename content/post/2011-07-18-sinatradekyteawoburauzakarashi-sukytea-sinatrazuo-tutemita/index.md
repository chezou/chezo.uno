---
authors: [aki]
categories: null
date: '2011-07-18 15:02:01-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2011-07-18 15:02:01-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: sinatraでKyTeaをブラウザから試すkytea-sinatra作ってみた
keywords: [sinatra, kytea, 結果, mykytea, mecab, 出力, ruby, seikichi, haml, japan]
recommendations: [/post/2011-09-23-kyteawota-yan-yu-deshi-uratupa-plus-amatome/, /post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/,
  /post/2013-10-06-kawasaki-dot-rb-number-004wokai-cui-simasita-number-kwskrb/]
---

先日のエントリで書いたとおり[Mykytea-ruby](https://chezo.uno/post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/)を使って、試しにブラウザから解析結果をみられるkytea-sinatraを作りました。

![](screenshot.png)

といっても、sinatraとhamlを使ってちょっと出力結果を見られるようにしたのシンプルなものです。  
イメージとしては、このような形でブラウザから簡単に解析結果が利用できると何か面白いことができないかなーと思っています。  
本当はどっかのサーバで動かして、jsonとかで気軽に解析結果を取得できるとかになればいいんですけどね。

ソースはgithubにあります。[**kytea\_sinatra@github**](https://github.com/chezou/kytea_sinatra)

KyTeaとMykytea-rubyをインストールした後、Mykytea.soをkytea-sinatraと同一のディレクトリに入れてから実行してください。

```
gem install sinatra haml bundler  
# (または、 gem install bundler; bundle install)

ruby kytea\_sinatra.rb
```

で、ブラウザで

> [http://localhost:4567/](http://localhost:4567/)

を開けばOK。  
なお、mecab-rubyも入っている場合は、下記のスクリプトを実行することで出力結果が比較できます。

> ruby kytea\_sinatra\_mecab.rb

出力結果は冒頭の感じです。

＃しかし、API修正されたその日のうちに [@seikichiさんが kytea-pythonを作られていて](http://twitter.com/seikichi/status/81095004558331904)、それで十分じゃんとか思ったのはここだけの話。  
＃全部叩けるようにするか、MeCabで言うところのparseToString, parseToNodeに絞ってアクセスできるようにしたかの違いだとは思う。  
＃@seikichiさんの.iの方がキレイだと思います。

参考URL

- [_Sinatra_: README (Japanese)](http://www.sinatrarb.com/intro-jp.html)
- [ウノウラボ by Zynga Japan: _Sinatra_気に入った](http://labs.unoh.net/2009/05/sinatra.html)
- [ウノウラボ by Zynga Japan: 5分で分かる_Haml_](http://labs.unoh.net/2009/05/5haml.html)