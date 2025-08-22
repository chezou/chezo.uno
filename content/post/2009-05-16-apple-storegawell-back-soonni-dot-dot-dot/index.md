---
authors: [aki]
categories: null
date: '2009-05-16 14:53:46-07:00'
draft: false
featured: false
image: {caption: '', focal_point: '', preview_only: false}
lastmod: '2009-05-16 14:53:46-07:00'
projects: []
subtitle: ''
summary: ''
tags: []
title: Apple storeがWe'll back soonに……
keywords: [マウント, volume, photo, nas, mac, 自動, 入手, それぞれ, 方法, 状態]
recommendations: [/post/2009-10-25-macdui-ying-siteinainasnopurintosabaji-neng-woshi-uniha/,
  /post/2009-05-31-linkstationnowebakusesutosimplify-music-2-at-iphone/, /post/2009-11-11-nas-navigator2wowindows7-64bit-dedong-kasufang-fa/]
---

もうすぐ、新型iPhoneだとかiPod touchの発表なんでしょうね。amazonでも32G touchが20000円引きで売られていることですし。

なぜ気づいたかって？Xcodeをダウンロードしようとしたら、メンテナンス中だったからだよ。iTunesStoreはXcodeの入手には必要なかったみたいです。そういえば、、、  
参考URL:[Mac OSX Build and Run! Xcodeの入手方法](http://lightchaos.blog10.fc2.com/blog-category-10.html)

今起きている問題は、Buffalo製のLS-C1.0TLに保存してあるiPhoto Libralyが不可視フォルダになって見えないということ。これにより、開けない状態になっているわけです。で、ターミナルを立ち上げて、dfをしてみると、どうもiPhoto Libralyが置いてあるディレクトリが複数あるわけです。

/Volume/photo  
/Volume/photo-1  
/Volume/photo-2  
で、それぞれ中を見てみると、無印と-1のところにはiPhoto Libralyのみ入っている状態。作成されているのがそれぞれ休みの日の夜中だから、もしかしたらNASがバックアップしている時にiPhotoを開いていて、変なことになったのかなぁ、とか勘ぐってみる物の原因は不明。

明日起きてから対処ですわ。

- 
  - 関連サイト--

[MacOSX 不可視ファイルの解除方法（&パスの通しかた） - WEB + PC[[Macでネットワークディスク（NAS）を自動マウントする方法｜BAMBOoのAppleでMacなiPhone徒然草](http://ameblo.jp/z9dz9d/entry-10149021737.html)  
もしかしたら、Nas navigator2を入れたときに自動マウント利用するようにしたのが悪いのかも。キーチェーンがおかしくて、大抵ゲストアカウントでマウントされてるし。