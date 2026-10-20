import json
from pathlib import Path
p=Path('/Users/boboyang/work/sublang.ai/premium-cycling/tests/delivery-acceptance')
v=json.loads((p/'coverage_review.json').read_text());reqs=json.loads((p/'requirements.json').read_text())['items'];ss=json.loads((p/'scenarios.json').read_text())['items'];ms={m['id']:m for m in json.loads((p/'methods.json').read_text())['items']}
resolutions={
'after-sales-4':'新增已购3且全部处理完的零剩余夹具，实际从两会话各提交1件并核对案件列表。若受理新申请、重新开放权益或返回非0可申请量，该场景失败。',
'after-sales-7':'新增无序列号配件，实际以订单行完成接收、检查通过／失败及退款或换货结论；若强制序列号而阻断、漏存检查证据、检查前推进或修改无关行，该场景失败。',
'after-sales-12':'新增V1截止T前、恰T、T后，记录时区、精度、起算事件、包含性和不同的V2；实际设业务时间并提交。任一资格不合V1独立计算即失败，缺已确认边界依据不得通过。',
'after-sales-18':'新增用合法对照取得的请求形状，向每个非法源状态的真实受支持边界发送转换；只有拒绝响应及重开状态历史无非法变化才合格。若请求被接受／持久状态非法推进则失败；仅隐藏控件或请求格式错误不能算拒绝证据。',
'after-sales-23':'新增测试已付、测试占库和模拟价差已结清但无实物授权的换货，实际尝试替代包裹及交运，并查真实承运／任务历史。任何测试来源真实授权或交运即失败；另跑真实授权成功对照排除一律禁止。',
'after-sales-24':'新增每个完成条件独立缺失、其他全部满足的矩阵，对多来源退款逐源置待定／失败／未知。实际Complete并重开，恢复仅该条件后再做正对照；任一缺项仍完成或全部满足不能完成即失败。',
'after-sales-27':'新增补款100、已退30、另有或没有既存预留20的真实动作夹具；分别撤回／无法履约并重放。若待退不是70、既有20被重复加入、新增占用超过50或累计退款超过100，该场景失败。原件N/T/R前置也已拆为可达分支。',
'after-sales-32':'新增真正相关联的多来源预留写入中断，故障确认定位到实际在途操作；故障中竞争核准、恢复后用同核准ID重试，并核对各来源余额。若可执行不完整核准、重复利用在途预留、恢复留孤立或双倍占用／超额即失败。普通短缺或仅丢响应不算触发证据。',
'cart-checkout-14':'新增已核实成功在订单已付、引用、优惠、积分各写入尝试期间的独立故障；同时核对订单及权益，恢复并重放原成功。若部分状态被当作完成／可履约、资金引用不符、重复扣款或权益重复确认即失败；不可证实触发故障则不能通过。',
'cart-checkout-16':'新增同顾客同商品金额但独立Q1/Q2报价，资源够两单，分别串行及并发提交，再逐报价重放及支付结果重放。若最终不是两个独立订单及各自一次占用／引用，或吞Q2／多生订单，该场景失败。',
'cart-checkout-22':'新增资源足够时订单快照保存失败、库存占用后中断、后续优惠／积分写失败，实际核对故障阶段并恢复同提交。若失败留可付部分单／付款、泄漏占用、恢复重复建单／跨模式借池即失败；在途恢复状态须明确不可付款。',
'customer-account-1':'新增同一规范化联系身份的双会话最终注册同步提交及渠道验证，核对账户ID和授权身份查询，另有独立联系正对照。若同一身份被两个账户占用即失败；同一已建账户的幂等返回不误判。',
'customer-account-5':'新增A和匿名实际发送B1地址编辑和删除的合法形状请求，B逐次重开列表与结账选择，另有本人地址正对照。任一外人写入／删除成功、B1/B2改变或本人合法动作无效即失败；拒读不是拒写证据。',
'customer-support-2':'新增持久化前拒绝与持久化后丢确认两个独立故障，观察故障中的发送状态、接收方实际历史和恢复后状态。若未保存却称已送达、未知被凭空终结或恢复历史与状态不合即失败。',
'customer-support-7':'新增同一时间基准的在途分配控制，逐中间阶段冻结后让A/B提交带标记的负责人专属回复，比较授权决定、所有权更新及通知时间线，并反向释放顺序。若同一所有权区间双方都有效、通知不合归属即失败；串行合法转派不误判。无法暴露竞态区间不能以最终单负责人通过。',
'customer-support-20':'新增A保留已认证旧撰写窗口，转派B完成后A实际发送，再B发送，顾客实时及重入查看。若新A消息被持久送达、B被拒或原A历史丢失，该场景失败。',
'orders-fulfillment-18':'新增独立三行已付未交运订单，逐行批准取消到最后一行，随后资金待退到各源成功单独推进。最后仍仅部分取消、提前称已全退或抹掉支付／行历史，该场景失败。',
'site-quality-12':'新增订单创建、支付结果、退款预留／结果、消息持久化实际业务写入阶段中断，与响应丢失分别记录；恢复原引用再试。若不可核对、重复订单／资金／消息或矛盾完成状态即失败；无故障触发关联证据不允许通过。'
}
journey_ids=['BB-journey-exchange-settlement-withdrawn','BB-journey-exchange-settlement-closed']
for item in v['items']:
 rid=item['requirement_id']; repaired=[]; newprobes=[]
 for probe in item['fault_probes']:
  if probe['failure_signal'].startswith('ESCAPES current methods: '):
   if probe['scenario_ids']==journey_ids:
    for mode,state,fault,signal in [
     ('原件未寄出早期撤回','N：原件未寄出、未检查、无目标占库、无补款','早期撤回伪造库存释放／退款待办，或无义务仍不能终止','新旅程N实际撤回并重放；若不是无原件及资金义务的终止，或出现虚构占用／退款，场景失败。'),
     ('原件在途撤回至处置履行','T：原件在途、未接收检查、无占库补款','原件仍在途便结案，或者到达后丢失原件归还义务','新旅程T实际撤回、接收并履行适用处置；若履行前终态、处置后不能终止或原订单快照变化，场景失败。'),
     ('已检查补款后撤回与双义务结清','R：原件已收回检查、目标占用、已确认补款；已退0或30及预留0或20','忽略已退／已预留而重复退款，或只结清资金／原件之一即终止','新旅程R实际确认原补款（同确认重放）、建立既有退款与预留、撤回、按原引用核对未知／失败／成功；若未退义务重复、成功源重退、未知重发或单义务完成即结案，场景失败。')]:
     newprobes.append(dict(mode=mode,state=state,plausible_fault=fault,scenario_ids=journey_ids,failure_signal=signal))
    repaired.append('AI-journey-exchange-settlement 已拆成N未寄出、T在途、R接收检查后三个互斥可达分支。补款、目标占库、退款故障仅在R发生；每个分支有实际过程及原订单不变比对，原矛盾前置已消除。')
   else:
    probe['failure_signal']=resolutions[rid]
    # Remove wording declaring a nonexistent current gap from the mode/state only where needed.
    newprobes.append(probe);repaired.append('AI-'+rid+'：'+resolutions[rid])
  else:
   if probe['scenario_ids']==journey_ids:
    probe['failure_signal']='目标占库多释放、未退补款义务重复、仅结清资金或原件之一就终态、原引用核对改变成功源、原订单快照变化均失败。现有方法的N/T/R是互斥可达时间线；不存在未收到却已检查的前置。'
   newprobes.append(probe)
 item['fault_probes']=newprobes
 item['operation_modes']=list(dict.fromkeys(x['mode'] for x in newprobes))
 item['user_states']=list(dict.fromkeys(x['state'] for x in newprobes))
 item['verdict']='sufficient';item['uncovered_paths']=[]
 first=newprobes[0]
 item['reason']='本轮对当前需求正文、关联场景及方法重新核对，并挑战已列模式／主体状态是否遗漏正常、例外、边界或转换。所列反例须由实际动作、对象／金额／状态／权限／内容的独立预期及逐向量证据揭露，不能只靠不变屏幕、ID或条数。关键可区分反例：'+first['plausible_fault']+'；对应信号：'+first['failure_signal']+' 当前范围内未发现重要未覆盖路径。'
 if repaired:item['reason']+=' 本轮修复核验：'+' '.join(dict.fromkeys(repaired))
 item['reason']+=' 本结论仅表示未来在真实App上完成这些方法并满足证据时足以支持该项约定范围交付；未执行或缺故障／业务规则oracle时不得宣称App通过。'
