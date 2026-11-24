#!/usr/bin/env python3
"""Start a new immutable chapter-workspace version, then edit the new files only."""
from pathlib import Path
import argparse, json, shutil, re, datetime
BASE=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser()
p.add_argument('--date',default=datetime.date.today().strftime('%Y-%m-%d'))
p.add_argument('--summary',required=True)
a=p.parse_args()
if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',a.date):raise SystemExit('YYYY-MM-DD')
ver=json.loads((BASE/'VERSION.json').read_text(encoding='utf-8'))
old=ver['latest'];oldpath=BASE/'01_paper/versions'/old
new='v%03d_%s'%(int(old[1:4])+1,a.date.replace('-',''))
newpath=BASE/'01_paper/versions'/new
if newpath.exists():raise SystemExit('New version exists; nothing overwritten')
shutil.copytree(oldpath,newpath)
for f in newpath.rglob('*.md'):
 t=f.read_text(encoding='utf-8').replace(old,new).replace('v%03d'%(int(old[1:4])),new[:4]);f.write_text(t,encoding='utf-8')
ver['latest']=new;ver['created']=a.date
(BASE/'VERSION.json').write_text(json.dumps(ver,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (BASE/'CHANGELOG.md').open('a',encoding='utf-8') as f:f.write(f'\n## {new}\n- {a.summary}\n- 日本語・ドイツ語の章全文、根拠、議題、引継ぎを更新すること。\n')
h=BASE/'04_handover'/('SESSION_LOG_'+a.date.replace('-','')+'.md')
if not h.exists():h.write_text(f'# SESSION_LOG {a.date}\n\n## 議題\n- {a.summary}\n\n## 決定\n- （追記）\n\n## 変更対象\n- （追記）\n\n## 次の議題と後続章へのフラグ\n- （追記）\n',encoding='utf-8')
print('Created',new,'under',newpath)
print('REMINDER: update both full chapters, HANDOFF_CURRENT, DECISION_LOG, OPEN_ISSUES, EVIDENCE, and ZIP.')
