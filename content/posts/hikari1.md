---
title: "カナノヒカリ第一号の完全カナ専用版"
date: 2025-07-18
draft: false
description: "『カナノヒカリ』第一号を記念して、その投稿をカナ専用文で再現してみました。ウエブ技術を通じて、いわゆるフリ漢字が自動的に表示されるようになっています。"
tags: ["カナ"]
---

103年も前（1922年）に発行された『カナノヒカリ』第一号を記念して、その投稿をカナ専用文で再現してみました。
原文の言葉はそのままに、旧字体や歴史的なカナづかいなど、漢字・カナの表記だけ現代風にしています。
また、できるだけ[標準分かち書き](https://www.kanamozi.org/sub-wakatigaki.html)の規則に従い、原文を分けて書きました。

こうした現代版の『カナノヒカリ』に触れて、当時の雰囲気も味わえると思います。
『カナノヒカリ』の投稿には面白いエピソードがありますので、読んでみてください。

## いわゆるフリ漢字

原文の多くは漢字カナ交じり文になっています。
つまり、現代日本語のように、漢字に頼るように書かれています。
これをカナ専用にしてみると、意味が曖昧になっているところが出てきます。
意味の分からない言葉を分かるようにするために、フリガナとは逆に漢字を振っています。

気になる文章のところにマウスや指を乗せると、その部分がすぐに漢字に切り替わるようになっています。
そこから離れると、またカナモジに戻ります。
こうすることで、意味の曖昧さを避けつつ、カナ専用文の形も保てます。

---

## 著作権の表示

下の投稿は『カナノヒカリ』第一号からの引用となります。
著作権はカナモジカイにあります。
許可を得て提供しています。

---

{{< kanasenyou-css >}}

{{< hikari01-01 >}}

{{< hikari01-02 >}}

{{< hikari01-03 >}}

{{< hikari01-04 >}}

{{< hikari01-05 >}}

{{< hikari01-06 >}}

---

## ウエブ技術について

フリ漢字をどのように実現したか説明します。

1. 括弧つきフリガナの日本語テキストファイルを自分の手で作成しました。
2. [Pythonスクリプト](https://github.com/uncomputable/nayami/tree/master/kanasenyou/furigana-to-html.py)を使って、テキストファイルをHTMLに変換しました。
3. [CSSスタイルシート](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/kanasenyou-css.html)と共に、フリガナから変換したHTMLを提供しました。

自分でフリガナを振る最初のステップが一番重要です。
なぜなら、フリガナを自動的に振ることが情報不足により不可能だからです。
例えば、「経緯」を「けいい」と読むか、「いきさつ」と読むか、定かではないことが多いです。
だから、最初のステップは自動的ではなく、専門家の知恵に頼ることにしました。

括弧つきフリガナのテキストファイルは下の通りです。
分けて書く必要があることが分かります。

```text
例文[れいぶん] と は、 文章[ぶんしょう] や 表現[ひょうげん] の 見本[みほん] として 提示[ていきょう] される 文[ぶん] の こと です。 例[れい] として 挙[あ]げられる 文章[ぶんしょう] や、 ある 表現[ひょうげん] の 模範[もはん] と なる 文章[ぶんしょう] を 指[さ]します。
```

上のテキストファイルは下の通りのHTMLに変換されます。

---

{{< reibun >}}

---

分かち書きに関しては、どのようにやっても問題ありません。
[Pythonスクリプト](https://github.com/uncomputable/nayami/tree/master/kanasenyou/furigana-to-html.py)によって、入力したテキストファイルが空白で区切られ、HTMLの要素に変換されます。

例えば、下には別の分かち書きのしたテキストファイルがあります。

```text
例文[れいぶん]とは 、 文章[ぶんしょう]や 表現[ひょうげん]の 見本[みほん]と して 提示[ていきょう]される 文[ぶん]の こと です 。 例[れい]と して 挙[あ]げられる 文章[ぶんしょう]や 、 ある 表現[ひょうげん]の 模範[もはん]と なる 文章[ぶんしょう]を 指[さ] します 。
```

上のテキストファイルは下の通りになります。

---

{{< reibun2 >}}

---

GitHubには、使った資料すべてを公開していますので、興味があれば見てください。
また、自分のプロジェクトでも自由に使っても構いません。

| フリガナつきのテキストファイル | 変換したHTML |
|:------------------------------:|:------------:|
| [『カナノヒカリ』第1号第1話](https://github.com/uncomputable/nayami/tree/master/kanasenyou/hikari01-01.txt) | [『カナノヒカリ』第1号第1話](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/hikari01-01.html) |
| [『カナノヒカリ』第1号第2話](https://github.com/uncomputable/nayami/tree/master/kanasenyou/hikari01-02.txt) | [『カナノヒカリ』第1号第2話](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/hikari01-02.html) |
| [『カナノヒカリ』第1号第3話](https://github.com/uncomputable/nayami/tree/master/kanasenyou/hikari01-03.txt) | [『カナノヒカリ』第1号第3話](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/hikari01-03.html) |
| [『カナノヒカリ』第1号第4話](https://github.com/uncomputable/nayami/tree/master/kanasenyou/hikari01-04.txt) | [『カナノヒカリ』第1号第4話](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/hikari01-04.html) |
| [『カナノヒカリ』第1号第5話](https://github.com/uncomputable/nayami/tree/master/kanasenyou/hikari01-05.txt) | [『カナノヒカリ』第1号第5話](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/hikari01-05.html) |
| [『カナノヒカリ』第1号第6話](https://github.com/uncomputable/nayami/tree/master/kanasenyou/hikari01-06.txt) | [『カナノヒカリ』第1号第6話](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/hikari01-06.html) |
| [例文](https://github.com/uncomputable/nayami/tree/master/kanasenyou/reibun.txt) | [例文](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/reibun.html) |
| [例文2](https://github.com/uncomputable/nayami/tree/master/kanasenyou/reibun2.txt) | [例文2](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes/reibun2.html) |
