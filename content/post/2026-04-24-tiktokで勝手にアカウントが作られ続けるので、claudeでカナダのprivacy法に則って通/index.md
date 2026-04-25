---
title: TikTokで勝手にアカウントが作られ続けるので、Claudeでカナダのprivacy法に則って通報をした
subtitle: ''
summary: ''
date: 2026-04-24 17:27:00-07:00
lastmod: ''
categories: [カナダ生活]
tags: [privacy, Canada]
draft: false
featured: false
image: null
recommendations: [/post/2008-09-07-chu-yin-mikunokaraokequ/, /post/2009-10-26-memo-windows7yong-dong-zuo-que-ren-xi-rinku/,
  /post/2025-09-19-review-fatigue/]
---

> [!WARNING]
> この記事は、Claude Opus 4.7とのやり取りを通じて解決した問題の顛末を、Opusに書かせたものです。ある程度のレビューはしていますが、情報の確実性はご自身で再検証することをおすすめします。

## tl;dr

- 自分が使った覚えのない TikTok アカウントが、僕のメアドで2つ作られていた（@chezou2 と @nigtg679）
- TikTok はメアド認証なしでアカウント登録を許可している。これが構造的な同意の欠落
- TikTok サポート経由で1つ目を削除させたが、しばらくして別のアカウントが同じメアドで作成され再発
- カナダの規制機関2つに通報した
    - [**CRTC**](https://crtc.gc.ca/)**（**[**Spam Reporting Centre**](https://www.fightspam.gc.ca/)**）** に [CASL](https://laws-lois.justice.gc.ca/eng/acts/E-1.6/) 違反として通報
    - [**OPC**](https://www.priv.gc.ca/)**（Office of the Privacy Commissioner of Canada）** に [PIPEDA](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/) 違反として正式 complaint 提出
- OPC は2025年9月に既に TikTok 相手に joint investigation の Report of Findings ([#2025-003](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2025/pipeda-2025-003/)) を出しており、僕の complaint はその文脈に乗る形になった
- カナダ居住者なら同様のケースで使える手順をまとめておく

***

## 何が起きたか

2025年11月頃から、`noreply@account.tiktok.com` という送信元から「新しいデバイス（LGE LM-Q730）からログインがありました」というメールが届くようになりました。僕は LG の Android 端末を持っていません。そもそも TikTok のアカウントを作ったことがありません。

メールの宛先は僕のプライベートのGmailのメアド。メール内では `@chezou2` というハンドルが言及されていて、僕のハンドル（@chezou ベースのもの）に近い名前で誰かがアカウントを作ったらしい、ということがわかりました。

ここで気付いた違和感: **TikTok は、メアド認証なしでアカウントを作らせている**。僕のメアドに「このメアドで TikTok アカウントを作ろうとしている人がいます、本人ですか？」という確認メールは一度も来ていない。にもかかわらずアカウントが成立している。

つまり、登録時のメアド入力に対する所有確認が一切行われていません。誰でも他人のメアドでアカウントを作ることができ、本来の所有者は通知メールを受け取り続ける構造になっている。

## 1回目の対応：3月にTikTokサポートへ

3月15日、TikTok の privacy report フォーム（https://www.tiktok.com/legal/report/privacy）から「Report a potential privacy violation」として通報しました。

返信は `feedback@tiktok.com` から、テンプレ的な内容で「アカウントを削除したい場合は、ログインして設定画面から削除してください」というもの。**そもそも自分のアカウントじゃないからログインできない**、というのが問題の本質なのに、こちらが所有者であることを前提とした応答が来る。

返信して「これは僕のアカウントではない、誰かが僕のメアドで作ったものだ、削除してほしい、PIPEDA 適用の話だ」と書きました。すると次の返信で、こう言われた。

> アカウント所有を確認するため、以下の情報を提供してください: 登録日、最初のログイン場所、登録時のデバイス、登録時の電話番号、リンクされた SNS アカウント...

これに答えられるわけがない。**答えられないこと自体が、僕が所有者でない証拠**です。再度返信して、「これらの情報を提供できないこと自体が、僕がアカウントを作っていない証拠だ。所有者であることを示せという要求は、non-user からの申し立てには構造的に応えられない」と書きました。あわせて「30日以内に解決しない場合は OPC に formal complaint を出す」と通告。

その後、@chezou2 は削除されました。

## ところが再発

僕が TikTok への返信で「30日以内に解決しなければ OPC に formal complaint を出す」と通告していたのですが、その期限が過ぎた翌日の4月16日から、別の送信元（`notification@service.tiktok.com`、Reply-To が `edm.feedback@tiktok.com`）からメールが来るようになりました。今度は **@nigtg679** という別のハンドル宛て。フランス語で「Mrs-mama💕✨️😘 t'a envoyé un message」みたいな、フランス語圏ユーザーからのメッセージ通知。

つまり、@chezou2 が削除された後、また別の誰かが僕のメアドでアカウントを作ったわけです。

ここで個人の問題を超えていることがはっきりしました。**個別アカウントを削除しても、TikTok がメアド認証を実装しない限り、永遠に同じことが繰り返される**。

ちなみに Reply-To にある `edm.feedback@tiktok.com` の `edm` は業界でいう "Electronic Direct Mail"、つまりマーケティングメール基盤の符牒。TikTok 自身がこれらの通知メールを marketing email infrastructure 内で扱っている、という小さな証拠でもあります。

## 規制当局ルートを2本

ここで「個別削除を申請し続ける」のは無限ループだと判断し、規制当局に持ち込むことにしました。カナダで使えるルートは2本あります。

### [CASL](https://laws-lois.justice.gc.ca/eng/acts/E-1.6/)（Canada's Anti-Spam Legislation） / [CRTC](https://crtc.gc.ca/)

CASL は同意なき商業電子メッセージ（CEM）の送信を規制する法律。ポイントは：

- 違反に対して **罰金を課す権限** が CRTC にある
- TikTok からの通知メールは「TikTok プラットフォームへの利用を促進する」 = 商業活動の促進、と解釈できる
- transactional notification（アカウント所有者向けの取引通知）の例外は、僕が **アカウント所有者ではない** ので適用できない

通報先は [CRTC Spam Reporting Centre](https://www.fightspam.gc.ca/)（spam@fightspam.gc.ca）。実は **メールに直接転送できる**（オンラインフォームより楽）。コンテキスト説明メールを1通送り、添付として証拠メールを `.eml` 形式で5通同梱して送信しました。

注意点: SRC は個別の case outcome を complainant にフィードバックしません。だから「処理が終わったら教えて」という期待はできない。集積されたデータが enforcement target の特定に使われる、という形。

### [PIPEDA](https://laws-lois.justice.gc.ca/eng/acts/p-8.6/)（Personal Information Protection and Electronic Documents Act） / [OPC](https://www.priv.gc.ca/)

PIPEDA は個人情報の収集・使用・開示に同意を求める法律。本件で問われるのは Schedule 1 の Principle 4.3（Consent）。

OPC への formal complaint は [online form](https://services.priv.gc.ca/plainte-complaint-lprpde-pipeda/en/register) 経由。ここで **罠** がありました。

#### フォームの自動ロック問題

最初に試した時、フォーム内に「他の機関に同じ件で complaint を提出していますか？」という質問がありました。CRTC SRC に出しているので素直に「Yes」と答えたら、システムが自動的にセッションを終了させ、「他の手続きを完了させてからまた来てください」というメッセージで蹴られました。

しかし SRC は個別フィードバックを出さない（前述）ので、待っていても「終了」は永遠に来ない。これでは PIPEDA 申立てが事実上不可能になる。

#### Information Centre 経由でリカバリ

OPC には [Information Centre](https://www.priv.gc.ca/en/contact-the-opc/contact-the-information-centre/) があり、自由記述2,000文字以内で問い合わせができます。ここに「自動ロックされた、CASL と PIPEDA は対象としている問題が違う、どうしたらいいか」という旨を送ったところ、24時間以内に OPC の担当から書面で返信が来ました。

返信内容は要約すると：

- TikTok の privacy contact（TikTok Inc., Culver City）へ書面で連絡することを推奨
- それでも解決しない場合は、formal complaint を提出してよい
- フォームの「他機関への complaint」質問には **「No」と答え、free text section で状況を説明** してほしい

OPC自身がフォームのバグ的挙動を認識していて、回避方法を書面で指示してくれた、というわけです。

#### Formal complaint の構成

OPC オンラインフォームは Part A（組織への接触履歴）/ Part B（管轄判定）/ Part C（詳細・救済）の3部構成。Part C は4つの自由記述欄があり、それぞれ500〜2,500文字制限。

法的根拠の組み立てとしては:

- **Principle 4.3 (Consent)**: 同意なしに個人情報（メアド）を収集・使用している
- **Principle 4.3.2 (Meaningful consent)**: メアド認証がない以上、同意の存在を裏付ける機構がそもそも存在しない
- **Reasonable expectations of a non-user**: PIPEDA Findings [#2012-002](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2012/pipeda-2012-002/)（Facebook が non-user のメアドを friend suggestion に使った件）が直接の precedent
- **Principle 4.7 (Safeguards)**: @chezou2 削除後に @nigtg679 が再発した事実が、reasonable safeguards の欠落を示す

要望としては:

1. **PIPEDA s.17.1 に基づく Compliance Agreement** — メアド認証義務化、non-ownership-based の苦情プロセス整備
2. 僕のメアドに紐づく全アカウントの削除
3. 僕のメアドの blocklist 登録
4. Public Report of Findings の発行（僕と同じ被害に遭っている人がいるはず）

添付資料は8ページ以内、25MB以内で、TikTok サポートとの3月の往復スレッド・OPC Information Centre からの返信・11月の security notification・4月の social notification サンプルを PDF 化して同梱しました。

## 既存の OPC × TikTok の文脈

書きながら気付いたのですが、**OPC はすでに2025年9月に TikTok 相手の Report of Findings (**[**#2025-003**](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2025/pipeda-2025-003/)**) を出しています**。OPC、CAI（Quebec）、OIPC BC、OIPC AB の4機関 joint investigation で、主に未成年者からの同意取得とターゲティング広告の問題に焦点が当てられたもの。

僕のケースは未成年者問題ではなく、non-user の同意を得ない個人情報利用という別の角度ですが、「TikTok の同意取得の実務全般に問題がある」という OPC の認識と整合する話。投稿のタイミングとしては悪くない（OPC の興味の射程内に入りやすい）。

ちなみにこの Findings の中では、BC PIPA と PIPEDA の jurisdiction 関係についても整理されていて、cross-border data flow の場合は両者が "airtight seal" で適用される、という理屈が示されています。僕が BC 在住で TikTok（シンガポール法人）相手という構図でも、PIPEDA 適用に問題がない理由がここで補強されます。

## カナダ居住者へのチェックリスト

同じような状況に遭遇した人向けに、手順を整理します。

**ステップ0: 現状把握**

- 不審なメールの送信元、送信日時、本文内容を保全する
- Gmail なら spam フォルダから救出してラベル付け（30日で自動削除されるので注意）
- 本文中に出てくる「自分のものではないアカウントハンドル」をメモ

**ステップ1: 相手企業に書面で連絡**

- 企業の privacy report channel から書面で連絡する（メール、フォーム、どちらでもよい）
- PIPEDA を引用する（信頼性が変わる）
- 「自分は所有者ではない」「メアド所有者として削除を要求する」を明確にする
- 30日以内の解決を促す

**ステップ2: CRTC SRC に CASL 通報（マーケ性のあるメール）**

- spam@fightspam.gc.ca に状況説明＋証拠 .eml を添付して送る
- フォーム経由より、メール直接転送のほうがヘッダー情報が完全に保持されて証拠能力が高い
- 個別フィードバックは来ない前提

**ステップ3: OPC に PIPEDA complaint**

- まず Information Centre に状況を聞く（フォーム経由、2,000字以内）
- 24〜48時間で返信が来る
- 指示に従って formal complaint を提出
- 添付資料は8ページ以内、25MB以内

**注意点**

- OPC は現在処理遅延あり（数ヶ月）。すぐに結果は出ないと割り切る
- BC OIPC（州機関）にも管轄が及ぶ可能性があるが、cross-border の場合は PIPEDA 適用が筋。OPC が必要なら自動的に振り分ける
- OPC は order-making power を持たない（罰金を課したり強制執行したりはできない）。最強のツールは **Compliance Agreement (s.17.1)** で、これは Federal Court で強制執行可能。だから明示的に要求する価値がある

## 雑感

（ここは人間が書いています）

- 今回、Sonnet 4.6で調査を開始したのだが、正式にcomplaintする段になって念のため出たばかりのOpus 4.7で検証をさせたところ、だいぶ間違いや思い込みを正せたのでよかった
    - たとえば「30日対応がなければ OPC に行ける」という Sonnet の主張は、実は法的根拠がなく Sonnet が圧力装置として勝手に設定した期限だった、というのを Opus に指摘された。これは戦術的には機能するものの、法的デッドラインと誤認すると別の判断ミスにつながるので、確認できてよかった。
- こういう法律系の調査を全部自力でやるの相当厳しいので、リファレンスはAIに取ってこさせて自分でも確認するのが良さそう
- こういった重めのトラブル解決を考えると、個人でLLM系のサービスを契約しないと辛いですね...
