"""Language-only localization from immutable pre-zh snapshot and reviewed explicit mappings."""
import json,pathlib,re,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/'review-history/pre-zh-localization'
MAP=json.loads((ROOT/'scripts/localize_zh_map.json').read_text())
COMMON={
'1. PLAN ONLY. Execute later on an available authorized app/test environment. If a required route, resource, policy, observable record or oracle is unavailable, mark the affected vector unproven/blocked; do not fabricate a result or infer approval. No app location is required during design.':'1. 仅为执行计划。日后在可用且已获授权的应用／测试环境中执行。如果所需入口、资源、政策、可观察记录或判定依据不可用，将受影响的测试向量标记为 unproven／blocked；不得编造结果或推断已获批准。设计阶段不需要应用地址。',
'2. Create a fresh named synthetic fixture per vector through supported customer/admin/service boundaries; reopen it to verify the stated starting state. Keep unrelated control records and record before balances/statuses. Do not inspect internal code/storage or assume a particular database, API shape or worker design.':'2. 通过受支持的客户、管理或服务交互边界，为每个测试向量新建有名称的合成测试数据；重新打开，确认其起始状态符合说明。保留无关对照记录，并记录操作前的余额和状态。不得检查内部代码或存储，也不得假定特定数据库、API 结构或后台任务设计。',
'3. Resolve market, currencies/minor units, rule versions, cutoffs/inclusivity, qualifications, role permissions and operational/visual standards from supplied confirmed configuration at execution time. Compute expected totals/sets independently before action; unknown business values remain pending, never adopt fixture values as business policy. Numeric examples are synthetic probes.':'3. 执行时根据已提供并确认的配置，确定市场、币种及其最小单位、规则版本、截止时间及边界是否包含、资格、角色权限，以及操作和视觉标准。操作前独立计算预期总额或集合；未知经营参数保持待定，不得把测试数据中的数值当成经营政策。数字示例仅为合成测试探针。',
'4. Credentials stay in an external secure store and are referenced only; capture redacted screenshots/receiver histories. Real-mode assertions use an authorized real-contract test environment and separately verified integration resources when later available; isolated app test mode is a distinct branch and does not prove real integration. Never initiate unapproved production charges, shipping or restore operations.':'4. 凭据保存在外部安全存储中，台账只记录引用；截图和接收方历史须脱敏。真实模式断言在日后具备条件时，使用已授权、符合真实服务契约的测试环境及单独验证过的集成资源；隔离的应用测试模式是独立分支，其通过不能证明真实集成通过。不得发起未经批准的生产扣款、发货或恢复操作。',
'4. After each vector, reload/re-enter through the appropriate authorized user or external receiver boundary and compare the observed state with the independently recorded before state and expected result. Check named unrelated control records. Record failures and missing oracles per vector; resetting one vector must not mask an earlier failure.':'4. 每个测试向量执行后，通过相应的已授权用户或外部接收方边界刷新或重新进入，将观察到的状态与独立记录的操作前状态及预期结果比较。检查指定的无关对照记录。逐向量记录失败和缺失的判定依据；重置某个向量不得掩盖先前失败。',
'1. For EACH vector: redacted setup/configuration and before-state record; ordered customer/staff action trace showing the actual action; final and reloaded user-visible page or supported external-system result. No execution evidence exists at design time.':'1. 对每个测试向量均需提供：脱敏的准备／配置及操作前状态记录；按顺序记录的客户／员工操作轨迹，证明实际执行了该操作；最终页面及重新加载后的用户可见页面，或受支持的外部系统结果。设计阶段尚无执行证据。',
'3. Where money, quantities, notifications or repeated actions are involved: before/after scoped balances, transaction/message/record identifiers and receiver history sufficient to detect a duplicate, wrong recipient or wrong mode. A screenshot of a button click alone is insufficient.':'3. 涉及金额、数量、通知或重复操作时，需记录相关范围内的前后余额、交易／消息／记录标识及接收方历史，足以发现重复执行、收件对象错误或模式错误。仅有点击按钮的截图不足以证明结果。'
}
sc=json.loads((BASE/'scenarios.json').read_text());me=json.loads((BASE/'methods.json').read_text()); paragraphs=dict(COMMON); titles=dict(MAP.get('method_titles',{})); expected=dict(MAP.get('method_expected',{}))
for s in sc['items']:
 key=s['id'].removeprefix('BB-');t=MAP['items'][key]
 titles[s['title']]=t[0];expected[s['expected']]=t[1]
 for marker,zhmarker in [(' Additional mandatory check:',' 额外必查：'),('; An actual forbidden transition request','；实际提交的禁止状态转换请求')]:
  if marker in s['expected']:expected[s['expected'].split(marker)[0]]=t[1].split(zhmarker)[0]
 s['title']=t[0];s['expected']=t[1]
