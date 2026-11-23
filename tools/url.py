#!/usr/bin/env python3
"""原稿（genko.json）から、撮影プロンプターの URL を作る。
使い方: python3 tools/url.py [genko.json]
原稿は URL の「#」より後ろに入るので、サーバーには届きません（スマホの中だけで使う）。"""
import base64, json, sys
p = sys.argv[1] if len(sys.argv) > 1 else 'genko.json'
g = json.load(open(p, encoding='utf-8'))
keep = {k: g[k] for k in ('kata', 'dai', 'rows', 'nare') if k in g}
b = base64.urlsafe_b64encode(json.dumps(keep, ensure_ascii=False, separators=(',', ':')).encode()).decode().rstrip('=')
print('https://sugukuru.yoseca.com/prompter/#g=' + b)
