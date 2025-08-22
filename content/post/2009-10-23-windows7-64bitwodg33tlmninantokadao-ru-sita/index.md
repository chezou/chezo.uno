---
authors:
- aki
categories: null
date: '2009-10-23 14:56:10-07:00'
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
keywords:
- bit
- ドライバ
- グラフィック
- アップデート
- '64'
- 完走
- dg
- bios
- intel
- lan
lastmod: '2009-10-23 14:56:10-07:00'
projects: []
recommendations:
- /post/2009-10-23-windows7gakita-ru-reta-xp-modeshi-sita/
- /post/2009-10-25-macdui-ying-siteinainasnopurintosabaji-neng-woshi-uniha/
- /post/2018-12-01_windows-64bit-mecab--kytea-------2018-b283b6c7b33c/
subtitle: ''
summary: ''
tags: []
title: Windows7 64bitをDG33TLMになんとか導入した
---

予想外に時間がかかってしまった、64bit版の導入。つまずいたところを忘れないようにメモする。

今回の問題は、intel dg33tmlのドライバ周りがデフォルトでは32bit版なのか、Windowsエクスペリメントインデックスが完走しなかった。行ったポイントは２つ。

1.BIOSのアップデートを念のため行う  
2.インテルのサイトでドライバアップデート。一応、チップセット、LAN、グラフィックを３つしっかりいれないとうまくいかなかった。  
64bitのほうがスコア値があがりました。  
ネックは、グラフィックか。