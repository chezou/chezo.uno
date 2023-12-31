---
title: 2023年を振り返って
subtitle: ''
summary: ''
authors: [aki]
tags: []
categories: [misc]
date: 2023-12-31 01:00:00-07:00
lastmod: 2023-12-31 01:00:00-07:00
featured: false
draft: false
image: {caption: '', focal_point: '', preview_only: false}
projects: []
keywords: [vancouver, post, social, 仕事, プロジェクト, あと, コールセンター, chezo, cad, accent]
recommendations: [/post/2022-12-30-2022-year-in-review/, /post/2021-12-18-8-months-after-relocating-vancouver/,
  /post/2023-04-05-first-time-skiing-in-25-years/]
---

今年もあと一日になりましたが、[昨年同様](https://chezo.uno/post/2022-12-30-2022-year-in-review/)一年を振り返っていきたいと思います。

## OSS活動・対外活動

ChromaというVector DBのOSSにコントリビュートしました。ChromaはRAGやLLMの文脈でよく使われるもののようです。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chroma-core/chroma/pull/1361" data-iframely-url="//iframely.net/Zj8hyr9?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

tabula-pyの裏側にjpype経由で使うようにして速くしたのですが、残念なことに Python 3.12 サポートがかなり時間がかかったので今はoptionalにしています。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://chezo.uno/blog/2023-09-09-tabula-py-280/" data-iframely-url="//iframely.net/f64jYQx"></a></div></div><script async src="//iframely.net/embed.js"></script>


また、tabula-pyの質問はStackOverflowに流していたのですが、[moderatorの気分でGitHub issue作ってねという文言が消される](https://meta.stackoverflow.com/questions/426607/is-it-forbidden-to-suggest-to-create-an-github-issue-discussion-for-other-proble/426610)ということが分かったので、今までの感謝とともにGitHub Discussionsに移行しました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/tabula-py/discussions" data-iframely-url="//iframely.net/PIG05ED?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

<br/>

あとは、NotionをscrapingしてPDFにするやつなんかも作りました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://github.com/chezou/vangohan-pdf" data-iframely-url="//iframely.net/cP0eFmn?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

<br/>


RubyKaigi 2023にもただの参加者としてですが参加できたので、その様子をバンクーバーのえんじに屋podcastでお話させていただきました。

https://www.vancouver-engineers.com/133

<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/CsLEfZ0P-0N/?utm_source=ig_embed&utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/p/CsLEfZ0P-0N/?utm_source=ig_embed&utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/CsLEfZ0P-0N/?utm_source=ig_embed&utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Aki Ariga (@chezo.uno)</a></p></div></blockquote>
<script async onerror="var a=document.createElement('script');a.src='https://iframely.net/files/instagram_embed.js';document.body.appendChild(a);" src="https://www.instagram.com/embed.js"></script>

また、Frogさんでキャリアのインタビューもしてもらいました。行き当たりばったりなキャリア経験ではありますが、きれいにまとめていただきました。

<div class="iframely-embed"><div class="iframely-responsive" style="height: 140px; padding-bottom: 0;"><a href="https://frogagent.com/interview/ariga/" data-iframely-url="//iframely.net/yH4K5NE?card=small"></a></div></div><script async src="//iframely.net/embed.js"></script>

## 仕事

昨年炎上プロジェクトに投入されて火消しをするも、いろいろあってぽしゃり、そしてまた、別の炎上プロジェクトに投入されてそちらはなんとかかんとか生き延びている、という状況です。突っ込まれてから、4カ月後の社外カンファレンスでデモまでこぎつけられたのは、ML系プロジェクトだからだなぁという良い経験をさせていただきました。6 pageのレポート作成からのexecutiveの説得、UX設計、PRD議論、アーキテクチャ設計、実装、他のエンジニアリングチームのとりまとめとまあ全部やりました。

最近の悩みは、クオーターごとに実装期間がほぼ1週間くらいしかないことでしょうか。楽しい時間は一瞬で過ぎ去ってしまう。。。soft skillを生かして仕事では動いていますが、やはりhard skillも伸ばしておかないと上流だけしかできないのね、と言われてしまうのが怖いです。スタッフ+としてどう生きていくのがいいのだろうか。副業などで手を動かす仕事をやりたいものです。

社内ハッカソンで、RAG (retrieval augmented generation)のアプリを作りました。[terapyon podcastで聞いていたおかげで](https://podcast.terapyon.net/) [Gradio](https://www.gradio.app/)を使い、さくっとデモアプリまで行けました。なお、RAGは短文で検索するときの検索性能が全然でないため、OOBじゃ全然使えないということも学びました。しかし、検索と推薦は楽しいですねぇ。

## プライベート

PRカードをついに手に入れました。永住権自体は昨年末に得ていたのですが、物理カードを得たので、これでビザ的には一番安心できる状況ですし、海外旅行も行けます。あと、海外の会社で働くのも楽になりました。

スキーを20年ぶりに再開してドはまりしています。ujihisaさんと何度も滑りに行ってますがローカルの山まで30分、Whistlerまで2時間なので更に滑りまくりたいです。今年はエルニーニョ現象のため、雪が全然なくてつらいです。パラレルをちゃんとものにしていきたい。

<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/C1Xt0P6yMRV/?utm_source=ig_embed&utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/p/C1Xt0P6yMRV/?utm_source=ig_embed&utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/C1Xt0P6yMRV/?utm_source=ig_embed&utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Aki Ariga (@chezo.uno)</a></p></div></blockquote>
<script async onerror="var a=document.createElement('script');a.src='https://iframely.net/files/instagram_embed.js';document.body.appendChild(a);" src="https://www.instagram.com/embed.js"></script>

あと、忘れもしないのは銀行のコールセンターに [accent discrimination](https://www.forbes.com/sites/janicegassam/2022/11/18/accent-discrimination-is-still-a-pervasive-issue-in-the-workplace-research-finds/?sh=46859d85697e) を受けたこと。Scotiabankという銀行を移住時に開設したのですが、全国一律のコールセンターの人に英語わからない認定を食らって[バトルしました](https://sizu.me/chezou/posts/a811we9eha27)。上司が出てきて謝罪をもらったんですが、そういう銀行を使うのは癪なので、TDに移行してすべてうまくいっています。1Passwordで自社名とconflictすることくらいがネックなだけです。なお、ショックだったのは、某日本人コミュニティで「あなたの考えすぎじゃないですか」というセカンドレイプを受けたことでした。 unconscious biasのトレーニングを会社で受けていてよかったなと思った瞬間です。

転んでもただは起きぬということで、[American English accentのレッスン](https://rachelsenglish.com/)を受けるようになりました。理屈より実践という感じの手法なのですが、なるほど実際そうするのねーというのが身についてきて、けだるい英語のリスニングができるようになった気がしています。

12月を丸っと休みにしたのですが、家族が次々と怪我をして看護休暇として追われています。ずっとワンオペで子供と犬の世話をしている日々なので、ゆっくりとした休みが欲しいなあと思う次第です。

## 振り返りと来年に向けて

今年は、いろいろと迷いの多い一年だったように思います。来年は40の大台に乗るので、仕事方面は人生で一回くらいプロモーションしていきたいなと思いますし、プライベートは英語とスキーを上達したいと思っています。

中長期的には、Greator Vancouverで家を買うには大体 1M CADが必要なのですが、その頭金として300K CADを貯めればいいことが分かったので、何とかしていきたいと思います。手っ取り早いのは、スタートアップで一発当てて$1M手に入れるか、big techに入って高給取りになることなんですが、まずは地道に貯めていこうかなと思います。

2年半バンクーバーエリアに住んでみてわかったのは、家賃上昇が激しく（Vancouver cityは2023年12月で[平均2BR $4300, 3BR $6200](https://www.zumper.com/rent-research/vancouver-bc)）living costはめちゃくちゃ高いわりに仕事があまりない（シニア以上はシアトルはじめUSに人が流れてしまうのが定番）という現状なんですが、医療費がかからない、スキーに行きやすいなどのメリットとの天秤でまだこの地にとどまることになると思います。が、平均年収$59Kの国で$100K超えの年収がないと一人暮らしできないVancouverやTrontoは異常なので、職があればAlbertaなどに行くのが良いんだろうなぁ。

Social media関連は色々と整理したり[^social]展開しなおしたりしたのですが、人と話すことで刺激を得たいと思っているので、Vancouver近辺にいらした際にはお声がけください。もちろん、近隣にお住いの皆さんは引き続きよろしくお願いいたします。

[^social]: 某toxicな持ち主のプラットフォームからは完全撤退しました