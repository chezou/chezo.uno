---
title: "Juliaでword countして気づいたこと #JuliaAC"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2014-12-24T00:00:00+00:00
lastmod: 2014-12-24T00:00:00+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
この記事は、[Julia Advent Calendar](http://qiita.com/advent-calendar/2014/julialang) 24日目の記事です。 昨日は[@nezuqさんのJuliaで楽しくWebスクレイピング！](http://qiita.com/nezuq/items/58ad2431654b5a494543)でした。

悲しいお知らせですが、このブログを通じてわかったのは、Python \&gt; Ingress \&gt;\&gt;\&gt; Juliaという人気度だということでした。Ingressの話は今回しません。

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

    julia\&gt; sort( sort(r::UnitRange{T&lt;:real at range.jl:531 sort sort.jl:346 range.jl:534 sort.jl:364&gt;
    
    
    &lt;p&gt;あれれ？調べていると、過去には&lt;code&gt;sort_by&lt;/code&gt;が出来た時期もあったようなのですが、今は出来ないようです。&lt;/p&gt;
    
    &lt;p&gt;そこで考えだしたのは、DataFrameを使えばいいんじゃない！って方法&lt;/p&gt;
    
    &lt;pre class=&quot;code&quot; data-lang=&quot;&quot; data-unlink&gt;dict = Dict{String, Int64}(&quot;apple&quot; =&amp;gt; 100, &quot;town&quot; =&amp;gt; 250, &quot;space&quot; =&amp;gt; 24)
    df = DataFrame(word = collect(keys(dict)), count = collect(values(dict)))
    sort(df, cols = [:count], rev = true)&lt;/pre&gt;
    
    
    &lt;p&gt;でも、このDataFrameの作り方、&lt;code&gt;convert(DataFrame, dict)&lt;/code&gt;で単純にできる形式と全然違うので不安ですよね。
    なので、&lt;a href=&quot;https://groups.google.com/d/topic/julia-users/uIotqx3M12g/discussion&quot;&gt;有識者に聞いてみました&lt;/a&gt;。&lt;/p&gt;
    
    &lt;h1&gt;julia-usersで聞いてみた回答&lt;/h1&gt;
    
    &lt;p&gt;閾値処理をしたいなら、&lt;code&gt;Dict()&lt;/code&gt;作って二回ループ回せばいいし、Top　N個の単語を取ってきたいのなら、&lt;a href=&quot;http://julia.readthedocs.org/en/latest/stdlib/collections/#priorityqueue&quot;&gt;&lt;code&gt;PriorityQueue()&lt;/code&gt;&lt;/a&gt;を使うのがいいよ、との回答でした。&lt;/p&gt;
    
    &lt;p&gt;後からsortするとo(NlogN)かかるじゃん。それだったら、最適なデータ構造を使えばいいんじゃないの、ということでした。確かに。&lt;/p&gt;
    
    &lt;p&gt;こんなコードになります。
    書き方も処理速度もほとんど代わりませんね。&lt;code&gt;Collection.dequeue!(pq)&lt;/code&gt;して、必要な回数だけ取り出しましょう。&lt;/p&gt;
    
    &lt;pre class=&quot;code&quot; data-lang=&quot;&quot; data-unlink&gt;julia&amp;gt; f = open(&quot;input.txt&quot;)
    IOStream(&lt;file input.txt&gt;)
    
    julia&amp;gt; text = readall(f);
    
    julia&amp;gt; function count_word(text::UTF8String)
             mecab = Mecab(&quot;-O wakati&quot;)
             counts = Dict{UTF8String, Int}()
             for word in split(sparse_tostr(mecab, text))
                 counts[word] = get(counts, word, 0) + 1
               end
             counts
           end
    count_word (generic function with 1 method)
    
    julia&amp;gt; @time count_word(text)
    elapsed time: 0.953731616 seconds (29676144 bytes allocated, 24.68% gc time)
    Dict{UTF8String,Int64} with 13583 entries:
      &quot;ウィキ&quot; =&amp;gt; 1
      &quot;TAKE&quot; =&amp;gt; 2
      &quot;null&quot; =&amp;gt; 4
      &quot;変革&quot; =&amp;gt; 5
      &quot;クソ&quot; =&amp;gt; 1
      &quot;228&quot; =&amp;gt; 3
      &quot;迫っ&quot; =&amp;gt; 1
      &quot;村山&quot; =&amp;gt; 1
      &quot;寺嶋&quot; =&amp;gt; 1
      &quot;リビング&quot; =&amp;gt; 1
      &quot;国籍&quot; =&amp;gt; 1
      &quot;ベーコン&quot; =&amp;gt; 1
      &quot;出す&quot; =&amp;gt; 13
      &quot;Core&quot; =&amp;gt; 5
      &quot;当選&quot; =&amp;gt; 2
      &quot;moguno&quot; =&amp;gt; 1
      &quot;Brainfuck&quot; =&amp;gt; 1
      &quot;積ん&quot; =&amp;gt; 4
      &quot;backup&quot; =&amp;gt; 2
      &quot;stress&quot; =&amp;gt; 1
      &quot;Qw&quot; =&amp;gt; 1
      &quot;細かい&quot; =&amp;gt; 3
      &quot;従って&quot; =&amp;gt; 1
      &quot;括弧&quot; =&amp;gt; 1
      &quot;ある程度&quot; =&amp;gt; 1
      &quot;法&quot; =&amp;gt; 14
      ⋮ =&amp;gt; ⋮
    
    julia&amp;gt; function count_word2(text::UTF8String)
             mecab = Mecab(&quot;-O wakati&quot;)
             counts = Collections.PriorityQueue()
             for word in split(sparse_tostr(mecab, text))
                 counts[word] = get(counts, word, 0) - 1
               end
             counts
           end
    count_word2 (generic function with 1 method)
    
    julia&amp;gt; @time count_word2(text)
    elapsed time: 0.891081099 seconds (24265472 bytes allocated, 20.83% gc time)
    PriorityQueue{Any,Any,ForwardOrdering} with 13583 entries:
      &quot;ウィキ&quot; =&amp;gt; -1
      &quot;TAKE&quot; =&amp;gt; -2
      &quot;null&quot; =&amp;gt; -4
      &quot;変革&quot; =&amp;gt; -5
      &quot;クソ&quot; =&amp;gt; -1
      &quot;228&quot; =&amp;gt; -3
      &quot;迫っ&quot; =&amp;gt; -1
      &quot;村山&quot; =&amp;gt; -1
      &quot;寺嶋&quot; =&amp;gt; -1
      &quot;リビング&quot; =&amp;gt; -1
      &quot;国籍&quot; =&amp;gt; -1
      &quot;ベーコン&quot; =&amp;gt; -1
      &quot;出す&quot; =&amp;gt; -13
      &quot;Core&quot; =&amp;gt; -5
      &quot;当選&quot; =&amp;gt; -2
      &quot;moguno&quot; =&amp;gt; -1
      &quot;Brainfuck&quot; =&amp;gt; -1
      &quot;積ん&quot; =&amp;gt; -4
      &quot;backup&quot; =&amp;gt; -2
      &quot;stress&quot; =&amp;gt; -1
      &quot;Qw&quot; =&amp;gt; -1
      &quot;細かい&quot; =&amp;gt; -3
      &quot;従って&quot; =&amp;gt; -1
      &quot;括弧&quot; =&amp;gt; -1
      &quot;ある程度&quot; =&amp;gt; -1
      &quot;法&quot; =&amp;gt; -14
      ⋮ =&amp;gt; ⋮&lt;/file&gt;&lt;/pre&gt;
    
    
    &lt;p&gt;型と多重dispatchがある分、なんでも同じようにできるわけではないこと、そしてそれをやるのが本当に最適手なのかを考えることができました。
    なお、julia-usersは気軽に質問できてどんどん斧が飛んできて楽しいので、みなさんも読むことをおすすめします！&lt;/p&gt;
    
    &lt;p&gt;明日はkimrinさんによるJuliaで楽器を作ろう！です。楽しみですね。&lt;/p&gt;
    &lt;div class=&quot;footnote&quot;&gt;
    &lt;p class=&quot;footnote&quot;&gt;&lt;a href=&quot;#fn-23bc65e3&quot; name=&quot;f-23bc65e3&quot; class=&quot;footnote-number&quot;&gt;*1&lt;/a&gt;&lt;span class=&quot;footnote-delimiter&quot;&gt;:&lt;/span&gt;&lt;span class=&quot;footnote-text&quot;&gt;本人のアイコン、バイキングの帽子をかぶっているのが有名ですよね&lt;/span&gt;&lt;/p&gt;
    &lt;/div&gt;
    &lt;/:real&gt;


