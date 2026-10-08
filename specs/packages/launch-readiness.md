<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# launch-readiness: 商家上线就绪

## 意图

本候选包使商家能识别真实营业所需的数据、政策、素材和服务是否具备，避免用样例配置形成不实交易承诺。
它规定可观察的就绪状态，不宣称当前已具备任何真实商品或服务凭据。

## 外部行为

### launch-readiness-1

当有权员工查看上线就绪状态，商店应按市场列出品牌与语言、商品与库存、价格、授权素材、税、配送、支付、售后政策、通知、客服和站点服务的配置状态；未配置市场时应列出市场缺项。

### launch-readiness-2

当市场缺少可售商品真实资料、价格或库存，商店应标示该市场商品交易未就绪并指出缺项。

### launch-readiness-3

当商品图片或视频缺少授权证明或来源记录，商店应标示正式素材未就绪并指出待补资料。

### launch-readiness-4

当市场缺少已确认税务、配送或售后规则，商店应标示受影响的目的地或商品交易未就绪，并指出规则缺口。

### launch-readiness-5

当真实支付模式缺少可用服务配置或测试模式未明确标示，商店应标示支付未就绪及缺失的确认资料。

### launch-readiness-6

当通知或客服渠道缺少可用配置，商店应显示对应服务未就绪及受影响的顾客联系路径。

### launch-readiness-7

当域名、公开服务、访问控制、备份或恢复验证缺少可核验结果，商店应在就绪状态中指出对应运行风险及待办。

### launch-readiness-8

当商家完成一项就绪输入，商店应重新核验相关状态并保留验证时间、结果和责任人。

### launch-readiness-9

当样例或测试数据存在于商店，商店应使其与正式商品、订单、库存、评价、积分和经营汇总隔离，并标示数据来源。

### launch-readiness-10

当有权员工请求正式上线结论，商店应只在所有适用阻断项通过且影响交易的人工决策已确认后给出就绪状态，否则列出未完成事项。

## 验证

### launch-readiness-11

当在系统或集成环境执行上线检查情形矩阵，验证者应逐项断言状态与阻断结果：

| 情形 | 断言 |
| --- | --- |
| 查看市场就绪页及未设市场 | 各类输入状态或市场缺项逐项可见 [[launch-readiness-1](#launch-readiness-1)] |
| 缺少商品、价格或库存 | 市场交易未就绪且缺项准确 [[launch-readiness-2](#launch-readiness-2)] |
| 缺少素材授权 | 正式素材未就绪且待补资料明确 [[launch-readiness-3](#launch-readiness-3)] |
| 缺少税、配送或售后规则 | 受影响交易未就绪且缺口明确 [[launch-readiness-4](#launch-readiness-4)] |
| 真实支付缺配置或测试模式未标示 | 支付未就绪且缺失资料明确 [[launch-readiness-5](#launch-readiness-5)] |
| 通知或客服渠道缺配置 | 受影响联系路径标未就绪 [[launch-readiness-6](#launch-readiness-6)] |
| 运行服务或恢复结果缺失 | 对应风险及待办可见 [[launch-readiness-7](#launch-readiness-7)] |
| 完成输入后重查 | 时间、结果、责任人及状态更新 [[launch-readiness-8](#launch-readiness-8)] |
| 样例和测试数据并存 | 正式记录与统计不受污染 [[launch-readiness-9](#launch-readiness-9)] |
| 全通过、有阻断项及人工决策待定 | 仅全部完成时正式就绪，否则列出未完成项 [[launch-readiness-10](#launch-readiness-10)] |

### launch-readiness-12

当在系统环境执行从缺少商家输入到补齐配置的组合路径，验证者应断言初始阻断项按市场列出 [[launch-readiness-1](#launch-readiness-1)]、补齐输入后记录核验结果 [[launch-readiness-8](#launch-readiness-8)]，且正式就绪结论只在适用阻断项全部通过后给出 [[launch-readiness-10](#launch-readiness-10)]。
