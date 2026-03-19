---
authors: [aki]
categories: []
date: 2018-12-15 22:06:00-08:00
description: この記事はpyspa Advenct calenderの17日目です。
lastmod: 2018-12-15 22:06:00-08:00
title: あなたの知らない煽りの世界
keywords: [コンピュータ, lib, 疑問, メッセージ, やりとり, 人間, pc, エンジニア, github, 連想]
recommendations: [/post/2025-09-19-review-fatigue/, /post/2014-01-24-kawasaki-dot-rb-number-008-wokai-cui-simasita-number-kwskrb/,
  /post/2018-10-25_risecamp------ee65c2ef0c9e/]
---


この記事は[pyspa Advenct calender](https://adventar.org/calendars/3018)の17日目です。

世の中にはAIを使ったchat botのような、高度なやりとりをするコンピュータが増えつつあります。コンピュータとやり取りすると人間はencourageされるのか？という疑問をお持ちの方もいるかと思いますが、そんな疑問を持つあなたはこの記事を読むことで、いかにコンピュータが人間の感情に対して働きかけてくれるかを学ぶでしょう。

それでは、ある日のエンジニアたちのチャットでのやりとりをお楽しみください。

Rのtest frameworkのtestthatの煽り力が高い

{{< figure src="1_PGBQH3d34YhCCfZ7XtTjSg.png" title="**Frustration is a natural part of programming :)**" >}}

ちぇぞーさんまた煽られてるの

なにこの機能ｗｗｗｗ  
Rすげぇな！  
テスト結果で煽りメッセージでるフレームワーク初めてみたよ！

っつうかさ、テスト結果レポータに煽りメッセージ入れるって発想すごくない？

バリエーションあるw

[**r-lib/testthat**  
_An R 📦 to make testing 😀. Contribute to r-lib/testthat development by creating an account on GitHub._github.com](https://github.com/r-lib/testthat/blob/e2703ca962af0419f122eb348b7a216e8861e887/R/praise.R#L19-L26 "https://github.com/r-lib/testthat/blob/e2703ca962af0419f122eb348b7a216e8861e887/R/praise.R#L19-L26")[](https://github.com/r-lib/testthat/blob/e2703ca962af0419f122eb348b7a216e8861e887/R/praise.R#L19-L26)

```
"Keep trying!",  
"Don't worry, you'll get it.",  
"No one is perfect!",  
"No one gets it right on their first try",  
"Frustration is a natural part of programming :)",  
"I believe in you!"
```

特に励ましているように見えねぇのは俺の問題？

オレにもそう見える

上っ面っぽさがあるよな

**No one is perfect!**  
特にお前

adjectiveになにはいるんだろ

```
praise <- function() {  
 x <- c(  
 “You rock!”,  
 “You are a coding rockstar!”,  
 “Keep up the good work.”,  
 “:)”,  
 “Woot!”,  
 “Way to go!”,  
 “Nice code.”,  
 praise::praise(“Your tests are ${adjective}!”),  
 praise::praise(“${EXCLAMATION} — ${adjective} code.”)
```

[**CRAN - Package praise**  
_Build friendly R packages that praise their users if they have done something good, or they just need it to feel…_cran.r-project.org](https://cran.r-project.org/web/packages/praise/index.html "https://cran.r-project.org/web/packages/praise/index.html")[](https://cran.r-project.org/web/packages/praise/index.html)

praiseってモジュールがあるｗ

[**I added "megalomanic" by michielmuliergithub · Pull Request #83 · rladies/praise**  
_Edit description_github.com](https://github.com/rladies/praise/pull/83/files "https://github.com/rladies/praise/pull/83/files")[](https://github.com/rladies/praise/pull/83/files)

なんだよこのPRは

いいじゃんこのモジュール  
bot性が高すぎる

辞書作ってマジで作りこんでんじゃねぇかｗｗｗｗ

メッセージ豪華にするために依存追加してるからな

[**More praise diversity & new encouragement. · r-lib/testthat@6b57f32**  
_An R 📦 to make testing 😀. Contribute to r-lib/testthat development by creating an account on GitHub._github.com](https://github.com/r-lib/testthat/commit/6b57f32c5dddc3092974ec7cc094506fe3807939 "https://github.com/r-lib/testthat/commit/6b57f32c5dddc3092974ec7cc094506fe3807939")[](https://github.com/r-lib/testthat/commit/6b57f32c5dddc3092974ec7cc094506fe3807939)

アホでしょｗ

このコミット、R界の神と呼ばれるHadleyがコミットしてんじゃんかよwww (編注：このcommitを入れたのは日本では「Rの神」とも呼ばれる[Hadley Wickham](http://hadley.nz/) です。彼のサイトに行くと熱い視線に「こっちみんなwww」と草が生える事うけあいです。)

OpenBSDのsshかなんかも、パスワード間違うと煽ってこなかったっけ

sudoか

[**嘘のようなホントの話：パスワード入力に失敗すると罵ってくるシステムがある**  
_パスワード入力に失敗して、「パスワードが違います」といったエラーメッセージを見たことがある人は星の数ほどいますが、「お前はカスだ！」と罵倒された経験を持つ人は、いったいどれくらいいるでしょうか。 ..._blogos.com](https://blogos.com/article/65504/ "https://blogos.com/article/65504/")[](https://blogos.com/article/65504/)

[**Make Sudo Insult User For Each Incorrect Password Attempt - It's FOSS**  
_You can have lots of fun in Linux terminal. And I am not talking about those funny commands to run a train in Linux…_itsfoss.com](https://itsfoss.com/sudo-insult-linux/ "https://itsfoss.com/sudo-insult-linux/")[](https://itsfoss.com/sudo-insult-linux/)

それ OpenBSD というより、sudo の機能だったな

```
AC\_ARG\_WITH(pc-insults, \[AS\_HELP\_STRING(\[ — with-pc-insults\], \[deprecated\])\],  
\[case $with\_pc\_insults in  
 yes) enable\_offensive\_insults=no  
 AC\_MSG\_NOTICE(\[ — with-pc-insults option deprecated, it is now the default\])  
 ;;  
 no) enable\_offensive\_insults=yes  
 AC\_MSG\_NOTICE(\[ — without-pc-insults option deprecated, use — enable-offensive-insults\])  
 ;;  
esac\])
```

`— with-insults` オプションを付けてビルドすると、出るようになるらしい。  
[https://www.sudo.ws/repos/sudo/file/tip/configure.ac](https://www.sudo.ws/repos/sudo/file/tip/configure.ac)

`Speak English you fool` つよい

```
\[xxxxx@yyyyy ~\]$ sudo ls  
\[sudo\] xxxxx のパスワード:  
The more you drive — the dumber you get.
```

できたｗ

まだあるな

```
AC\_ARG\_WITH(all-insults, \[AS\_HELP\_STRING(\[ — with-all-insults\], \[include all the sudo insult sets\])\],  
AC\_ARG\_WITH(classic-insults, \[AS\_HELP\_STRING(\[ — with-classic-insults\], \[include the insults from the “classic” sudo\])\],  
AC\_ARG\_WITH(csops-insults, \[AS\_HELP\_STRING(\[ — with-csops-insults\], \[include CSOps insults\])\],  
AC\_ARG\_WITH(hal-insults, \[AS\_HELP\_STRING(\[ — with-hal-insults\], \[include 2001-like insults\])\],  
AC\_ARG\_WITH(goons-insults, \[AS\_HELP\_STRING(\[ — with-goons-insults\], \[include the insults from the “Goon Show”\])\],  
AC\_ARG\_WITH(python-insults, \[AS\_HELP\_STRING(\[ — with-python-insults\], \[include the insults from “Monty Python’s Flying Circus”\])\],
```

頑張りすぎだろw

classic-insults

[**sudo: 270660da2de4 plugins/sudoers/ins\_classic.h**  
_\* Copyright (c) 1996, 1998, 1999 Todd C. Miller \* \* Permission to use, copy, modify, and distribute this software for…_www.sudo.ws](https://www.sudo.ws/repos/sudo/file/tip/plugins/sudoers/ins_classic.h "https://www.sudo.ws/repos/sudo/file/tip/plugins/sudoers/ins_classic.h")[](https://www.sudo.ws/repos/sudo/file/tip/plugins/sudoers/ins_classic.h)

ほう  
これはたのしそうだ  
無駄にくっそ作り込んであるな

煽っていこう  
!煽り (編注: !からはじまるワードはbotコマンドで、ランダムでDBから何かが引かれる)

pyspa-bot  
出力に慎みなきこと。

なにげにこのbotのチョイス神がかってた

```
#ifndef OFFENSIVE\_INSULTS
```

今まで見た中で一番圧強いdefine

```
#ifdef PC\_INSULTS  
 “Listen, broccoli brains, I don’t have time to listen to this trash.”,  
#else  
 “Listen, burrito brains, I don’t have time to listen to this trash.”,  
#endif
```

何が違うのかわからん

ブリトー → メキシコ料理、文化的背景を連想させる  
ブロッコリー → PCに配慮

ポリコレか

その分岐作る方がPCに問題ありそうｗ

いかがでしたか。人はこのようにしてコンピュータからエネルギーを貰っているし、それを支えるソフトウェアエンジニアの力が感じられたでしょうか？

明日は、みんなだいすきwozozoです。