for m in me['items']:
 key=m['id'].removeprefix('AI-');t=MAP['items'][key]
 p=m['preconditions'].split('\n\n');a=m['actions'].split('\n\n')
 paragraphs[p[4]]=t[2]
 if len(a)>1:paragraphs[a[1]]=t[3]
 for field,translations in MAP.get('extras',{}).get(key,{}).items():
  originals=[x for x in m[field].split('\n\n') if x not in COMMON and not x.startswith(('1. Read the confirmed requirement(s)','3. Assert:','2. Assertion evidence must demonstrate:')) and x not in (p[4],a[1] if len(a)>1 else '')]
  assert len(originals)==len(translations),(key,field,originals,translations)
  paragraphs.update(zip(originals,translations))
# Populate reusable expectations from explicit full translations.
for old,new in expected.items():paragraphs['3. Assert: '+old]='3. 断言：'+new;paragraphs['2. Assertion evidence must demonstrate: '+old]='2. 断言证据必须证明：'+new
untranslated=[]
for m in me['items']:
 matrix_rule=MAP.get('transition_execution_rules',{}).get(m['id'].removeprefix('AI-'))
 if matrix_rule is not None:m['transition_matrix']['execution_rule']=matrix_rule
 desc=m['description'];prefix='Planned reusable AI-operated boundary procedure: ';suffix='. Re-run with fresh fixtures for every enumerated vector; not executed evidence.'
 if desc.startswith(prefix) and desc.endswith(suffix):
  title=desc[len(prefix):-len(suffix)];m['description']='计划中的可复用 AI 边界操作方法：'+titles[title]+'。对每个列举的测试向量使用新的测试数据重新执行；本记录并非执行证据。'
 else:m['description']=MAP.get('special',{}).get(desc,desc);untranslated.append(('description',desc))
 for field in ['preconditions','actions','evidence_expected']:
  override=MAP.get('field_overrides',{}).get(m['id'].removeprefix('AI-'),{}).get(field)
  if override is not None:
   m[field]=override;continue
  translated=[]
  for part in m[field].split('\n\n'):
   if part in paragraphs:translated.append(paragraphs[part]);continue
   mt=re.fullmatch(r'1\. Read the confirmed requirement\(s\) (.+) from requirements\.json\. Enumerate every setup vector, including all stated table rows and independent omissions; record concrete fixture IDs, role, mode and expected oracle before execution\.',part)
   if mt:translated.append('1. 阅读 requirements.json 中已确认的需求 '+mt[1]+'。枚举每个准备测试向量，包括所有列明的表格行及各项独立缺失条件；执行前记录具体测试数据 ID、角色、模式和预期判定依据。');continue
   if part in MAP.get('special',{}):translated.append(MAP['special'][part]);continue
   untranslated.append((m['id'],field,part));translated.append(part)
  m[field]='\n\n'.join(translated)
if untranslated:
 print(json.dumps(untranslated,ensure_ascii=False,indent=2));raise SystemExit('Missing explicit translations')
for name,data in [('scenarios',sc),('methods',me)]:
 old=json.loads((BASE/(name+'.json')).read_text());fields={'title','expected','target_condition'} if name=='scenarios' else {'description','preconditions','actions','evidence_expected'}
 def withouttext(d):
  stripped=json.loads(json.dumps(d))
  for item in stripped['items']:
   for f in fields:item.pop(f,None)
   if name=='methods' and 'transition_matrix' in item:item['transition_matrix'].pop('execution_rule',None)
  return stripped
 assert withouttext(old)==withouttext(data),'Non-text mutation '+name
 assert all(re.search('[\u4e00-\u9fff]',x[f]) for x in data['items'] for f in fields if f in x),'Missing Chinese prose'
 (ROOT/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Localized',len(sc['items']),'scenarios and',len(me['items']),'methods; non-text fields unchanged')
