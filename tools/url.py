#!/usr/bin/env python3
"""原稿（genko.json）から、撮影プロンプターの URL を作る。
使い方: python3 tools/url.py [genko.json]   英語の画面にする時: genko.json に "lang": "en" を入れる（または --en）
原稿は URL の「#」より後ろに入るので、サーバーには届きません（スマホの中だけで使う）。"""
import base64, json, sys
args = [a for a in sys.argv[1:] if not a.startswith('--')]
p = args[0] if args else 'genko.json'
g = json.load(open(p, encoding='utf-8'))
keep = {k: g[k] for k in ('kata', 'dai', 'rows', 'nare') if k in g}
b = base64.urlsafe_b64encode(json.dumps(keep, ensure_ascii=False, separators=(',', ':')).encode()).decode().rstrip('=')
en = '--en' in sys.argv or g.get('lang') == 'en'
print(('https://sugukuru.yoseca.com/en/prompter/' if en else 'https://sugukuru.yoseca.com/prompter/') + '#g=' + b)