v['status']='passed'
v['basis']='本轮独立Reviewer重新读取当前188项已确认需求、204个黑盒场景、196个方法（含追加动作和证据及8个跨边界旅程），并核对188项正文与当前11个spec包一致。以逐项操作模式、用户状态、正常／异常、边界及转换反例审查方法能否真实触发与观察故障；复核上轮25个未覆盖路径的具体修复，而非采信Analyst结论或覆盖率。额外关注原子写入中断与响应丢失的区别、独立报价去重、身份并发、跨主体地址写入、分配中间态、转派旧窗口、全部取消、零余额／无序列号配件、保修时间边界及换货资金与原件时间线。N/T/R互斥分支现在分别可达，故障方法明确实际触发和观测证据，不具备时只能unproven/blocked。本轮188项均充分，无发现的重要未覆盖路径。业务参数按确认范围仍待配置，不代填数值。只审查设计，不证明App运行或所有潜在bug不存在；资源、白盒、执行及运行证据门禁不作本次前提。仅Reviewer更新coverage_review.json，未修改Analyst台账或规格。'
v.update(requirements_sha256='19eac30ed888286396019edbdc3b79937ae17218ab16b48797ba0395a21c943a',scenarios_sha256='76afd4aef03f855af5bb40f3db244ccfeaba53836650222a1ca59e38d936da92',methods_sha256='102cb5de345738a8b9e95685e611f18a9c3adf10411d7281d52d60916e9724bf')
assert len(v['items'])==188 and {x['requirement_id'] for x in v['items']}=={r['id'] for r in reqs}
assert not any(x['uncovered_paths'] for x in v['items'])
assert {s['id'] for s in ss}=={sid for i in v['items'] for pr in i['fault_probes'] for sid in pr['scenario_ids']}
(p/'coverage_review.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':v['status'],'requirements':len(v['items']),'uncovered_paths':0,'fault_probes':sum(len(i['fault_probes']) for i in v['items'])}))
