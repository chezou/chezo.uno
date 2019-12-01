---
title: "MeCabのJuliaバインディングMeCab.jlを作りました"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-09-15T12:09:52+00:00
lastmod: 2014-09-15T12:09:52+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
Juliaから日本語形態素解析器として最も有名な[MeCab](https://code.google.com/p/mecab/)を使える[MeCab.jl](https://github.com/chezou/MeCab.jl)を作りました。

まだ、METADATA.jlに[マージされていない](https://github.com/JuliaLang/METADATA.jl/pull/1446)のですが、きっと明日には使えるようになっていると思います。  
[2014/09/15 23:33追記] マージされました！

## How to use

簡単な使い方は

    Pkg.add(&quot;MeCab&quot;)

を一度していただければ、こんな感じでアクセスできます

    using MeCab mecab = Mecab() results = parse(mecab, &quot;すももももももももものうち&quot;) for result in results println(result.surface, &quot;:&quot;, result.feature) end

## JuliaでCのコードをbindingするには

基本的には、公式マニュアルを読めばいいです。

[Calling C and Fortran Code — Julia Language 0.4.0-dev documentation](http://julia.readthedocs.org/en/latest/manual/calling-c-and-fortran-code/)

とかだけ書くと大分辛いのですが、ポイントは`ccall`を使えば良いということです。

例えば、以下の様なCのコードがあったとします。(マニュアルより引用)

    int main(int argc, char \*\*argv);

すると、Julia側のコードはこう書けばよいのです。

    argv = [&quot;a.out&quot;, &quot;arg1&quot;, &quot;arg2&quot;] ccall(:main, Int32, (Int32, Ptr{Ptr{Uint8}}), length(argv), argv)

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

    type Mecab ptr::Ptr{Void} function Mecab(option::String = &quot;&quot;) argv = split(option) if(length(argv) == 0) argv = [&quot;&quot;] end ptr = ccall( (:mecab\_new, &quot;libmecab&quot;), Ptr{Void}, (Cint, Ptr{Ptr{Uint8}}), length(argv), argv ) if ptr == C\_NULL error(&quot;failed to create tagger&quot;) end smart\_p = new(ptr) finalizer(smart\_p, obj -\&gt; ccall((:mecab\_destroy, &quot;libmecab&quot;), Void, (Ptr{Void},), obj.ptr)) smart\_p end end

ポイントは`finalizer`を実装すると、それがデストラクタとして働くということです。

## C++は？クラスとかnamespaceとかは？

どうも扱えないようです。  
色々と調べたのですが、特にnamespace周りは鬼門のようです。

なので、`extern C`をしながらwrapperを一枚書くのが良さそうですね。

## 最後に

思ったより簡単にバインディングができました。  
多分、Kytea.jlも書けそう。

この内容を[JuliaTokyo #2](http://juliatokyo.connpass.com/event/8010/)でLTしてこようと思います。


