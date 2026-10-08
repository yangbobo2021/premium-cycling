<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# DR-001: 首版候选业务需求的来源与边界

## 状态

已接受的文档编写决策；所列业务行为仍为候选需求草案，未经逐项业务批准。

## 背景

人类已确认本项目是销售自行车及自行车配件的高端出海独立站，首版中文需求最终服务于测试。
本项目尚无已确认的目标市场、品牌、付款方式、商业政策、真实商品数据或服务凭据。
参考材料为相邻 K.P 项目的 specs/requirements/、REQUEST.md 和 PRODUCTION_REQUEST.md；这些材料属于另一品牌和滑板品类，且含相互演进的演示与生产边界。

## 决策

- 将完整电商能力写成按共同业务意图组织的候选规约包；各包外部行为和验证均为设计约定，不表示已实现、已测试或已获逐项批准。
- 本次文档版本为候选 v0.1；该版本号标识审阅阶段，不代表正式业务基线。
- 仅继承参考材料的功能覆盖线索，不继承 K.P 品牌、滑板品类、美国／加拿大市场、英文站点、模拟支付、税费或退换政策，也不继承其技术和历史演示政策。
- 将自行车尺码与几何、配件兼容性、整车履约和维修保修作为本项目特有的候选行为；缺乏可靠数据时明确提示，不作尺寸或适配保证。
- 将未确定的经营参数作为配置和决策输入；在所需输入缺失时，不得把示例值伪装为可交易的正式报价或承诺。
- 已分配的规约条目 ID 可供将来确认和 JSON 需求快照使用；公开发布后遵守 ID 永不重新分配的规则。
- 未来测试资产目录由用户指定，建议默认项目 tests/；进入测试流程前先询问目录，本次不导出已确认 JSON 或创建测试台账。
- 跨包端到端组合由最终结果所在包承接验证设计：发现至付款与订单由 cart-checkout 负责，订单至送达由 orders-fulfillment 负责，订单至售后结案由 after-sales 负责，会话至处理接续由 customer-support 负责，上线配置至正式可交易状态由 launch-readiness 负责。

### 待定决策及影响范围

| 待定事项 | 主要影响包 |
| --- | --- |
| 目标国家／地区、站点语言、报价与结算币种 | market-catalog、cart-checkout、content-marketing、launch-readiness |
| 正式品牌、视觉资产与授权商品资料 | market-catalog、content-marketing、site-quality、launch-readiness |
| 真实或测试支付、支付服务、退款资金边界与对账 | cart-checkout、after-sales、orders-fulfillment、launch-readiness |
| 配送范围、服务、运费、税务规则、退货期限与费用承担 | cart-checkout、orders-fulfillment、after-sales、launch-readiness |
| 整车包装／组装责任、运输损坏处理、保修与维修承诺 | orders-fulfillment、after-sales、content-marketing、launch-readiness |
| 自行车类别、是否销售电助力车、配件类型及兼容数据来源 | market-catalog、product-selection、orders-fulfillment、after-sales |
| 积分是否上线、取得／兑换／过期数值及促销叠加 | customer-account、cart-checkout、content-marketing |
| 定制装配、经销商业务是否纳入后续范围 | market-catalog、product-selection、orders-fulfillment、merchant-operations |
| 客服时段、通知渠道、隐私与服务政策、数据保留期 | customer-support、site-quality、launch-readiness |

电助力车、定制装配和经销商能力仅是待定扩展范围，不构成首版交付要求。

## 影响

- 规约包以候选身份保持可审阅、可测试设计和稳定引用，后续业务确认可逐项接受、修订或撤销。
- 商家资料、授权素材、政策和外部服务缺失会限制正式交易或公开承诺，但不阻断需求文档编写。
- 后续确认实质性经营选择时，应记录相应决策并同步修订受影响的规约包与索引。
