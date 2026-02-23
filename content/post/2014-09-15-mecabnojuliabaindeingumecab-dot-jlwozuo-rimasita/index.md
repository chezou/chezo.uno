---
authors: [aki]
categories: null
date: '2014-09-15 05:09:52-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2014-09-15 05:09:52-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: MeCabのJuliaバインディングMeCab.jlを作りました
keywords: [ptr, mecab, void, end, julia, int, 構造体, ポインタ, length, uint]
recommendations: [/post/2014-12-06-japan-dot-rde-mecab-dot-jltukututemita-wofa-biao-sitekita-number-juliaac-number-japanr/,
  /post/2016-10-15-rnnlmbesunoxing-tai-su-jie-xi-qi-juman-plus-plus-wohomebrewdeinsutorudekiruyounisita/,
  /post/2015-09-23-mecab-dot-jlwojulia-v0-dot-4-0-rc2nidui-ying-sita/]
---

Juliaから日本語形態素解析器として最も有名な[MeCab](https://code.google.com/p/mecab/)を使える[MeCab.jl](https://github.com/chezou/MeCab.jl)を作りました。

まだ、METADATA.jlに[マージされていない](https://github.com/JuliaLang/METADATA.jl/pull/1446)のですが、きっと明日には使えるようになっていると思います。  
[2014/09/15 23:33追記] マージされました！

## How to use

簡単な使い方は

    Pkg.add("MeCab")

を一度していただければ、こんな感じでアクセスできます

    using MeCab mecab = Mecab() results = parse(mecab, "すももももももももものうち") for result in results println(result.surface, ":", result.feature) end

## JuliaでCのコードをbindingするには

基本的には、公式マニュアルを読めばいいです。

[Calling C and Fortran Code — Julia Language 0.4.0-dev documentation](http://julia.readthedocs.org/en/latest/manual/calling-c-and-fortran-code/)

とかだけ書くと大分辛いのですが、ポイントは`ccall`を使えば良いということです。

例えば、以下の様なCのコードがあったとします。(マニュアルより引用)

    int main(int argc, char \*\*argv);

すると、Julia側のコードはこう書けばよいのです。

    argv = ["a.out", "arg1", "arg2"] ccall(:main, Int32, (Int32, Ptr{Ptr{Uint8}}), length(argv), argv)

問題は、ポインタが帰ってくる場合どうすればいいのかです。  
これは、意外と簡単で第二引数を`Ptr{Void}`で受けてあげれば良いです。

返り値が構造体なんかの場合は、対応する`immutable`をJuliaで作ってあげて、`unsafe_load`すれば良さそうです。

なお、関数ポインタも受けれるとか。  
[C Structs with function pointers - Google グループ](https://groups.google.com/forum/#!msg/julia-users/8isqR_J4r8Y/L2sa0T_KJBUJ)

ただ未確認ですが、構造体のメンバに構造体がいる場合はどうやればいいのかわかりませんでした。  
(なので、今回は`mecab_node_t`は諦めた)

## コンストラクタとデストラクタ

MeCabのtaggerの様にに、Cで確保したポインタを保持しておく場合、コンストラクタで作りデストラクタで解放するのが良いようです。

bicycle1885さんのこの記事を参考に、実装してみました。  
[Juliaのデストラクター - りんごがでている](http://bicycle1885.hatenablog.com/entry/2014/03/16/113501)

    type Mecab ptr::Ptr{Void} function Mecab(option::String = "") argv = split(option) if(length(argv) == 0) argv = [""] end ptr = ccall( (:mecab\_new, "libmecab"), Ptr{Void}, (Cint, Ptr{Ptr{Uint8}}), length(argv), argv ) if ptr == C\_NULL error("failed to create tagger") end smart\_p = new(ptr) finalizer(smart\_p, obj -\> ccall((:mecab\_destroy, "libmecab"), Void, (Ptr{Void},), obj.ptr)) smart\_p end end

ポイントは`finalizer`を実装すると、それがデストラクタとして働くということです。

## C++は？クラスとかnamespaceとかは？

どうも扱えないようです。  
色々と調べたのですが、特にnamespace周りは鬼門のようです。

なので、`extern C`をしながらwrapperを一枚書くのが良さそうですね。

## 最後に

思ったより簡単にバインディングができました。  
多分、Kytea.jlも書けそう。

この内容を[JuliaTokyo #2](http://juliatokyo.connpass.com/event/8010/)でLTしてこようと思います。