---
title: "カナ専用の試し"
date: 2025-03-20
draft: false
description: "ウエブ上のカナ専用文を支えるためのHTML・CSSを作って、ここで試してみたいと思う。"
tags: ["カナ"]
---

ウエブ上のカナ専用文を支えるためのHTML・CSSを作って、ここで試してみたいと思う。
文章全体はカナモジで表示される。
マウスオーバーやクリックをすると、局所的に漢字に戻すことができる。
TABキーを押すと順を追って、漢字があるところが表示される。
以上はテキストの操作だ。

今回の文章は『カナノヒカリ』第11号からの引用だ。
なぜこういう文章にしたかといえば、読んでいるところだったからにすぎない。
原文は漢字カナ交じり文として書かれており、別にカナ専用に適した文章というわけではない。
適していない文章だからこそ、カナ専用の支えるHTML・CSSを発揮できる。

{{< kanasenyou >}}

## 開発者へ

[ベースのHTML・CSSがGitHubにある](https://github.com/uncomputable/nayami/tree/master/layouts/shortcodes)。

まずは原文を下のような形に書き起こしておいた。
漢字のあるところにはフリガナをつけて、分かち書きは自分で決めた。

```
我[わ]が 国民[こくみん] は 外国[がいこく] の 文物[ぶんぶつ] を 取[と]り入[い]れて、 これ を 丸呑[まるの]み に する こと は ない。
```

そして、この文章を下のようなHTMLに書き換えるプログラムを使った。
HTMLはくどいから、自動的な書き換えは効率よい。
プログラムは自作でまだ未公開だ。

```
<div class="word" tabindex="0">
    <span class="front">わが</span>
    <span class="back">我が</span>
</div>
<div class="word" tabindex="0">
    <span class="front">こくみん</span>
    <span class="back">国民</span>
</div>
<span>は</span>
<div class="word" tabindex="0">
    <span class="front">がいこく</span>
    <span class="back">外国</span>
</div>
<span>の</span>
<div class="word" tabindex="0">
    <span class="front">ぶんぶつ</span>
    <span class="back">文物</span>
</div>
<span>を</span>
<div class="word" tabindex="0">
    <span class="front">とりいれて、</span>
    <span class="back">取り入れて、</span>
</div>
<span>これ</span>
<span>を</span>
<div class="word" tabindex="0">
    <span class="front">まるのみ</span>
    <span class="back">丸呑み</span>
</div>
<span>に</span>
<span>する</span>
<span>こと</span>
<span>は</span>
<span>ない。</span>
```

## 協力の呼びかけ

原文が漢字で書かれているため、読み方を考える必要があった。
日本語は読みが曖昧なことがある。
例えば、「数百年の後」という表現は「〜ののち」、「〜のあと」、もしくは「〜のご」と読むか、分からないことがある。
皆様の知恵にお任せしたい。
もし誤った読み方や誤字があれば、[ぜひご指摘ください](/contact)。
