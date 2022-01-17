---
title: 'Juliaでword countして気づいたこと #JuliaAC'
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2014-12-24 00:00:00+00:00
lastmod: 2014-12-24 00:00:00+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [word, julia, dict, text, time, hash, mecab, end, string, utf]
recommendations: [/post/2015-02-18-word2vecke-shi-hua-suruyatuwoipython-notebookkarajian-reruyounisita/,
  /post/2014-05-06-julia-vs-python-bitutokoinopusiyonnomontekarurosimiyuresiyon/,
  /post/2015-11-08-tinysegmenter-dot-jlwogotobi-jiao-sitefu-ketatosi-tutararuo-zhe-gazui-shi-hua-sitekureta/]
---
この記事は、[Julia Advent Calendar](http://qiita.com/advent-calendar/2014/julialang) 24日目の記事です。 昨日は[@nezuqさんのJuliaで楽しくWebスクレイピング！](http://qiita.com/nezuq/items/58ad2431654b5a494543)でした。

悲しいお知らせですが、このブログを通じてわかったのは、Python \> Ingress \>\>\> Juliaという人気度だということでした。Ingressの話は今回しません。

当初は、Cで書かれたライブラリをバインディングする方法について書こうと思っていたのですが、r9y9さんによる[ポインタ周りの解説](http://r9y9.github.io/blog/2014/12/09/julia-advent-calender-2014-poiner-tips/)が出ていたので、必要なくなったかなと思い、Juliaならではの型の話をしたいと思います。

このお話は、自分が[julia-usersで質問したこと](https://groups.google.com/d/topic/julia-users/uIotqx3M12g/discussion)の回答をまとめたものです。

気軽にコミッターから斧が飛んでくるのがいいですね。さすが、Karpinskiさん\*1

# Ruby脳のWord count

僕は自然言語処理が好きなので、word countをちょくちょくやります。MapReduce時代以降Word countはHello worldの代わりに急成長していると言えましょう。 Rubyでword countをするなら、Hashを使ってこう書きます

    hash = Hash.new{|h, k| h[k] = 0 } words.each do |word| hash[word] += 1end

もし、閾値以下の単語を除去したいならもう一回ループを回して、判定しますが、頻度top N個の単語を取り出したいときはどうしますか？

top10個の単語を取り出したいときはこう書きます。

    hash.sort\_by{|\_,v| -v}.take(10)

簡単ですね。

# Juliaの世界でのWord count

では、Juliaでも同様のことをやりたくなった場合どう書きますか？ Dictをsortしたいですよね？

できないんです

    julia\> sort( sort(r::UnitRange{T<:real at range.jl:531 sort sort.jl:346 range.jl:534 sort.jl:364>
    
    
    <p>あれれ？調べていると、過去には<code>sort_by</code>が出来た時期もあったようなのですが、今は出来ないようです。</p>
    
    <p>そこで考えだしたのは、DataFrameを使えばいいんじゃない！って方法</p>
    
    <pre class="code" data-lang="" data-unlink>dict = Dict{String, Int64}("apple" =&gt; 100, "town" =&gt; 250, "space" =&gt; 24)
    df = DataFrame(word = collect(keys(dict)), count = collect(values(dict)))
    sort(df, cols = [:count], rev = true)</pre>
    
    
    <p>でも、このDataFrameの作り方、<code>convert(DataFrame, dict)</code>で単純にできる形式と全然違うので不安ですよね。
    なので、<a href="https://groups.google.com/d/topic/julia-users/uIotqx3M12g/discussion">有識者に聞いてみました</a>。</p>
    
    <h1>julia-usersで聞いてみた回答</h1>
    
    <p>閾値処理をしたいなら、<code>Dict()</code>作って二回ループ回せばいいし、Top　N個の単語を取ってきたいのなら、<a href="http://julia.readthedocs.org/en/latest/stdlib/collections/#priorityqueue"><code>PriorityQueue()</code></a>を使うのがいいよ、との回答でした。</p>
    
    <p>後からsortするとo(NlogN)かかるじゃん。それだったら、最適なデータ構造を使えばいいんじゃないの、ということでした。確かに。</p>
    
    <p>こんなコードになります。
    書き方も処理速度もほとんど代わりませんね。<code>Collection.dequeue!(pq)</code>して、必要な回数だけ取り出しましょう。</p>
    
    <pre class="code" data-lang="" data-unlink>julia&gt; f = open("input.txt")
    IOStream(<file input.txt>)
    
    julia&gt; text = readall(f);
    
    julia&gt; function count_word(text::UTF8String)
             mecab = Mecab("-O wakati")
             counts = Dict{UTF8String, Int}()
             for word in split(sparse_tostr(mecab, text))
                 counts[word] = get(counts, word, 0) + 1
               end
             counts
           end
    count_word (generic function with 1 method)
    
    julia&gt; @time count_word(text)
    elapsed time: 0.953731616 seconds (29676144 bytes allocated, 24.68% gc time)
    Dict{UTF8String,Int64} with 13583 entries:
      "ウィキ" =&gt; 1
      "TAKE" =&gt; 2
      "null" =&gt; 4
      "変革" =&gt; 5
      "クソ" =&gt; 1
      "228" =&gt; 3
      "迫っ" =&gt; 1
      "村山" =&gt; 1
      "寺嶋" =&gt; 1
      "リビング" =&gt; 1
      "国籍" =&gt; 1
      "ベーコン" =&gt; 1
      "出す" =&gt; 13
      "Core" =&gt; 5
      "当選" =&gt; 2
      "moguno" =&gt; 1
      "Brainfuck" =&gt; 1
      "積ん" =&gt; 4
      "backup" =&gt; 2
      "stress" =&gt; 1
      "Qw" =&gt; 1
      "細かい" =&gt; 3
      "従って" =&gt; 1
      "括弧" =&gt; 1
      "ある程度" =&gt; 1
      "法" =&gt; 14
      ⋮ =&gt; ⋮
    
    julia&gt; function count_word2(text::UTF8String)
             mecab = Mecab("-O wakati")
             counts = Collections.PriorityQueue()
             for word in split(sparse_tostr(mecab, text))
                 counts[word] = get(counts, word, 0) - 1
               end
             counts
           end
    count_word2 (generic function with 1 method)
    
    julia&gt; @time count_word2(text)
    elapsed time: 0.891081099 seconds (24265472 bytes allocated, 20.83% gc time)
    PriorityQueue{Any,Any,ForwardOrdering} with 13583 entries:
      "ウィキ" =&gt; -1
      "TAKE" =&gt; -2
      "null" =&gt; -4
      "変革" =&gt; -5
      "クソ" =&gt; -1
      "228" =&gt; -3
      "迫っ" =&gt; -1
      "村山" =&gt; -1
      "寺嶋" =&gt; -1
      "リビング" =&gt; -1
      "国籍" =&gt; -1
      "ベーコン" =&gt; -1
      "出す" =&gt; -13
      "Core" =&gt; -5
      "当選" =&gt; -2
      "moguno" =&gt; -1
      "Brainfuck" =&gt; -1
      "積ん" =&gt; -4
      "backup" =&gt; -2
      "stress" =&gt; -1
      "Qw" =&gt; -1
      "細かい" =&gt; -3
      "従って" =&gt; -1
      "括弧" =&gt; -1
      "ある程度" =&gt; -1
      "法" =&gt; -14
      ⋮ =&gt; ⋮</file></pre>
    
    
    <p>型と多重dispatchがある分、なんでも同じようにできるわけではないこと、そしてそれをやるのが本当に最適手なのかを考えることができました。
    なお、julia-usersは気軽に質問できてどんどん斧が飛んできて楽しいので、みなさんも読むことをおすすめします！</p>
    
    <p>明日はkimrinさんによるJuliaで楽器を作ろう！です。楽しみですね。</p>
    <div class="footnote">
    <p class="footnote"><a href="#fn-23bc65e3" name="f-23bc65e3" class="footnote-number">*1</a><span class="footnote-delimiter">:</span><span class="footnote-text">本人のアイコン、バイキングの帽子をかぶっているのが有名ですよね</span></p>
    </div>
    </:real>


