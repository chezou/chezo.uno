---
title: Windows7 64bitをDG33TLMになんとか導入した
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2009-10-23 21:56:10+00:00
lastmod: 2009-10-23 21:56:10+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [bit, '64', lan, '33', ネック, デフォルト, '32', 一応, うまく, 導入]
recommendations: [/post/2009-10-23-windows7gakita-ru-reta-xp-modeshi-sita/, /post/2018-12-01_Windows-64bit-MeCab--KyTea-------2018-b283b6c7b33c/,
  /post/2011-02-05-acer-aspire-1410wocrucial-realssd-c300niwai-fu-kedvdnasinihuan-zhuang-sita/]
---
予想外に時間がかかってしまった、64bit版の導入。つまずいたところを忘れないようにメモする。

今回の問題は、intel dg33tmlのドライバ周りがデフォルトでは32bit版なのか、Windowsエクスペリメントインデックスが完走しなかった。行ったポイントは２つ。

1.BIOSのアップデートを念のため行う  
2.インテルのサイトでドライバアップデート。一応、チップセット、LAN、グラフィックを３つしっかりいれないとうまくいかなかった。  
64bitのほうがスコア値があがりました。  
ネックは、グラフィックか。


