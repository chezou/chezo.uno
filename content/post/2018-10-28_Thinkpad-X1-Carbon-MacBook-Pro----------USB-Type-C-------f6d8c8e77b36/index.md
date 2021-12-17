---
title: Thinkpad X1 CarbonとMacBook Proとで使える充電可能なUSB Type-Cのハブを選ぶ
description: >-
  転職をして、業務で使うマシンがMacBook Proになったので、自宅用のThinkpad X1 Carbon (5th Gen,
  2017モデル)と共通して使える充電とUSB-Aがはやせるハブ(とかマルチポートアダプタとか色々言われているもの)を探しました。
date: '2018-10-28T13:11:26+09:00'
categories: []
keywords: [PC]
authors: [aki]
---

![“two phones on white table” by [Steve Johnson](https://unsplash.com/@steve_j?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](/img/0__jIYyoN2vxlQsPgm5.jpg)
“two phones on white table” by [Steve Johnson](https://unsplash.com/@steve_j?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

転職をして、業務で使うマシンがMacBook Proになったので、自宅用のThinkpad X1 Carbon (5th Gen, 2017モデル)と共通して使える充電とUSB-Aがはやせるハブ(とかマルチポートアダプタとか色々言われているもの)を探しました。

### 最終的に選んだもの

以下の2つを買いましたが、買ってから2ヶ月弱安定して動作しています。

[**_Amazonベーシック USB3.1タイプC - HDMIマルチポートアダプター_**  
Amazonベーシック USB3.1タイプC - HDMIマルチポートアダプターamzn.to](https://amzn.to/2CMJPB1 "https://amzn.to/2CMJPB1")[](https://amzn.to/2CMJPB1)

[**USB-C PD 充電器 Power Delivery 60W 急速充電 PSE認証 ACアダプター Macbook Pro、任天堂スイッチ、Dell XPS、X1 Carbon 2017等対応…**  
_USB-C Power Delivery充電器 MacBook Pro 2016、任天堂スイッチ、X1 Carbon 2017をはじめとするType C対応デバイスに最大60Wの出力で急速充電可能です。 また、iPhone 8 /…_amzn.to](https://amzn.to/2EOUH4e "https://amzn.to/2EOUH4e")[](https://amzn.to/2EOUH4e)

ここに至るまでにいくつかの充電器やハブを買っては返品を繰り返していたので、備忘録として書きたいと思います。

### 要件

*   USB Type-C Power Delivery(PD)で充電できる
*   USB-Aのポートがある
*   HDMI 4kは60Hzでないので気にしない

X1 Carbon 5th GenはUSB Type-Cで充電をするのですが、W数が45Wより少ないと充電できないように本体側でコントロールをしているという罠があります。それをいかに乗り越えるかが今回の課題でした。あと、Amazonのレビューを調べると「X1Carbonでは使えません」というコメントが散見されます。なので、利用可能という実績があるものを探さないといけないです。MacBook ProはNintendo Switchの充電器でも充電できるくらい、結構ゆるゆるです。

HDMI 4k 60HzはThunderbolt 3ポート一個では帯域が足りないため、複数の機能をもたせたハブでは実現不可能なので諦めました。Thunderbolt 3-Display Portケーブルを別途使っています。

### ハブを経由するとW数が下がる

X1 Carbon付属の充電器が45Wで、直接刺すと充電できるのにハブを経由すると充電ができなくなる、という現象が根本的な原因でした。厳密に言うとスリープ状態では充電できるけど、稼働時には充電されないのです。これに気づいたのは、Lenovoの純正のハブでも経由すると充電できないという記述がなされていたためです。

実際に検証しようとしたときに、45Wクラスの充電器は安価に手に入るのですが、60Wクラスの充電器でそれなりに安価で比較的安心して使えそうなものが見当たらず検証するのに苦労しました。ここに至るまでには、使い始めて1週間で熱暴走して死んでしまったハブもあり、USB PDがあるときちんと熱管理をできているようなものを探さないといけないというのもポイントでした。中には「高温になりますが大丈夫です」などと商品説明で開き直っているものもあり、注意が必要です。

たまたまEngadgetでPSEマークがついているというレビューをみた[Yojochの60W充電器](https://amzn.to/2EOUH4e)を見つけ買うことにしました。更には、1週間で壊れたハブを経験したので、ある程度信頼できそうなブランドでかついざとなれば返品・交換が容易にできそうなものということで、[Amazon Basicのハブ](https://amzn.to/2CMJPB1)を購入しました。

この苦労、おそらく2018年モデルだとしなくて良いみたいですが、参考になれば。