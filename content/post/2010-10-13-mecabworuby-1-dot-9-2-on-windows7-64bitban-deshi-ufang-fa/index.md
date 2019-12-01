---
title: "MeCabをRuby 1.9.2 on Windows7(64bit版)で使う方法"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2010-10-13T21:59:53+00:00
lastmod: 2010-10-13T21:59:53+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
Windows7の開発環境を構築するに当たって、なんとなくRubyを1.8.7から1.9.2にしてみました。  
そしたら意外とx64でMeCabを使えるようになるまでにハマったのでメモしておきます。  
Makefileとかよく分からないなりに頑張ったのですが、かなりいい加減だと思います。

方針としては、libmecab.dllをx64環境でコンパイルしなおして、次のサイトを参考にしてmecab.rbを作ります。(ついでに、元々の[言語処理関連のプログラム類](http://nlp.sfc.keio.ac.jp/%7Eaihara/nlp.html) で実装されていたsparse\_tonode(str)も使えるようにさせていただきました。ありがとうございます！ )  
[Windowsのrubyでmecab | アッセんぶら　困ぱいる](http://kitykey.jugem.jp/?eid=21)

1. Windows版のMeCabをとりあえず入れておく。
2. MeCabのソースを入手し、展開する。
3. src以下にある、mecab.h, feaure\_index.cpp, wrier.cpp, Makefile.msvc.inを修正する  
mecab.h  
・254行目　#ifndef SIWG → #ifndef SWIG  
・257行目 #endif を 260行目の};の前の行に挿入feaure\_index.cpp  
・311行目 case &#39;t&#39;:&amp;nbsp; os\_ \&lt;\&lt; (size\_t)path-\&gt;rnode-\&gt;char\_type;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; break;  
→ case &#39;t&#39;:&amp;nbsp; os\_ \&lt;\&lt; (unsigned int)path-\&gt;rnode-\&gt;char\_type;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; break;wrier.cpp  
・236行目 case &#39;L&#39;: \*os \&lt;\&lt; std::strlen(sentence); break;  
→ case &#39;L&#39;: \*os \&lt;\&lt; (unsigned int)std::strlen(sentence); break;

Makefile.msvc.in → Makefile.msvcにファイル名変更  
・5行目 /MACHINE:X86 → /MACHINE:X64  
・7行目、8行目

  - DDIC\_VERSION=@DIC\_VERSION@→ -DDIC\_VERSION=102
  - DVERSION=”\”@VERSION@”\”&quot; →&amp;nbsp; -DVERSION=“\”0.98″\”&quot;

2011/01/11追記:  
Visual Studio 2010ではcommon.hに #include &lt;iterator&gt;を追加する必要があるそうです。&lt;br&gt;
詳しくは&lt;a href=&quot;http://blogs.msdn.com/b/vcblog/archive/2009/05/25/stl-breaking-changes-in-visual-studio-2010-beta-1.aspx&quot;&gt;こちら&lt;/a&gt;を参照(Thanks to id:&lt;a href=&quot;http://b.hatena.ne.jp/mayuki/&quot;&gt;mayuki&lt;/a&gt;さん！)&lt;/iterator&gt;

  
4. Visual Studio 2008 x64 Cross Tool コマンドプロンプトでnmake
  
5. できたlibmecab.dllをlibmecab64.dllなど適当な名前にして、libmecab.dllと同じフォルダに移動
  
6. [Windowsのrubyでmecab | アッセんぶら　困ぱいる](http://kitykey.jugem.jp/?eid=21) と[言語処理関連のプログラム類](http://nlp.sfc.keio.ac.jp/%7Eaihara/nlp.html)を参考にしてmecab.rbを作成
  

    # -\*- coding: windows-31j -\*-require &quot;dl/import&quot;require &quot;dl/struct&quot;module MecabFuncextend DL::Importer dlload &#39;libmecab64.dllの場所&#39; typealias(&#39;size\_t&#39;, &#39;unsigned long&#39;) extern &quot;mecab\_t\* mecab\_new2(const char\*)&quot; extern &quot;const char\* mecab\_version()&quot; extern &quot;const char\* mecab\_sparse\_tostr(mecab\_t\*, const char\*)&quot; extern &quot;const char\* mecab\_strerror(mecab\_t\*)&quot; extern &quot;void mecab\_destroy(mecab\_t \*)&quot;endmodule MecabLibclass Mecabinclude MecabFunc@mecab=nildef initialize(args) @mecab=MecabFunc.mecab\_new2(args) enddef version() MecabFunc.mecab\_version() enddef strerror() MecabFunc.mecab\_strerror(@mecab) enddef sparse\_tostr(str) MecabFunc.mecab\_sparse\_tostr(@mecab,str) enddef sparse\_tonode(str) #http://nlp.sfc.keio.ac.jp/~aihara/nlp.html でのaihara氏の実装です。 prev=nil head=Node.new() tmp\_str= &quot;#{sparse\_tostr(str)}&quot; tmp\_str.split(&quot;\n&quot;).each{|line| buf=Node.new(line,prev) if prev!=nil prev.next=buf end prev=buf if head.next==nil head.next=buf end } head enddef destroy() MecabFunc.mecab\_destroy(@mecab) endclass Node@prev=nil@next=nil@surface=nil#形態素の表記@pos=nil#品詞@root=nil#原形@reading=nil#読み@pronunciation=nil#発音attr\_accessor :prev,:next,:surface,:pos,:root,:reading,:pronunciationdef initialize(line=nil,prev=nil) @prev=prev if line != nilif line == &quot;EOS&quot;#EOSの時@surface=line @pos=&quot;EOS&quot;@root=&quot;EOS&quot;@reading=&quot;EOS&quot;@pronunciation=&quot;EOS&quot;else#それ以外 linels=line.split(&quot;\t&quot;) @surface=linels[0] fetls=linels[1].split(&quot;,&quot;) @pos=fetls[0..5].join(&quot;,&quot;) if fetls[6]==nil@root=&quot;&quot;else@root=fetls[6] endif fetls[7]==nil@reading=&quot;&quot;else@reading=fetls[7] endif fetls[8]==nil@pronunciation=&quot;&quot;else@pronunciation=fetls[8] endendendenddef hasNext() if @next==nilfalseelsetrueendendendendend

mecab.rbの名前をmecab64.rbとでもつけます。実際に呼ぶときは、RUBY\_VERSIONで切り替えたりしています。

    # -\*- coding: windows-31j -\*-require &quot;mecab64&quot;m = MecabLib::Mecab.new(&quot;&quot;) puts m.version puts m.sparse\_tostr(&quot;本日は晴天なり。&quot;) node = m.sparse\_tonode(&quot;本日は晴天なり。&quot;)while node.hasNext node = node.next print node.surface + &quot; : &quot; + node.pos + &quot; : &quot; + node.root + &quot; : &quot; + node.reading + &quot; : &quot; + node.pronunciation + &quot;\n&quot;end

とすると、次のような結果が出るはずです。

&gt; 0.98  
&gt; 本日&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; 名詞,副詞可能,\*,\*,\*,\*,本日,ホンジツ,ホンジツ  
&gt; は&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; 助詞,係助詞,\*,\*,\*,\*,は,ハ,ワ  
&gt; 晴天&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; 名詞,一般,\*,\*,\*,\*,晴天,セイテン,セイテン  
&gt; なり&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; 助動詞,\*,\*,\*,文語・ナリ,基本形,なり,ナリ,ナリ  
&gt; 。&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; 記号,句点,\*,\*,\*,\*,。,。,。  
&gt; EOS  
&gt; 本日 : 名詞,副詞可能,\*,\*,\*,\* : 本日 : ホンジツ : ホンジツ  
&gt; は : 助詞,係助詞,\*,\*,\*,\* : は : ハ : ワ  
&gt; 晴天 : 名詞,一般,\*,\*,\*,\* : 晴天 : セイテン : セイテン  
&gt; なり : 助動詞,\*,\*,\*,文語・ナリ,基本形 : なり : ナリ : ナリ  
&gt; 。 : 記号,句点,\*,\*,\*,\* : 。 : 。 : 。  
&gt; EOS : EOS : EOS : EOS : EOS

$

