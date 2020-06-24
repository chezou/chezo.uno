---
title: "Google製の正規表現エンジンRe2を日本語で試してみた"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2011-11-25T22:02:51+00:00
lastmod: 2011-11-25T22:02:51+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
C++で正規表現を使う時、boost::regexを使うことが多いと思っていたのですが、何故か1.46.1以降(といっても1.48.0しか試していませんが)、regex\_search,regex\_matchがNullPointerExceptionぽく落ちるので、解決方法を探していました。

そこで、試してみたのが[Google製の正規表現エンジン Re2](http://code.google.com/p/re2/)です。  
インストールは簡単です。Mercurialが必要ですが、Ubuntuではaptで簡単に入ります。(ちなみに、Ubuntu11.04で試しました)

[2011/11/28追記]  
もう少しだけ[詳しい使用例](http://chezou.wordpress.com/2011/11/26/%e6%ad%a3%e8%a6%8f%e8%a1%a8%e7%8f%be%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aare2%e3%81%ae%e7%b0%a1%e5%8d%98%e3%81%aa%e4%bd%bf%e3%81%84%e6%96%b9%e3%81%be%e3%81%a8%e3%82%81/ "正規表現ライブラリre2の簡単な使い方まとめ")を書きました！

    まず、入っていなければMercurialのインストールです。
    
        sudo apt-get install mercurial
    
    
    
    で、適当な所にre2をcloneして、インストールです。
    
    
    
        hg clone https://re2.googlecode.com/hg re2 cd re2 make test sudo make install make testinstall
    
    
    
    で、試してみたコードが以下のものになります。  
    [gist:1393431](https://gist.github.com/1393431 "gist:1393431")
    
    
    
        #include \<iostream\> #include \<string\> #include \<re2/re2.h\> #include \<cassert\> using namespace std;int main(int argc, char \*\*argv){ string s,t; string str("あぶらかたぶら"); RE2 re1("(.ら).(.ぶ)"); assert(re1.ok()); if(RE2::PartialMatch(str, re1 , &s, &t)) cout \<\< "s:"\<\< s \<\< " t:"\<\< t \<\< endl; return 0; }
    
    
    
    出力結果はこうなりました。
    
    
    
        s:ぶら t:たぶ
    
    
    
    勿論、部分マッチだけでなく、FullMatchやReplaceもできます。  
    ただ、可変数マッチしたものを全部取り出すのはやり方わからないんですよねー。  
    マッチした物をeachで取り出す的なことがしたいんですが。
    
    
    
    **[2011/11/26追記]**  
    PartialMatchNを利用すれば解決できると、[@unnonounoさん](https://twitter.com/#!/unnonouno)に教えていただきました！  
    ただ、結構トリッキーなので、下記記事中のサンプルコードを見るのが早いと思います。ありがとうございます！  
    [re2のxxxNの使い方:unnonouno](http://unnonouno.blogspot.com/2011/11/re2xxxn.html)
    
    
    
    exampleは[re2.h](http://code.google.com/p/re2/source/browse/re2/re2.h)にたくさんあるので参考にしてください。
    
    
    
    とりあえず、正規表現だけ欲しければre2を使ってみるのもよいかもしれません。
    

参考URL:  
[Re2の使い方と疑問](http://blog.broomie.net/?id=43)  
[RE2を試してみた。](http://d.hatena.ne.jp/tkuro/20100317/1268807785)
