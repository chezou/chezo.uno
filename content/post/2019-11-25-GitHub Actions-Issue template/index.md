---
authors: [aki]
date: '2019-11-25 00:52:00-08:00'
lastmod: '2019-11-28 22:10:00-08:00'
summary: GitHub Actionsを使って正規表現でtemplateをチェックする
tags: [GitHub]
title: GitHub ActionsでIssue templateに従っていないissueをcloseする
keywords: [issue, 正規表現, template, tabula, py, chezou, 貧弱, トリガー, close, actions]
recommendations: [/post/2016-09-11-pdfnobiao-wopandasnodataframenidekiru-tabula-py-zuo-tuta/,
  /post/2019-11-25-github actions-api token-pypi release/, /post/2011-11-25-googlezhi-nozheng-gui-biao-xian-enzinre2wori-ben-yu-deshi-sitemita/]
---

![](https://images.unsplash.com/photo-1520716963369-9b24de965de4?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb)

GitHub ActionsはissueやPRのcreateをトリガーに動いてくれる。

このActionを使えば正規表現でtemplateをチェックして自動でcloseする。経験上、面倒くさい人は大抵読まずにtemplate全消ししてくるので、貧弱な正規表現でも十分役に立つ。

[roots/issue-closer-action](https://github.com/roots/issue-closer-action)

実際のworkflowはこちら。

[chezou/tabula-py](https://github.com/chezou/tabula-py/blob/master/.github/workflows/autocloser.yml)

ポイントは以下のように雑に `.*((PATTERN_A)|(PATTERN_B)).*` と書いてあげれば良い。

```yaml
issue-pattern: ".*((Is your feature request related to a problem)|(Check list before submit)).*"
```

なお、この正規表現はJavaScriptの `RegExp` として動くのでChromeのconsoleなんかでテストすればいい。

```jsx
var regexp = new RegExp(".*((guidelines for Contributing)|(Check list before submit)).*");
regexp.exec("aaaaaaaguidelines for Contributingbbbb")
// (4) ["aaaaaaaguidelines for Contributingbbbb", "guidelines for Contributing", "guidelines for Contributing", undefined, index: 0, input: "aaaaaaaguidelines for Contributingbbbb", groups: undefined]

```

こんな感じで動く。

[test · Issue #189 · chezou/tabula-py](https://github.com/chezou/tabula-py/issues/189)

---

[Back to home](https://memo.chezo.uno/)