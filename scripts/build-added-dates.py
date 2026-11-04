#!/usr/bin/env python3
"""Real first-commit date (HST) of each top-level page -> assets/data/page-added.json (auto-expiring New badge on find cards)."""
import json,subprocess,os,datetime
os.chdir(os.path.join(os.path.dirname(__file__),'..'))
log=subprocess.run(['git','log','--diff-filter=A','--format=@%cI','--name-only','--','*.html'],capture_output=True,text=True).stdout
first={};cur=None
for ln in log.splitlines():
    if ln.startswith('@'): cur=ln[1:]
    elif ln.strip() and '/' not in ln: first[ln.strip()]=cur
hst=datetime.timezone(datetime.timedelta(hours=-10))
out={k:datetime.datetime.fromisoformat(v).astimezone(hst).date().isoformat() for k,v in first.items()}
json.dump(out,open('assets/data/page-added.json','w'),separators=(',',':'),sort_keys=True);print(out)
