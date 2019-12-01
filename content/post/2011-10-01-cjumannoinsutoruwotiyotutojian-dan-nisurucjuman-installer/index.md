---
title: "cJumanのインストールをちょっと簡単にするcJuman-installer"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2011-10-01T22:02:34+00:00
lastmod: 2011-10-01T22:02:34+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
cJumanという[@kharakawa](http://twitter.com/kharakawa) さんの作成された、形態素解析器Jumanをpythonから使うためのSWIGで作られたラッパーがあります。

[python-cjuman: A Python (SWIG) bindings of JUMAN, A Japanese Morphological Analyzer](http://app-dist.khlog.net/software/python-cjuman/)

「入門自然言語処理」でも紹介されているのですが、インストールが少し面倒でした。

特にこの辺。

&gt; \&gt;|bash|  
&gt; gcc -c cJuman\_wrap.c -fPIC -I/usr/include/python2.4  
&gt; gcc -shared \*.o -o \_cJuman.so  
&gt; sudo install -m 644 \_cJuman.so cJuman.py /usr/lib/python2.4/site-packages/  
&gt; |


