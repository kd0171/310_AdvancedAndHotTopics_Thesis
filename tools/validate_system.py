#!/usr/bin/env python3
"""Check source completeness, language parity, and evidence source matching."""
from pathlib import Path
import json,csv,re,sys,fitz
base=Path(__file__).resolve().parent.parent
cat=json.loads((base/'02_literature/catalog/LITERATURE_CATALOG.json').read_text(encoding='utf-8'))
ver=json.loads((base/'VERSION.json').read_text(encoding='utf-8'))
latest=base/'01_paper/versions'/ver['latest']
errs=[]
for lang in ('ja','de'):
 files=sorted((latest/lang).glob('*.md'))
 if len(files)!=7:errs.append(f'{lang}: expected 7 chapter md; got {len(files)}')
for d in cat:
 if d['pdf_file'] and not (base/'02_literature/papers'/d['pdf_file']).exists():errs.append(f"Missing PDF: {d['id']}")
with (base/'02_literature/evidence/EVIDENCE_LEDGER.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
for row in rows:
 p=base/'02_literature/papers'/row['source_filename']
 if not p.exists():errs.append('Missing quote source '+row['evidence_id']);continue
 d=fitz.open(p);idx=int(row['pdf_page'])-1
 if not (0<=idx<len(d)):errs.append('Invalid page '+row['evidence_id']);continue
 t=re.sub(r'\s+',' ',d[idx].get_text()).replace('\xad','').replace('ﬁ','fi').replace('ﬂ','fl')
 q=re.sub(r'\s+',' ',row['original_excerpt']).replace('\xad','').replace('ﬁ','fi').replace('ﬂ','fl')
 if q not in t:errs.append('Quote not found '+row['evidence_id'])
assert not any('Abstract' in x['section'] for x in rows)
print('VERSION',ver['latest'],'SOURCE PAPERS',sum(bool(c['pdf_file']) for c in cat),'evidences',len(rows),'errors',len(errs))
for x in errs:print('ERROR',x)
sys.exit(bool(errs))
