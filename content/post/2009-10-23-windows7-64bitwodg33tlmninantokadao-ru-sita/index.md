---
title: "Windows7 64bitをDG33TLMになんとか導入した"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2009-10-23T21:56:10+00:00
lastmod: 2009-10-23T21:56:10+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
予想外に時間がかかってしまった、64bit版の導入。つまずいたところを忘れないようにメモする。

今回の問題は、intel dg33tmlのドライバ周りがデフォルトでは32bit版なのか、Windowsエクスペリメントインデックスが完走しなかった。行ったポイントは２つ。

1.BIOSのアップデートを念のため行う  
2.インテルのサイトでドライバアップデート。一応、チップセット、LAN、グラフィックを３つしっかりいれないとうまくいかなかった。  
64bitのほうがスコア値があがりました。  
ネックは、グラフィックか。


