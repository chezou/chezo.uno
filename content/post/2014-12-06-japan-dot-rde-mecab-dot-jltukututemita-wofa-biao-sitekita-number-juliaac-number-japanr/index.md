---
title: "Japan.Rで\"MeCab.jlつくってみた\"を発表してきた #JuliaAC #JapanR"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-12-06T18:18:20+00:00
lastmod: 2014-12-06T18:18:20+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
何故か、Facebookで[@shinyorke](https://twitter.com/shinyorke)さんと[Japan.R](https://atnd.org/events/58624)の話をしてたら、[@0kayu](https://twitter.com/0kayu)さんに補足されてしまったので、LT発表してきました。

&lt;iframe src=&quot;//www.slideshare.net/slideshow/embed_code/42416256&quot; width=&quot;476&quot; height=&quot;400&quot; frameborder=&quot;0&quot; marginwidth=&quot;0&quot; marginheight=&quot;0&quot; scrolling=&quot;no&quot;&gt;&lt;/iframe&gt;

[MeCab.jl](https://github.com/chezou/MeCab.jl)の紹介と、R,Ruby,Juliaでのベンチマークについて話しました。

ベンチマーク結果を見ると、gcを切ったらRにはなんとかかっています。

![](/img/2014/12/06/181820/20141206160009.png)

当日の[デモ内容のnotebook](http://nbviewer.ipython.org/gist/chezou/a68cfa3d9abc0e7f669d)はこれです。 ベンチマークに使用したコードはこちら[https://gist.github.com/chezou/1f947423c6655c266e0a](https://gist.github.com/chezou/1f947423c6655c266e0a)

各言語のversionはこんな感じです。

    $ ruby -v ruby 2.1.0p0 (2013-12-25 revision 44422) [x86\_64-darwin13.0] $ julia --version julia version 0.4.0-dev+1752 $ r --version R version 3.1.2 (2014-10-31) -- &quot;Pumpkin Helmet&quot; Copyright (C) 2014 The R Foundation for Statistical Computing Platform: x86\_64-apple-darwin13.4.0 (64-bit) R is free software and comes with ABSOLUTELY NO WARRANTY. You are welcome to redistribute it under the terms of the GNU General Public License versions 2 or 3. For more information about these matters see http://www.gnu.org/licenses/.

やる前はRに対して圧勝！とかならないかなぁとか思っていたのですが、そもそもMeCabをバインディングしてるだけじゃん、と気づいた時には甘かった。 敵は、Rではなかったのです。Cだったのです...。

共有ライブラリを配布して、それをRから呼べるようにしているだけとは恐れ入りました。 RMeCabは、まさか頻度カウントをするための関数まであるとは思ってもみなかったのですが、基本的に遅くなる処理はCにまかせてしまうというのは戦略的には合理的ですね。

## おまけ

会場ではきちんと言えなかったのですが、Juliaのバインディングをする上でのPros/Consはこんな感じです

- Pros
  - Cを書くことなくCのバインディングができる
- Cons
  - C++は現状(特にMacからは)辛い
  - gc!
  - 文字列処理が遅いかも？(要検証)

Rubyに対して遅いのは、ちょっと検証してみます。

特に「Cを書くことなく」という点は素晴らしく、 MeCabのnodeの構造体に対応するtypeを作れば、それでcastしてくれてJuliaから扱えるようになります。

[mecab.h](https://code.google.com/p/mecab/source/browse/trunk/mecab/src/mecab.h)からCのコードを抜粋

    struct mecab\_node\_t { struct mecab\_node\_t \*prev; struct mecab\_node\_t \*next; struct mecab\_node\_t \*enext; struct mecab\_node\_t \*bnext; struct mecab\_path\_t \*rpath; struct mecab\_path\_t \*lpath; const char \*surface; const char \*feature; unsigned int id; unsigned short length; unsigned short rlength; unsigned short rcAttr; unsigned short lcAttr; unsigned short posid; unsigned char char\_type; unsigned char stat; unsigned char isbest; float alpha; float beta; float prob; short wcost; long cost; };

対応する[MeCab.jlのコード](https://github.com/chezou/MeCab.jl/blob/master/src/MeCab.jl#L40-L63)

    type MecabRawNode prev::Ptr{MecabRawNode} next::Ptr{MecabRawNode} enext::Ptr{MecabRawNode} bnext::Ptr{MecabRawNode} rpath::Ptr{Void} lpath::Ptr{Void} surface::Ptr{Uint8} feature::Ptr{Uint8} id::Cint length::Cushort rlength::Cushort rcAttr::Cushort lcAttr::Cushort posid::Cushort char\_type::Cuchar stat::Cuchar isbest::Cuchar alpha::Cfloat beta::Cfloat prob::Cfloat wcost::Cshort cost::Clong end

`mecab_node_path_t`は使っていないので捨てています。

Cの場合、headerに構造体を先に宣言すれば、お互いが依存する構造体を記述できますが、Juliaの場合はそれができないため`Ptr{Void}`で受けています。


