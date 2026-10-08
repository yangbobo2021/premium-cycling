<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# launch-readiness: 商家上线就绪

## 意图

本候选包使商家能识别真实营业所需的数据、政策、素材和服务是否具备，避免用样例配置形成不实交易承诺。
它规定可观察的就绪状态，不宣称当前已具备任何真实商品或服务凭据。

## 外部行为

### launch-readiness-1

当有权员工查看上线就绪状态，商店应按市场列出品牌与语言、商品与库存、价格、授权素材、税、配送、适用整车组装责任、支付、售后政策、通知、客服和站点服务的配置状态，并标明缺项影响的商品变体与可服务目的地；未配置市场时应列出市场缺项。

### launch-readiness-2

当商店核验市场中的商品交易资格，商店应按每个拟售变体的已发布资料 [[market-catalog-5](market-catalog.md#market-catalog-5)]、当前市场价格 [[market-catalog-6](market-catalog.md#market-catalog-6)] 与可售库存 [[market-catalog-13](market-catalog.md#market-catalog-13)] 标示其真实交易就绪或缺项；市场无任何可交易变体时应标示市场无可交易商品。

### launch-readiness-3

当商品图片 [[market-catalog-9](market-catalog.md#market-catalog-9)] 或内容视频 [[content-marketing-4](content-marketing.md#content-marketing-4)] 缺少授权证明或来源记录，商店应标示对应商品素材或内容发布未就绪并指出待补资料；仅被交易引用的商品素材缺口阻断对应商品交易。

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

当样例或测试数据存在于商店，商店应使测试订单与正式订单、可售库存 [[market-catalog-11](market-catalog.md#market-catalog-11)]、限额优惠 [[content-marketing-13](content-marketing.md#content-marketing-13)]、积分 [[customer-account-19](customer-account.md#customer-account-19)]、评价和经营汇总 [[merchant-operations-12](merchant-operations.md#merchant-operations-12)] 隔离，并标示数据来源；正式商品资料仅可供测试流程只读引用。

### launch-readiness-10

当有权员工请求真实售卖就绪结论，商店应按市场、拟售商品变体及可服务目的地的组合核对商品与库存 [[launch-readiness-2](#launch-readiness-2)]、该商品所用授权素材 [[launch-readiness-3](#launch-readiness-3)]、该目的地及商品适用的税配送与售后政策 [[launch-readiness-4](#launch-readiness-4)]、适用整车组装责任与顾客指引 [[launch-readiness-15](#launch-readiness-15)]，并核对市场共同依赖的真实支付及退款服务 [[launch-readiness-5](#launch-readiness-5)]、通知客服 [[launch-readiness-6](#launch-readiness-6)]、运行恢复 [[launch-readiness-7](#launch-readiness-7)]，其他商业决策按其影响范围核对；仅通过的组合可标为真实售卖就绪，市场应分别显示全部、部分或无组合就绪及各缺项，测试支付不能满足真实售卖条件。

### launch-readiness-13

当有权员工请求测试流程就绪结论，商店应仅在可核对的测试报价 [[cart-checkout-10](cart-checkout.md#cart-checkout-10)]、显式测试付款 [[cart-checkout-18](cart-checkout.md#cart-checkout-18)]、隔离的测试库存与实际使用的权益可供下单 [[cart-checkout-22](cart-checkout.md#cart-checkout-22)] [[launch-readiness-9](#launch-readiness-9)] 和阻止测试订单真实交运 [[orders-fulfillment-13](orders-fulfillment.md#orders-fulfillment-13)] 均可核验时标示测试流程就绪，并与真实售卖就绪状态分开显示。

### launch-readiness-14

当顾客准备对市场、商品变体与收货目的地的组合发起真实收款，商店应仅允许该组合已通过真实售卖就绪核验 [[launch-readiness-10](#launch-readiness-10)] 的付款；未就绪组合应阻止收款并避免对公众宣称其可真实购买，已就绪组合不受其他商品或目的地缺项阻断；显式测试付款仍不得授权实物交运 [[orders-fulfillment-13](orders-fulfillment.md#orders-fulfillment-13)]。

### launch-readiness-15

当市场准备销售整车，商店应核对该车型的商家已确认组装责任、交付形态、可用于随货交付的顾客指引 [[orders-fulfillment-7](orders-fulfillment.md#orders-fulfillment-7)] 及购买前可见的组装说明与适用政策 [[market-catalog-17](market-catalog.md#market-catalog-17)] [[content-marketing-9](content-marketing.md#content-marketing-9)]；任一缺失应将该车型的真实售卖标为未就绪并列出缺项，未销售整车的市场不以此项阻断。

## 验证

### launch-readiness-11

当在系统或集成环境执行上线检查情形矩阵，验证者应逐项断言状态与阻断结果：

| 情形 | 断言 |
| --- | --- |
| 查看部分就绪市场及未设市场 | 各类输入状态、受影响变体与目的地或市场缺项逐项可见 [[launch-readiness-1](#launch-readiness-1)] |
| 同市场一变体缺少资料、价格或库存及市场无可交易变体 | 仅缺项变体未就绪；无可交易变体时市场无商品可卖 [[launch-readiness-2](#launch-readiness-2)] |
| 一商品素材或非交易内容视频缺少授权 | 对应素材或内容待补，非交易内容不阻断其他商品 [[launch-readiness-3](#launch-readiness-3)] |
| 缺少税、配送或售后规则 | 受影响交易未就绪且缺口明确 [[launch-readiness-4](#launch-readiness-4)] |
| 真实服务有效、测试模式明确及配置缺失 | 真实／测试支付就绪状态分离且缺项明确 [[launch-readiness-5](#launch-readiness-5)] |
| 通知或客服渠道缺配置 | 受影响联系路径标未就绪 [[launch-readiness-6](#launch-readiness-6)] |
| 运行服务或恢复结果缺失 | 对应风险及待办可见 [[launch-readiness-7](#launch-readiness-7)] |
| 完成输入后重查 | 时间、结果、责任人及状态更新 [[launch-readiness-8](#launch-readiness-8)] |
| 测试订单引用正式商品资料并尝试占正式库存、优惠或积分 | 只读资料可用，正式资源与统计不受影响，缺少隔离资源时测试下单受阻 [[launch-readiness-9](#launch-readiness-9)] |
| 同市场一个目的地缺配送规则、一车型缺组装指引、另一组合完整；仅测试付款或市场共同条件缺失 | 完整组合仍就绪；缺项组合受阻；共同条件缺失时全市场无组合就绪 [[launch-readiness-10](#launch-readiness-10)] |
| 整车组装责任、交付形态、顾客指引或购买前政策缺失；仅售配件 | 有整车缺项则受影响车型未就绪，配件市场不受整车组装门槛阻断 [[launch-readiness-15](#launch-readiness-15)] |
| 显式测试付款与测试数据隔离 | 测试就绪独立显示且无实物交运授权 [[launch-readiness-13](#launch-readiness-13)] |
| 局部组合未就绪且其他组合就绪 | 仅未就绪组合的真实收款与公开购买承诺受阻，测试付款不授权交运 [[launch-readiness-14](#launch-readiness-14)] |

### launch-readiness-12

当在系统环境执行从缺少商家输入到补齐配置的组合路径，验证者应断言初始阻断项按市场、商品及目的地列出 [[launch-readiness-1](#launch-readiness-1)]、补齐输入后记录核验结果 [[launch-readiness-8](#launch-readiness-8)]，且真实售卖的各组合与测试流程分别按其条件给出结论 [[launch-readiness-10](#launch-readiness-10)] [[launch-readiness-13](#launch-readiness-13)]。
