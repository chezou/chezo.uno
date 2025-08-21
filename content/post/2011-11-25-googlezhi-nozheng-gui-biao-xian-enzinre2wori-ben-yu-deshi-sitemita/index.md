---
title: Google製の正規表現エンジンRe2を日本語で試してみた
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: null
date: 2011-11-25 22:02:51+00:00
lastmod: 2011-11-25 22:02:51+00:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [正規表現, regex, マッチ, mercurial, unnonouno, ubuntu, '2011', インストール, 使い方, '11']
recommendations: [/post/2011-11-26-zheng-gui-biao-xian-raiburarire2nojian-dan-nashi-ifang-matome/,
  /post/2017-07-10_thinkpad-x1-carbon--2017--windows-10-ubuntu-17-04-----------9f73d89073c3/,
  /post/2019-11-25-github actions-issue template/]
---
C++で正規表現を使う時、boost::regexを使うことが多いと思っていたのですが、何故か1.46.1以降(といっても1.48.0しか試していませんが)、regex\_search,regex\_matchがNullPointerExceptionぽく落ちるので、解決方法を探していました。

そこで、試してみたのが[Google製の正規表現エンジン Re2](http://code.google.com/p/re2/)です。  
インストールは簡単です。Mercurialが必要ですが、Ubuntuではaptで簡単に入ります。(ちなみに、Ubuntu11.04で試しました)



[2011/11/28追記]  
もう少しだけ[詳しい使用例](https://chezo.uno/post/2011-11-26-zheng-gui-biao-xian-raiburarire2nojian-dan-nashi-ifang-matome)を書きました！

まず、入っていなければMercurialのインストールです。

```sh
sudo apt-get install mercurial
```

で、適当な所にre2をcloneして、インストールです。

```sh
hg clone https://re2.googlecode.com/hg re2 
cd re2
make test
sudo make install
make test install
```

で、試してみたコードが以下のものになります。  

{{< gist chezou 1393431 >}}


```cpp
#include <iostream> 
#include <string>
#include <re2/re2.h>
#include <cassert>
using namespace std;

int main(int argc, char **argv){
  string s,t;
  string str("あぶらかたぶら");
  RE2 re1("(.ら).(.ぶ)");
  assert(re1.ok());
  
  if(RE2::PartialMatch(str, re1 , &s, &t))
    cout << "s:"<< s << " t:"<< t << endl;

  return 0;
}
```

出力結果はこうなりました。

```
s:ぶら t:たぶ
```

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
