#!/usr/bin/env python3
"""Local-only structural and link checks; no network or publication."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
ROOT=Path(__file__).resolve().parent; SITE=ROOT/'site'
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.refs=[]; self.lang=None;self.h1=0;self.ids=[];self.scripts=0;self.forms=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='script':self.scripts+=1
        if tag=='form':self.forms+=1
        if 'id' in a:self.ids.append(a['id'])
        for k in ['href','src']:
            if k in a:self.refs.append(a[k])
count=0
for path in SITE.rglob('*.html'):
    text=path.read_text(); page=Page();page.feed(text)
    assert page.lang in ['es','en'],path
    assert page.h1==1,path
    assert not page.scripts and not page.forms,path
    assert '{{' not in text,path
    assert len(page.ids)==len(set(page.ids)),path
    for ref in page.refs:
        url=urlsplit(ref)
        if url.scheme:assert url.scheme in ['https','mailto'],(path,ref);continue
        target=(path.parent/unquote(url.path)).resolve() if url.path else path.resolve()
        assert target.is_relative_to(SITE.resolve()) and target.exists(),(path,ref)
        if url.fragment:
            p=Page();p.feed(target.read_text());assert url.fragment in p.ids,(path,ref)
    count+=1
assert count==11,count
assert (SITE/'.nojekyll').exists()
assert not any(x.suffix in ['.swift','.sqlite','.p12','.mobileprovision','.ckdb'] or x.name=='.git' for x in SITE.rglob('*'))
print(f'PASS: {count} ES/EN HTML pages; local links, language, headings, no scripts/forms or app files.')
