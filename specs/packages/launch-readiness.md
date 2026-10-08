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

当市场缺少已发布商品资料 [[market-catalog-5](market-catalog.md#market-catalog-5)]、当前市场价格 [[market-catalog-6](market-catalog.md#market-catalog-6)] 或可售库存 [[market-catalog-13](market-catalog.md#market-catalog-13)]，商店应标示该市场商品交易未就绪并指出缺项。

### launch-readiness-3

当商品图片 [[market-catalog-9](market-catalog.md#market-catalog-9)] 或内容视频 [[content-marketing-4](content-marketing.md#content-marketing-4)] 缺少授权证明或来源记录，商店应标示正式素材未就绪并指出待补资料。

### launch-readiness-4

当市场缺少已生效税务、配送或售后规则 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)]，商店应标示受影响的目的地或商品交易未就绪，并指出结账阻断条件 [[cart-checkout-12](cart-checkout.md#cart-checkout-12)]。

### launch-readiness-5

当有权员工检查结账所用支付配置 [[cart-checkout-13](cart-checkout.md#cart-checkout-13)]，商店应按已选择的支付模式分别标示真实收款或测试付款的就绪状态及缺失的确认资料：

| 支付配置 | 就绪结果 |
| --- | --- |
| 真实支付服务已核验且资金与退款路径 [[after-sales-9](after-sales.md#after-sales-9)] [[after-sales-25](after-sales.md#after-sales-25)] 可用 | 可供真实售卖就绪检查使用 |
| 测试支付已明确标示 [[cart-checkout-18](cart-checkout.md#cart-checkout-18)] | 仅可供测试流程就绪检查使用 |
| 模式未确认、真实服务不可用或测试标示缺失 | 对应支付流程未就绪 |

### launch-readiness-6

当通知发送渠道 [[customer-support-10](customer-support.md#customer-support-10)] 或客服联系途径 [[customer-support-1](customer-support.md#customer-support-1)] 缺少可用配置，商店应显示对应服务未就绪及受影响的顾客联系路径。

### launch-readiness-7

当域名与公开服务、私有资料访问控制 [[site-quality-8](site-quality.md#site-quality-8)]、备份结果 [[site-quality-14](site-quality.md#site-quality-14)] 或恢复验证 [[site-quality-17](site-quality.md#site-quality-17)] 缺少可核验结果，商店应在就绪状态中指出对应运行风险及待办。

### launch-readiness-8

当商家完成一项就绪输入，商店应重新核验相关状态并保留验证时间、结果和责任人。

### launch-readiness-9

当样例或测试数据存在于商店，商店应使其与正式商品、订单、库存、评价、积分和经营汇总 [[merchant-operations-12](merchant-operations.md#merchant-operations-12)] 隔离，并标示数据来源。

### launch-readiness-10

当有权员工请求真实售卖就绪结论，商店应仅在商品与库存 [[launch-readiness-2](#launch-readiness-2)]、授权素材 [[launch-readiness-3](#launch-readiness-3)]、税配送及售后政策 [[launch-readiness-4](#launch-readiness-4)]、真实支付及退款服务 [[launch-readiness-5](#launch-readiness-5)]、通知客服 [[launch-readiness-6](#launch-readiness-6)]、运行恢复 [[launch-readiness-7](#launch-readiness-7)] 和适用商业决策均通过后给出就绪状态，否则列出未完成事项；测试支付不能满足真实售卖条件。

### launch-readiness-13

当有权员工请求测试流程就绪结论，商店应仅在可核对的测试报价 [[cart-checkout-10](cart-checkout.md#cart-checkout-10)]、显式测试付款 [[cart-checkout-18](cart-checkout.md#cart-checkout-18)]、测试数据隔离 [[launch-readiness-9](#launch-readiness-9)] 和阻止测试订单真实交运 [[orders-fulfillment-13](orders-fulfillment.md#orders-fulfillment-13)] 均可核验时标示测试流程就绪，并与真实售卖就绪状态分开显示。

### launch-readiness-14

当市场未达到真实售卖就绪状态 [[launch-readiness-10](#launch-readiness-10)]，商店应阻止新的真实收款并避免对公众宣称可真实购买；已就绪的显式测试流程可独立标示，测试付款不授权实物交运 [[orders-fulfillment-13](orders-fulfillment.md#orders-fulfillment-13)]。

## 验证

### launch-readiness-11

当在系统或集成环境执行上线检查情形矩阵，验证者应逐项断言状态与阻断结果：

| 情形 | 断言 |
| --- | --- |
| 查看市场就绪页及未设市场 | 各类输入状态或市场缺项逐项可见 [[launch-readiness-1](#launch-readiness-1)] |
| 缺少商品、价格或库存 | 市场交易未就绪且缺项准确 [[launch-readiness-2](#launch-readiness-2)] |
| 缺少素材授权 | 正式素材未就绪且待补资料明确 [[launch-readiness-3](#launch-readiness-3)] |
| 缺少税、配送或售后规则 | 受影响交易未就绪且缺口明确 [[launch-readiness-4](#launch-readiness-4)] |
| 真实服务有效、测试模式明确及配置缺失 | 真实／测试支付就绪状态分离且缺项明确 [[launch-readiness-5](#launch-readiness-5)] |
| 通知或客服渠道缺配置 | 受影响联系路径标未就绪 [[launch-readiness-6](#launch-readiness-6)] |
| 运行服务或恢复结果缺失 | 对应风险及待办可见 [[launch-readiness-7](#launch-readiness-7)] |
| 完成输入后重查 | 时间、结果、责任人及状态更新 [[launch-readiness-8](#launch-readiness-8)] |
| 样例和测试数据并存 | 正式记录与统计不受污染 [[launch-readiness-9](#launch-readiness-9)] |
| 真实服务全通过、仅测试付款及人工决策待定 | 仅真实售卖条件全部完成时就绪 [[launch-readiness-10](#launch-readiness-10)] |
| 显式测试付款与测试数据隔离 | 测试就绪独立显示且无实物交运授权 [[launch-readiness-13](#launch-readiness-13)] |
| 市场真实售卖未就绪 | 新真实收款受阻、无公开购买承诺且测试付款不授权交运 [[launch-readiness-14](#launch-readiness-14)] |

### launch-readiness-12

当在系统环境执行从缺少商家输入到补齐配置的组合路径，验证者应断言初始阻断项按市场列出 [[launch-readiness-1](#launch-readiness-1)]、补齐输入后记录核验结果 [[launch-readiness-8](#launch-readiness-8)]，且真实售卖与测试流程分别按其条件给出结论 [[launch-readiness-10](#launch-readiness-10)] [[launch-readiness-13](#launch-readiness-13)]。
