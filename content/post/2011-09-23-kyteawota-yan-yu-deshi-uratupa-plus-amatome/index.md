---
authors: [aki]
categories: null
date: '2011-09-22 22:09:10-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2011-09-22 22:09:10-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: KyTeaを他言語で使うラッパー+αまとめ
keywords: [kytea, sinatra, mykytea, 言語モデル, 推定, 読み, nltk, 対話, 音声, python]
recommendations: [/post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/,
  /post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/,
  /post/2011-09-14-nltkkarakyteadekopasuwodu-miip-mujpkyteatokenizerzuo-rimasita/]
---

[@neubig](http://twitter.com/neubig)さんの作られたKyTeaを他言語で利用できるラッパーですが、  
拙作のMykytea意外にも色々とあるようなのでまとめておきます。

KyTeaって何？って人は[本家](http://www.phontron.com/kytea/index-ja.html)やこちらの[@nokunoさんの記事](http://d.hatena.ne.jp/nokuno/20100307/1267923299)がわかりやすいですが、  
一言で言うと形態素解析や読みの推定を行ってくれるものです。  
MeCabと違って読みの推定をまじめにやってくれるようです。

### Ruby

- [Mykytea-ruby](https://chezo.uno/post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/) (@chezou作)

### Python

- [Mykytea-python](https://chezo.uno/post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/) (@chezou作)
- [kytea-python](https://github.com/seikichi/kytea-python) ([@seikichi](https://twitter.com/#%21/seikichi/)さん作。[Tweet](https://twitter.com/#%21/seikichi/status/81095004558331904))

### Perl

- [Text::KyTea](http://pawa.dojikko.com/pg/perl/2614.html) ([@\_pawa\_](https://twitter.com/#!/_pawa_)さん作)

### 番外編

- sinatra : [sinatraでKyTeaをブラウザから試すkytea-sinatra作ってみた](https://chezo.uno/post/2011-07-18-sinatradekyteawoburauzakarashi-sukytea-sinatrazuo-tutemita/)
- NLTK : [NLTKからKyTeaでコーパスを読み込むJPKyteaTokenizer作りました](https://chezo.uno/post/2011-09-14-nltkkarakyteadekopasuwodu-miip-mujpkyteatokenizerzuo-rimasita/)
- [音声対話用言語モデル作成](http://plata.ar.media.kyoto-u.ac.jp/sasada/research/project/dialog/) ([@ssyn](http://twitter.com/ssyn)さん)
- [KyTeaで音声対話用言語モデル あしたからがんばる ―椀屋本舗](http://d.hatena.ne.jp/caesar_wanya/20101121) ([@caesar\_wanya](http://twitter.com/caesar_wanya)さん)