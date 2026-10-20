#!/usr/bin/env python3
"""Render design ledgers for human review; never execute the application."""
import collections, json
from pathlib import Path
A=Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((A/name).read_text())
r=load('requirements.json'); s=load('scenarios.json'); m=load('methods.json'); c=load('coverage_review.json'); g=load('black-box-gate.json'); p=load('pending-business-inputs.json')
black=[x for x in s['items'] if x['kind']=='black_box']; req={x['id']:x for x in r['items']}; method={x['id']:x for x in m['items']}; linked=collections.defaultdict(list)
for x in black:
    for i in x['requirement_ids']: linked[i].append(x['id'])
lines=['# 黑盒场景设计报告','',f"需求：{len(req)}；黑盒场景：{len(black)}；方法：{len(method)}；覆盖需求：{len(set(linked)&set(req))}/{len(req)}。",f"黑盒门禁：{g['status']}；独立审查：{c['status']}。",'', '本次仅完成需求快照、黑盒场景设计和独立反事实审查。未实现网站、未执行应用测试、未生成白盒场景、未宣称网站验收通过。','',f"基线：{r['version']}",'', '## 分包覆盖','', '| 业务包 | 需求数 | 已关联需求 | 关联场景数 |','| --- | ---: | ---: | ---: |']
for package in sorted({x['package'] for x in req.values()}):
    ids=[i for i,x in req.items() if x['package']==package]; scenarios={v for i in ids for v in linked[i]}
    lines.append(f'| {package} | {len(ids)} | {sum(bool(linked[i]) for i in ids)} | {len(scenarios)} |')
history=A/'review-history/round-1/coverage_review.json'
if history.is_file():
    first=json.loads(history.read_text()); gaps=[x for x in first['items'] if x.get('verdict')=='gap']
    lines+=['',f"首轮独立审查发现 {len(gaps)} 项需求涉及 {sum(len(x.get('uncovered_paths',[])) for x in gaps)} 条缺口记录；首轮台账与审查保存在 review-history/round-1/。当前仍存在的审查缺口：{sum(x.get('verdict')=='gap' for x in c['items'])} 项。"]
lines+=['','跨包场景会在多个包中出现；上述关联场景数不可直接相加。','','## 独立审查与门禁','',c['basis'],'', '```json',json.dumps(g,ensure_ascii=False,indent=2),'```','','## 未确定的业务输入','',p['execution_policy'],'']
for group in p['groups']:
    lines.append('- '+group['id']+'：'+'、'.join(group['topics'])+'。')
lines+=['','这些输入在执行前需要已确认规则与可核对数据；当前不选定任何具体经营值。场景只在约定范围内给出条件化预期，缺项分支按需求明确阻断。独立审查中的未覆盖路径见 coverage_review.json。','','## 生成文件完整路径','']
manifest={path for path in A.rglob('*') if path.is_file() and '__pycache__' not in path.parts}
manifest.update({A/'black-box-design-report.md', A/'black-box-scenarios.md'})
for path in sorted(manifest):
    lines.append('- '+str(path))
(A/'black-box-design-report.md').write_text('\n'.join(lines)+'\n')
lines=['# 黑盒场景与操作方法','', '全部内容为未来执行计划，不是实际执行结果。经营参数引用已确认配置，合成数据不构成营业政策。','']
for x in black:
    lines+=['## '+x['id']+'：'+x['title'],'','需求：'+', '.join(x['requirement_ids']),'','预期结果：',json.dumps(x['expected'],ensure_ascii=False,indent=2) if not isinstance(x['expected'],str) else x['expected'],'']
    for i in x['method_ids']:
        v=method[i]; lines+=['### 方法 '+i,'',v['description'],'']
        for key,label in [('preconditions','前置条件'),('actions','操作步骤'),('evidence_expected','未来执行证据')]:
            value=v.get(key); lines.append('**'+label+'**'); lines.append('')
            if isinstance(value,list): lines += [f'{n}. '+(y if isinstance(y,str) else json.dumps(y,ensure_ascii=False)) for n,y in enumerate(value,1)]
            else: lines.append(value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2))
            lines.append('')
(A/'black-box-scenarios.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'requirements':len(req),'black_box_scenarios':len(black),'methods':len(method),'covered':len(set(linked)&set(req)),'gate':g['status'],'review':c['status']},ensure_ascii=False))
