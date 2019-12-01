---
title: "正規表現ライブラリre2の簡単な使い方まとめ"
subtitle: ""
summary: ""
authors: [aki]
tags: []
categories: 
date: 2011-11-26T22:02:56+00:00
lastmod: 2011-11-26T22:02:56+00:00
featured: false
draft: false

image:
  caption: ""
  focal_point: ""
  preview_only: false

projects: []
---
先日、[インストールして試してみた](http://chezou.wordpress.com/2011/11/25/google%e8%a3%bd%e3%81%ae%e6%ad%a3%e8%a6%8f%e8%a1%a8%e7%8f%be%e3%82%a8%e3%83%b3%e3%82%b8%e3%83%b3re2%e3%82%92%e6%97%a5%e6%9c%ac%e8%aa%9e%e3%81%a7%e8%a9%a6%e3%81%97%e3%81%a6%e3%81%bf%e3%81%9f/ &quot;Google製の正規表現エンジンRe2を日本語で試してみた&quot;)Google製正規表現エンジン[re2](http://code.google.com/p/re2/)。

シンプルな使い方は、前の記事を見ていただければ分かると思うのですが、色々やってみようと思った時に、意外と独特の癖があってやりたいことをやるのに少し手間取ったので、メモがてらまとめておきます。  
本家の[ドキュメント](http://code.google.com/p/re2/wiki/CplusplusAPI)は思ったよりあっさりしていて、基本的には[ヘッダーにあるサンプル](http://code.google.com/p/re2/source/browse/re2/re2.h)を見るのが良いのですが、それもいまいちわかりにくいところがあったので、[テストコード](http://code.google.com/p/re2/source/browse/re2/testing/re2_test.cc)を見ながら試したことを書きます。詳細が知りたい人はテストコード見た方が早いかもしれません。

**[2011/11/28追記]**  
 **Windows Visual Studio向けのforkがでたようです。これでVisual Studio使いの人も安心ですね！**  
 **[re2win](http://code.google.com/p/re2win/)**

**[2011/12/03追記]**  
**re2winは日本語の文字列をマッチングさせようとしても、Invalid UTF-8とエラーがでてしまいます。**  
**どうやら内部で文字列がUTF-8であることを期待しているようです。文字コード変換をしないといけません。**

gistにも[コード](https://gist.github.com/1395527)を置きました。

### お品書き

1. FullMatch:文全体にマッチするかを判定
2. PartialMatch:文の一部分にマッチするかを判定
3. PartialMatchN:特に部分マッチした文字列を取得したい時に
4. FindAndConsume:部分マッチする文字列を繰り返し取得したい時に
5. Replace:パターンにマッチする最初の文字列を一置換
6. GlobalReplace:パターンにマッチする全ての文字列を置換
7. Extract:マッチする文字列を抽出して利用したい時に
8. サンプルコード

### 0.はじめに
re2を扱う上で知っておいた方が良さそうなポイントです。
- 後方参照に対応していない
- Unicode文字列にも対応している
- 対応している(していない)シンタックスは[ここにある](http://code.google.com/p/re2/wiki/Syntax)
後方参照については以下のように書いてありました。

&gt; RE2 supports submatch extraction, but not backreferences.
&gt; 
&gt; If you absolutely need backreferences and generalized assertions, then RE2 is not for you, but you might be interested in [irregexp](http://blog.chromium.org/2009/02/irregexp-google-chromes-new-regexp.html), Google Chrome&#39;s regular expression engine.  
&gt; ( from [http://code.google.com/p/re2/](http://code.google.com/p/re2/) )

ここで言う後方参照とは、&quot;(.n)\1&quot;というパターンで&quot;anan&quot;という文字列にマッチさせるというように、マッチした文字列を使ってパターンを作りたいという場合の事だと思います。単にgroupにマッチする文字列を抽出するだけならば可能です。  
また、どういうシンタックスが使えるかは確認しておくと良いと思います。
### 1.FullMatch:文全体にマッチするかを判定(boost::regex\_match)
FullMatchという関数で、あるパターンが一文全体にマッチするかを判定します。  
マッチすればtrueを返し、groupを作っていれば引数として用意したstringやintにそのグループに該当する値を返します。

    string s,t; string str(&quot;あぶらかたぶら&quot;); re2::StringPiece input(str); re2::RE2 re(&quot;(.ら).(.ぶ)&quot;);if(re2::RE2::FullMatch(input, re , &amp;s, &amp;t)) cout \&lt;\&lt; &quot;s:&quot;\&lt;\&lt; s \&lt;\&lt; &quot; t:&quot;\&lt;\&lt; t \&lt;\&lt; endl;elsecout \&lt;\&lt; &quot;Not match.&quot; \&lt;\&lt; endl;if(re2::RE2::FullMatch(input, &quot;.(.ら).(.ぶ).&quot; , &amp;s, &amp;t)) cout \&lt;\&lt; &quot;s:&quot;\&lt;\&lt; s \&lt;\&lt; &quot; t:&quot;\&lt;\&lt; t \&lt;\&lt; endl;elsecout \&lt;\&lt; &quot;Not match.&quot; \&lt;\&lt; endl;

出力結果は以下のようになります。

    Not match. s:ぶら t:たぶ

### 2.PartialMatch:文の一部分にマッチするかを判定(boost::regex\_search)
先ほどは、一つの文字列全体を考慮したパターンを考えましたが、今回は部分文字列で一致すればOKという関数です。

     string s,t; string str(&quot;あぶらかたぶら&quot;); re2::StringPiece input(str); re2::RE2 re(&quot;(.ら).(.ぶ)&quot;); if(re2::RE2::PartialMatch(input, re , &amp;s, &amp;t)) cout \&lt;\&lt; &quot;s:&quot;\&lt;\&lt; s \&lt;\&lt; &quot; t:&quot;\&lt;\&lt; t \&lt;\&lt; endl;

出力結果は以下のようになります。

    s:ぶら t:たぶ

### 3.PartialMatchN:特に部分マッチした文字列を取得したい時に
今までのやり方だとマッチしたかを判定することに重きを置いていて、取得した文字列を後から利用したい時には必要な数だけ変数を用意しなければならず、統一的に扱いづらいという問題があります。

そこで、任意の数のgroupを取得したい場合には、PartialMatchNを使います。  
(なお、全文一致の場合はFullMatchNになります。以降の関数にもXXXXNという物が存在することが多いようです)

このやり方は[@unnonouno](http://twitter.com/unnonouno)さんに教えていただいた方法です。[@unnnonounoさんの記事](http://unnonouno.blogspot.com/2011/11/re2xxxn.html)も参考にしてください。(教えていただきありがとうございます！)

     string str(&quot;abcadca&quot;); re2::RE2 re(&quot;((a.)(..))&quot;); re2::StringPiece input(str); int groupSize = re.NumberOfCapturingGroups(); vector\&lt;re2::RE2::Arg\&gt; argv(groupSize); vector\&lt;re2::RE2::Arg\*\&gt; args(groupSize); vector\&lt;re2::StringPiece\&gt; ws(groupSize); for (int i = 0; i \&lt; groupSize; ++i) { args[i] = &amp;argv[i]; argv[i] = &amp;ws[i]; } re2::RE2::PartialMatchN(input, re, &amp;(args[0]), groupSize); cout \&lt;\&lt; groupSize \&lt;\&lt; endl; string s; for (int i = 0; i \&lt; groupSize; ++i){ cout \&lt;\&lt; ws[i] \&lt;\&lt; endl;

出力結果

    3 abca ab ca

### 4.FindAndConsume:部分マッチする文字列を繰り返し取得したい時に(boost::regex\_regex相当？)
パターンにマッチしている文字列が何回出てくるか分からない場合に、この関数を利用するといいと思います。

    string str(&quot;あぶらかたぶら&quot;); RE2 re(&quot;(.ぶ)&quot;); re2::StringPiece input(str); string r;while(re2::RE2::FindAndConsume(&amp;input, re, &amp;r) ){ cout \&lt;\&lt; r \&lt;\&lt; endl; }

出力結果

    あぶ たぶ

### 5.Replace:パターンにマッチする最初の文字列を一置換(boost::regex\_replace)
パターンに一致した文字列のうち、最初に出てきた文字列のみを置換する場合、Replaceを使います。  
全てのマッチする文字列を置換したい場合は、GlobalReplaceを使います。

    string s = &quot;PerlRubyPython&quot;; re2::RE2::Replace(&amp;s, &quot;P&quot;, &quot;D&quot;); cout \&lt;\&lt; s \&lt;\&lt; endl;

出力結果

    DerlRubyPython

### 6.GlobalReplace:パターンにマッチする全ての文字列を置換
Replaceの全ての文字列を置換する場合です。  
ただし、文字列&quot;banana&quot;に対するパターン&quot;ana&quot;のようにオーバーラップする場合は対応しません。  
この場合は、一回のみマッチするようです。

    string s = &quot;PerlRubyPython&quot;; re2::RE2::GlobalReplace(&amp;s, &quot;P&quot;, &quot;D&quot;); cout \&lt;\&lt; s \&lt;\&lt; endl;

出力結果

    DerlRubyDython

### 7.Extract:マッチする文字列を抽出して利用したい時に
Replaceはどちらかというと、入力された文字列の一部を変える時が多いと思いますが、  
Extractはマッチしたgroupを抽出して、新たに文字列を生成したい場合に使える関数です。

    string s; RE2::Extract(&quot;foo@bar.com&quot;, &quot;(.\*)@([^.]\*)&quot;, &quot;In domain \&quot;\\2\&quot;, user \&quot;\\1\&quot; is exist!&quot;, &amp;s); cout \&lt;\&lt; s \&lt;\&lt; endl;

出力結果

    In domain &quot;bar&quot;, user &quot;foo&quot; is exist!

### サンプルコード
上記全部の例を含んだサンプルコードはこんな形になります。[gist](https://gist.github.com/1395527)にも同じ物があります。

コンパイルはこんな感じ。

    g++ -Wall re2testbasic.cpp -o re2all.out -lre2 -lpthread

ソースは以下。

    #include \&lt;iostream\&gt; #include \&lt;string\&gt; #include \&lt;re2/re2.h\&gt; #include \&lt;vector\&gt;using namespace std;void test\_fullmatch(){ string s,t; string str(&quot;あぶらかたぶら&quot;); re2::StringPiece input(str); re2::RE2 re(&quot;(.ら).(.ぶ)&quot;); if(re2::RE2::FullMatch(input, re , &amp;s, &amp;t)) cout \&lt;\&lt; &quot;s:&quot;\&lt;\&lt; s \&lt;\&lt; &quot; t:&quot;\&lt;\&lt; t \&lt;\&lt; endl; else cout \&lt;\&lt; &quot;Not match.&quot; \&lt;\&lt; endl; if(re2::RE2::FullMatch(input, &quot;.(.ら).(.ぶ).&quot; , &amp;s, &amp;t)) cout \&lt;\&lt; &quot;s:&quot;\&lt;\&lt; s \&lt;\&lt; &quot; t:&quot;\&lt;\&lt; t \&lt;\&lt; endl; else cout \&lt;\&lt; &quot;Not match.&quot; \&lt;\&lt; endl; }void test\_partialmatch(){ string s,t; string str(&quot;あぶらかたぶら&quot;); re2::StringPiece input(str); re2::RE2 re(&quot;(.ら).(.ぶ)&quot;); if(re2::RE2::PartialMatch(input, re , &amp;s, &amp;t)) cout \&lt;\&lt; &quot;s:&quot;\&lt;\&lt; s \&lt;\&lt; &quot; t:&quot;\&lt;\&lt; t \&lt;\&lt; endl; }void test\_partialmatchn(){ string str(&quot;abcadca&quot;); re2::RE2 re(&quot;((a.)(..))&quot;); re2::StringPiece input(str); int groupSize = re.NumberOfCapturingGroups(); vector\&lt;re2::RE2::Arg\&gt; argv(groupSize); vector\&lt;re2::RE2::Arg\*\&gt; args(groupSize); vector\&lt;re2::StringPiece\&gt; ws(groupSize); for (int i = 0; i \&lt; groupSize; ++i) { args[i] = &amp;argv[i]; argv[i] = &amp;ws[i]; } re2::RE2::PartialMatchN(input, re, &amp;(args[0]), groupSize); cout \&lt;\&lt; groupSize \&lt;\&lt; endl; string s; for (int i = 0; i \&lt; groupSize; ++i){ cout \&lt;\&lt; ws[i] \&lt;\&lt; endl; } }void test\_findandconsume(){ string str(&quot;あぶらかたぶら&quot;); RE2 re(&quot;(.ぶ)&quot;); re2::StringPiece input(str); string r; while(re2::RE2::FindAndConsume(&amp;input, re, &amp;r) ){ cout \&lt;\&lt; r \&lt;\&lt; endl; } }void test\_replace(){ string s = &quot;PerlRubyPython&quot;; re2::RE2::Replace(&amp;s, &quot;P&quot;, &quot;D&quot;); cout \&lt;\&lt; s \&lt;\&lt; endl; }void test\_globalreplace(){ string s = &quot;PerlRubyPython&quot;; re2::RE2::GlobalReplace(&amp;s, &quot;P&quot;, &quot;D&quot;); cout \&lt;\&lt; s \&lt;\&lt; endl; }void test\_extract(){ string s; RE2::Extract(&quot;foo@bar.com&quot;, &quot;(.\*)@([^.]\*)&quot;, &quot;In domain \&quot;\\2\&quot;, user \&quot;\\1\&quot; is exist!&quot;, &amp;s); cout \&lt;\&lt; s \&lt;\&lt; endl; }int main(int argc, char \*\*argv){ cout \&lt;\&lt; &quot;test FullMatch&quot; \&lt;\&lt; endl; test\_fullmatch(); cout \&lt;\&lt; &quot;test PartialMatch&quot; \&lt;\&lt; endl; test\_partialmatch(); cout \&lt;\&lt; &quot;test PartialMatchN&quot; \&lt;\&lt; endl; test\_partialmatchn(); cout \&lt;\&lt; &quot;test FindAndConsume&quot; \&lt;\&lt; endl; test\_findandconsume(); cout \&lt;\&lt; &quot;test Replace&quot; \&lt;\&lt; endl; test\_replace(); cout \&lt;\&lt; &quot;test GlobalReplace&quot; \&lt;\&lt; endl; test\_globalreplace(); cout \&lt;\&lt; &quot;test Extract&quot; \&lt;\&lt; endl; test\_extract(); return 0; }

出力結果

    test FullMatch Not match. s:ぶら t:たぶ test PartialMatch s:ぶら t:たぶ test PartialMatchN 3 abca ab ca test FindAndConsume あぶ たぶ test Replace DerlRubyPython test GlobalReplace DerlRubyDython test Extract

### おわりに
駆け足で説明したので、分かりにくい点や間違いがあるかと思います。  
その際には[@chezou](http://twitter.com/chezou)までご指摘いただければと思います。

後方参照さえ必要なければ、boostから乗り換えられるんじゃないかなーと思っています。

enjoy!

