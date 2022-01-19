---
title: KyTeaを他言語で使うラッパー+αまとめ
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2011-09-23 05:09:10+00:00
lastmod: 2011-09-23 05:09:10+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [kytea, sinatra, mykytea, nltk, python, 言語モデル, ruby, 推定, コーパス, 読み]
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

- [Mykytea-ruby](http://chezou.wordpress.com/2011/07/15/kytea%e3%82%92ruby-python%e3%81%8b%e3%82%89%e4%bd%bf%e3%81%88%e3%82%8bmykytea%e3%82%92%e4%bd%9c%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/ "KyTea:京都テキスト解析ツールキット をRuby, Pythonから使えるMykyteaを作ってみた") (@chezou作)

### Python

- [Mykytea-python](http://chezou.wordpress.com/2011/07/15/kytea%e3%82%92ruby-python%e3%81%8b%e3%82%89%e4%bd%bf%e3%81%88%e3%82%8bmykytea%e3%82%92%e4%bd%9c%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/ "KyTea:京都テキスト解析ツールキット をRuby, Pythonから使えるMykyteaを作ってみた") (@chezou作)
- [kytea-python](https://github.com/seikichi/kytea-python) ([@seikichi](https://twitter.com/#%21/seikichi/)さん作。[Tweet](https://twitter.com/#%21/seikichi/status/81095004558331904))

### Perl

- [Text::KyTea](http://pawa.dojikko.com/pg/perl/2614.html) ([@\_pawa\_](https://twitter.com/#!/_pawa_)さん作)

### 番外編

- sinatra : [sinatraでKyTeaをブラウザから試すkytea-sinatra作ってみた](http://chezou.wordpress.com/2011/07/18/sinatra%e3%81%a7kytea%e3%82%92%e3%83%96%e3%83%a9%e3%82%a6%e3%82%b6%e3%81%8b%e3%82%89%e8%a9%a6%e3%81%99kytea-sinatra%e4%bd%9c%e3%81%a3%e3%81%a6%e3%81%bf%e3%81%9f/ "sinatraでKyTeaをブラウザから試すkytea-sinatra作ってみた")
- NLTK : [NLTKからKyTeaでコーパスを読み込むJPKyteaTokenizer作りました](http://chezou.wordpress.com/2011/09/14/nltk%e3%81%8b%e3%82%89kytea%e3%81%a7%e3%82%b3%e3%83%bc%e3%83%91%e3%82%b9%e3%82%92%e8%aa%ad%e3%81%bf%e8%be%bc%e3%82%80jpkyteatokenizer/ "NLTKからKyTeaでコーパスを読み込むJPKyteaTokenizer作りました")
- [音声対話用言語モデル作成](http://plata.ar.media.kyoto-u.ac.jp/sasada/research/project/dialog/) ([@ssyn](http://twitter.com/ssyn)さん)
- [KyTeaで音声対話用言語モデル あしたからがんばる ―椀屋本舗](http://d.hatena.ne.jp/caesar_wanya/20101121) ([@caesar\_wanya](http://twitter.com/caesar_wanya)さん)

