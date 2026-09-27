#!/usr/bin/env python3
"""Undo Cloudflare quick-tunnel email obfuscation in mirrored HTML (the /cdn-cgi decoder does not exist on Pages)."""
import re, sys, pathlib

def dec(h):
    k = int(h[:2], 16)
    return ''.join(chr(int(h[i:i+2], 16) ^ k) for i in range(2, len(h), 2))

for p in sys.argv[1:]:
    f = pathlib.Path(p)
    s = f.read_text(encoding='utf-8')
    s = re.sub(r'<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="([0-9a-f]+)">\[email&#160;protected\]</a>', lambda m: dec(m.group(1)), s)
    s = re.sub(r'<a href="/cdn-cgi/l/email-protection#([0-9a-f]+)"', lambda m: '<a href="mailto:' + dec(m.group(1)) + '"', s)
    s = re.sub(r'<script data-cfasync="false" src="/cdn-cgi/scripts/[^"]+/cloudflare-static/email-decode.min.js"></script>', '', s)
    f.write_text(s, encoding='utf-8')
    if 'cdn-cgi' in s:
        print('WARN cdn-cgi left in', p)
