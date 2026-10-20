#!/usr/bin/env python3
"""Persist role outcomes and machine transitions without raw tool transcripts."""
import hashlib,json,sys
from pathlib import Path
A=Path(__file__).resolve().parents[1]
b=json.loads((A/'workflow-sessions.json').read_text())
sid=next(reversed(b));src=Path.home()/'.spex/sessions'/f'{sid}.records.jsonl'
events=[]
for line in src.read_text().splitlines():
    r=json.loads(line).get('record',{})
    if r.get('type')=='player_finished':
        result=r.get('result',{})
        events.append({'type':'independent_role_completion','role':r.get('playerId'),'turn_id':r.get('turnId'),'timestamp':r.get('timestamp'),'status':result.get('status'),'report':result.get('finalText')})
    elif r.get('type')=='captain_telemetry' and r.get('topic')=='playbook.trace':
        t=r.get('payload') or {}
        if t.get('playbookId')=='black-box-scenarios' and t.get('type') in ['fsm.transition','boss.input.settled']:
            events.append({'type':t.get('type'),'timestamp':t.get('timestamp'),'payload':t.get('payload')})
    elif r.get('type')=='captain_reply':
        events.append({'type':'captain_terminal_report','report':r.get('text')})
out={'session_id':sid,'binding':b[sid],'runtime_record_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'skill':'/Users/boboyang/.codex/skills/app-delivery-acceptance/SKILL.md','roles':'Analyst designs and repairs; separate Reviewer judges coverage; deterministic script gates final design','events':events,'application_execution':'not_run','website_acceptance':'not_assessed'}
(A/'workflow-provenance.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Saved provenance for '+sid)
