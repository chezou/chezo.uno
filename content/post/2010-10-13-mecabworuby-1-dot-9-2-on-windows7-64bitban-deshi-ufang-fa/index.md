---
authors: [aki]
categories: null
date: '2010-10-13 14:59:53-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2010-10-13 14:59:53-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: MeCabをRuby 1.9.2 on Windows7(64bit版)で使う方法
keywords: [mecab, 本日, dll, cpp, break, 名詞, makefile, libmecab, case, '64']
recommendations: [/post/2018-12-01_windows-64bit-mecab--kytea-------2018-b283b6c7b33c/,
  /post/2014-12-06-japan-dot-rde-mecab-dot-jltukututemita-wofa-biao-sitekita-number-juliaac-number-japanr/,
  /post/2019-11-29-mecab-python3/]
---

Windows7の開発環境を構築するに当たって、なんとなくRubyを1.8.7から1.9.2にしてみました。  
そしたら意外とx64でMeCabを使えるようになるまでにハマったのでメモしておきます。  
Makefileとかよく分からないなりに頑張ったのですが、かなりいい加減だと思います。

方針としては、libmecab.dllをx64環境でコンパイルしなおして、次のサイトを参考にしてmecab.rbを作ります。(ついでに、元々の[言語処理関連のプログラム類](http://nlp.sfc.keio.ac.jp/%7Eaihara/nlp.html) で実装されていたsparse_tonode(str)も使えるようにさせていただきました。ありがとうございます！ )  
[Windowsのrubyでmecab | アッセんぶら　困ぱいる](http://kitykey.jugem.jp/?eid=21)

1. Windows版のMeCabをとりあえず入れておく。
2. MeCabのソースを入手し、展開する。
3. src以下にある、mecab.h, feaure_index.cpp, wrier.cpp, Makefile.msvc.inを修正する  
mecab.h  
・254行目　`#ifndef SIWG` → `#ifndef SWIG`  
・257行目 `#endif` を 260行目の`};`の前の行に挿入 feaure_index.cpp  
・311行目 `case 't':  os_ \<\< (size_t)path-\>rnode-\>char_type;     break;`  
→ `case 't':  os_ \<\< (unsigned int)path-\>rnode-\>char_type;     break;` wrier.cpp  
・236行目 `case 'L': \*os \<\< std::strlen(sentence); break;`  
→ `case 'L': \*os \<\< (unsigned int)std::strlen(sentence); break;`

Makefile.msvc.in → Makefile.msvcにファイル名変更  
・5行目 `/MACHINE:X86` → `/MACHINE:X64`  
・7行目、8行目

  - `DDIC_VERSION=@DIC_VERSION@` → - `DDIC_VERSION=102`
  - `DVERSION=”\”@VERSION@”\”"` →  - `DVERSION=“\”0.98″\”"`

2011/01/11追記:  
Visual Studio 2010ではcommon.hに #include <iterator>を追加する必要があるそうです。<br>
詳しくは<a href="http://blogs.msdn.com/b/vcblog/archive/2009/05/25/stl-breaking-changes-in-visual-studio-2010-beta-1.aspx">こちら</a>を参照(Thanks to id:<a href="http://b.hatena.ne.jp/mayuki/">mayuki</a>さん！)</iterator>

  
4. Visual Studio 2008 x64 Cross Tool コマンドプロンプトでnmake
  
5. できたlibmecab.dllをlibmecab64.dllなど適当な名前にして、libmecab.dllと同じフォルダに移動
  
6. [Windowsのrubyでmecab | アッセんぶら　困ぱいる](http://kitykey.jugem.jp/?eid=21) と[言語処理関連のプログラム類](http://nlp.sfc.keio.ac.jp/%7Eaihara/nlp.html)を参考にしてmecab.rbを作成
  
```rb
# -*- coding: windows-31j -*-
require "dl/import"
require "dl/struct"

module MecabFunc
  extend DL::Importer
  dlload 'libmecab64.dllの場所' 
  typealias('size_t', 'unsigned long')
  extern "mecab_t\* mecab_new2(const char\*)"
  extern "const char\* mecab_version()"
  extern "const char\* mecab_sparse_tostr(mecab_t\*, const char\*)"
  extern "const char\* mecab_strerror(mecab_t\*)"
  extern "void mecab_destroy(mecab_t \*)"
end

module MecabLib
  class Mecab
    include MecabFunc

    @mecab=nil

    def initialize(args)
      @mecab=MecabFunc.mecab_new2(args)
    end

    def version()
      MecabFunc.mecab_version()
    end

    def strerror()
      MecabFunc.mecab_strerror(@mecab)
    end

    def sparse_tostr(str)
      MecabFunc.mecab_sparse_tostr(@mecab,str)
    end

    def sparse_tonode(str)
      #http://nlp.sfc.keio.ac.jp/~aihara/nlp.html でのaihara氏の実装です。
      prev=nil
      head=Node.new()
      tmp_str= "#{sparse_tostr(str)}"
      tmp_str.split("\n").each{|line|
        buf=Node.new(line,prev)
        if prev!=nil
          prev.next=buf
        end
        prev=buf
        if head.next==nil
          head.next=buf
        end
      }
      head
    end

    def destroy()
      MecabFunc.mecab_destroy(@mecab)
    end

      class Node
        @prev=nil
        @next=nil
        @surface=nil #形態素の表記
        @pos=nil #品詞
        @root=nil #原形
        @reading=nil #読み
        @pronunciation=nil #発音
        attr_accessor :prev,:next,:surface,:pos,:root,:reading,:pronunciation

        def initialize(line=nil, prev=nil)
          @prev=prev if line != nil
          if line == "EOS" #EOSの時
            @surface=line
            @pos="EOS"
            @root="EOS"
            @reading="EOS"
            @pronunciation="EOS"
          else #それ以外
          linels=line.split("\t")
          @surface=linels[0]
          fetls=linels[1].split(",")
          @pos=fetls[0..5].join(",")
          if fetls[6]==nil
            @root=""
          else
            @root=fetls[6]
          end
          if fetls[7]==nil
            @reading=""
          else
            @reading=fetls[7]
          end
          if fetls[8]==nil
            @pronunciation=""
          else
            @pronunciation=fetls[8] end
          end
        end
      end

      def hasNext()
        if @next==nil
          false
        else
          true
        end
      end
    end
  end
end
```

mecab.rbの名前をmecab64.rbとでもつけます。実際に呼ぶときは、RUBY_VERSIONで切り替えたりしています。

```rb
# -*- coding: windows-31j -*-
require "mecab64"
m = MecabLib::Mecab.new("")
puts m.version
puts m.sparse_tostr("本日は晴天なり。")
node = m.sparse_tonode("本日は晴天なり。")
while node.hasNext
  node = node.next
  print node.surface + " : " + node.pos + " : " + node.root + " : " + node.reading + " : " + node.pronunciation + "\n"
end
```

とすると、次のような結果が出るはずです。

> 0.98  
> 本日        名詞,副詞可能,\*,\*,\*,\*,本日,ホンジツ,ホンジツ  
> は        助詞,係助詞,\*,\*,\*,\*,は,ハ,ワ  
> 晴天        名詞,一般,\*,\*,\*,\*,晴天,セイテン,セイテン  
> なり        助動詞,\*,\*,\*,文語・ナリ,基本形,なり,ナリ,ナリ  
> 。        記号,句点,\*,\*,\*,\*,。,。,。  
> EOS  
> 本日 : 名詞,副詞可能,\*,\*,\*,\* : 本日 : ホンジツ : ホンジツ  
> は : 助詞,係助詞,\*,\*,\*,\* : は : ハ : ワ  
> 晴天 : 名詞,一般,\*,\*,\*,\* : 晴天 : セイテン : セイテン  
> なり : 助動詞,\*,\*,\*,文語・ナリ,基本形 : なり : ナリ : ナリ  
> 。 : 記号,句点,\*,\*,\*,\* : 。 : 。 : 。  
> EOS : EOS : EOS : EOS : EOS