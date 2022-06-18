---
title: homebrewを移動してiRubyが壊れたときに見直すポイント
description: 'kawasaki.rb #041 で得た知見です。'
date: '2016-10-29T13:50:25+09:00'
categories: [ruby]
authors: [aki]
keywords: [jupyter, iruby, ruby, ipython, 以下, register, force, kernel, 手順, usr]
recommendations: [/post/2016-07-12-jupyterkaraspark-clusterwocao-zuo-dekirulivy-plus-sparkmagicwoshi-sitemita/,
  /post/2015-01-11-dockershang-ninbviewerwoli-teteiruby-plus-nyaplotdemiao-itagurahuwogong-you-dekiruyounisitemita/,
  /post/2017-07-10_thinkpad-x1-carbon--2017--windows-10-ubuntu-17-04-----------9f73d89073c3/]
---

kawasaki.rb #041 で得た知見です。

/opt 以下から /usr/local 以下にhomebrewの場所を戻しました。理由はhomebrew caskが/optから/usr/localに移ったためなんですが、これに伴いrbenvで入れたirubyがopensslを/opt以下から探すようになってしまったため、壊れてしまいました。

いつもはjupyterでパーフェクトRubyの読み会をやっていたんですが、この日はこれを解決するのが間に合いませんでした。

で、このときにどうしたかというと、以下の記事に従って解決しました。

[**iruby (jupyter) でrubyのバージョンを切り替える手順 - Qiita**  
_iRuby(Jupyter上で動くruby)を利用する際にRubyのバージョンを切り替える手順について MacOS ElCapitan IRuby 0.2.9 jupyterにkernelとして登録されているirubyはjupyterに…_qiita.com](http://qiita.com/yohm13/items/46d9d5247b6e4f1e5164 "http://qiita.com/yohm13/items/46d9d5247b6e4f1e5164")[](http://qiita.com/yohm13/items/46d9d5247b6e4f1e5164)

iruby register --force  
jupyter kernelspec install  
iruby notebook

これで大丈夫です。  
実際には、僕は `iruby register --force` をやって、それを `/.ipython/kernels/ruby/kernel.json` にコピーしました。

困ったところとしては、ipythonからjupyterに名前が変わったので `~/.jupyter` 以下に何かおけばいいだろうと思って色々こねこねしてたんですが、結局大事なのは `~/.ipython` が重要でした。 `jupyter --paths` をやると `~/.jupyter` しかでてこないので騙されてしまいました。気をつけてください。