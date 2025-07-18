# This work is in the public domain under the terms of the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.
# 
# To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights
# to this software to the public domain worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software. 
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.

import re
import sys

FURIGANA_PATTERN = re.compile(r"((.+)-)?([一-龯ヶ々〆]+)\[([^\]]+)\]")

def furigana_to_kanji(matchobj) -> str:
    kanji = (matchobj.group(2) or "") + matchobj.group(3)
    return f"{kanji}"

def furigana_to_kana(matchobj) -> str:
    kana = (matchobj.group(1) or "") + matchobj.group(4)
    return f"{kana}"

def word_to_html(word: str) -> str:
    majiri = FURIGANA_PATTERN.sub(furigana_to_kanji, word)
    kana = FURIGANA_PATTERN.sub(furigana_to_kana, word)
    return f'  <div class="word" tabindex="0"><span class="front">{kana}</span><span class="back">{majiri}</span></div>'

def file_to_html(input_file) -> str:
    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    output_paragraphs = []
    for paragraph in input_text.strip().split('\n'):
        output_words = []
        for word in paragraph.strip().split():
            if FURIGANA_PATTERN.search(word):
                html = word_to_html(word)
                output_words.append(html)
            else:
                output_words.append(f'  <span>{word}</span>')
        if not output_words:
            continue
        paragraph_html = '\n'.join(output_words)
        output_paragraphs.append(f'<div class="paragraph">\n{paragraph_html}\n</div>')

    result = "\n".join(output_paragraphs)
    return result

def display_help():
    help_message = """使い方: furigana-to-html.py [-h] text_file

フリガナのついたテキストファイルをHTMLに変換するツール

パラメータ:
  text_file   括弧つきフリガナの日本語テキストファイル

オプション:
  -h, --help  このヘルプメッセージを表示して終了"""
    print(help_message)

def main():
    if len(sys.argv) != 2:
        print("エラー: 必要なパラメータがない\n")
        display_help()
        sys.exit(1)
    if sys.argv[1] in ("-h", "--help"):
        display_help()
        sys.exit(0)
    text_file = sys.argv[1]

    try:
        print(file_to_html(text_file))
    except FileNotFoundError:
        print(f"エラー: ファイル「{text_file}」が見つからない", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"エラー: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
