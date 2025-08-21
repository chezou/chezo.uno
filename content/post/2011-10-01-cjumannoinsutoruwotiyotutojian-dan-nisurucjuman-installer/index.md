---
title: cJumanのインストールをちょっと簡単にするcJuman-installer
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2011-10-01 22:02:34+00:00
lastmod: 2011-10-01 22:02:34+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [python, juman, gcc, usr, '2.4', swig, morphological, analyzer, '644', wrap]
recommendations: [/post/2011-07-15-kytea-jing-du-tekisutojie-xi-turukituto-woruby-pythonkarashi-erumykyteawozuo-tutemita/,
  /post/2014-01-18-ke-xue-ji-suan-niokerujun-zhi-hua-aruihanazepythongazhao-shi-nita-yan-yu-nosieawoduo-tuteiruka/,
  /post/2016-10-15-rnnlmbesunoxing-tai-su-jie-xi-qi-juman-plus-plus-wohomebrewdeinsutorudekiruyounisita/]
---
cJumanという[@kharakawa](http://twitter.com/kharakawa) さんの作成された、形態素解析器Jumanをpythonから使うためのSWIGで作られたラッパーがあります。

[python-cjuman: A Python (SWIG) bindings of JUMAN, A Japanese Morphological Analyzer](http://app-dist.khlog.net/software/python-cjuman/)

「入門自然言語処理」でも紹介されているのですが、インストールが少し面倒でした。

特にこの辺。

> \>|bash|  
> gcc -c cJuman\_wrap.c -fPIC -I/usr/include/python2.4  
> gcc -shared \*.o -o \_cJuman.so  
> sudo install -m 644 \_cJuman.so cJuman.py /usr/lib/python2.4/site-packages/  
> |


