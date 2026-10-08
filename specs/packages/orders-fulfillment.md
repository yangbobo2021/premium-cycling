<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# orders-fulfillment: 订单与履约

## 意图

本候选包使顾客和员工以不被后续配置改写的订单记录跟踪自行车及配件的实际履约。
整车包装、组装、承运和损坏处理政策仍待商家确认。

## 外部行为

### orders-fulfillment-1

当结账提交已确认报价并建立待付款订单 [[cart-checkout-22](cart-checkout.md#cart-checkout-22)]，订单系统应保存下表所列不可变的成交快照：

| 快照部分 | 必需内容 |
| --- | --- |
| 订单身份 | 编号、购买人或游客联系途径、提交时间 |
| 商品行 | 确切变体 [[market-catalog-6](market-catalog.md#market-catalog-6)]、数量、成交单价和币种 |
| 行金额 | 优惠分摊 [[content-marketing-7](content-marketing.md#content-marketing-7)]、积分抵扣分摊 [[customer-account-12](customer-account.md#customer-account-12)]、税额与计税依据 [[cart-checkout-10](cart-checkout.md#cart-checkout-10)]，以及多件同一订单行按件分摊和尾差归属 |
| 配送 | 收货地址、所选服务、费用、预计时效 [[cart-checkout-8](cart-checkout.md#cart-checkout-8)]、适用费用分摊规则 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)] 及逐行按件实际分摊金额 |
| 成交与政策 | 最终应付总额 [[cart-checkout-10](cart-checkout.md#cart-checkout-10)]、支付模式 [[cart-checkout-13](cart-checkout.md#cart-checkout-13)]、适用规则和政策版本 [[content-marketing-9](content-marketing.md#content-marketing-9)] |

### orders-fulfillment-2

当商品资料、价格或政策在下单后改变，订单系统应保留原订单快照而不以新配置覆写历史。

### orders-fulfillment-3

当已核验订单归属的游客 [[customer-account-3](customer-account.md#customer-account-3)]、已登录且订单归属本人的会员 [[customer-account-7](customer-account.md#customer-account-7)] 或有权员工 [[merchant-operations-3](merchant-operations.md#merchant-operations-3)] 查询订单，订单系统应展示其可访问的当前支付、履约及售后状态和事件时间。

### orders-fulfillment-4

当支付、履约或售后事件推进订单记录，订单系统应按下表分别保存对应状态、操作者或事件来源、原因与时间，并拒绝表外跳转：

| 状态维度 | 允许的变化 |
| --- | --- |
| 支付 | 待付款 → 结果待核对／已付款／付款失败／已失效／已关闭（全部未付款行取消）；结果待核对 → 已付款／付款失败；付款失败与已失效为终态，重试建立关联的新待付款订单 [[cart-checkout-17](cart-checkout.md#cart-checkout-17)]；已付款结果不因退款倒退 [[cart-checkout-14](cart-checkout.md#cart-checkout-14)] [[cart-checkout-15](cart-checkout.md#cart-checkout-15)] [[cart-checkout-23](cart-checkout.md#cart-checkout-23)] [[cart-checkout-25](cart-checkout.md#cart-checkout-25)] [[after-sales-2](after-sales.md#after-sales-2)] |
| 订单行履约 | 待付款 → 待履约（确认付款后）／已取消（付款前取消）；待履约 → 拣货中 → 已打包 → 已交运 → 已送达；未交运的行可按批准取消转为已取消 [[after-sales-2](after-sales.md#after-sales-2)]；已交运行不得直接取消 |
| 包裹配送 | 待交运 → 已交运 → 已送达；运输异常作为带证据的标记，不代替送达事件 |
| 退款 | 每行未退款 → 部分退款 → 已退款；仅在退款成功结果被确认 [[after-sales-25](after-sales.md#after-sales-25)] 后推进，不改写原支付成功记录或既有交运历史 |
| 售后 | 案件状态单独记录 [[after-sales-18](after-sales.md#after-sales-18)]，不将申请中直接解释为订单已取消或已退款 |

### orders-fulfillment-5

当履约人员开始处理已具备付款确认 [[cart-checkout-14](cart-checkout.md#cart-checkout-14)] 且非结果待核对 [[cart-checkout-23](cart-checkout.md#cart-checkout-23)] 的订单，订单系统应按实物履约授权记录每个整车或配件订单行的拣货与待发状态。

### orders-fulfillment-6

当履约人员包装整车，订单系统应记录适用的包装检查项目、完成者和异常结果。

### orders-fulfillment-7

当整车按已公布的组装与保修政策 [[content-marketing-9](content-marketing.md#content-marketing-9)] 交付，订单系统应记录需由商家完成或需顾客完成的组装事项及随货指引。

### orders-fulfillment-8

当同一订单包含整车与配件，订单系统应允许分别记录包裹和履约状态，且顾客可识别各商品的预计到达情况。

### orders-fulfillment-9

当包裹被交运，订单系统应保存承运服务、跟踪标识、交运时间和来源证据，并向顾客展示更新时间。

### orders-fulfillment-10

当承运状态不可获得或更新失败，订单系统应标示跟踪信息的来源与最后更新时间，而不声称已送达。

### orders-fulfillment-11

当包裹有可核实的送达事件，订单系统应记录送达时间与来源，并更新相应包裹而非无关包裹的状态。

### orders-fulfillment-12

当顾客报告运输损坏，订单系统应保存所涉包裹、商品、证据和报告时间，并提供可跟踪的售后处理入口 [[after-sales-3](after-sales.md#after-sales-3)]。

### orders-fulfillment-13

给定订单的支付方式为测试模式 [[cart-checkout-18](cart-checkout.md#cart-checkout-18)]，当员工尝试生成真实交运任务，订单系统应阻止将测试支付结果当作实物交运授权。

### orders-fulfillment-14

当履约动作重复提交，订单系统应避免重复拣货、交运或送达事件影响同一包裹状态。

### orders-fulfillment-18

当订单含多个订单行或包裹，订单系统应根据各行与包裹的实际状态展示部分或全部交运、送达及取消结果，并单独显示退款和售后状态，不以汇总状态覆盖历史事件。

### orders-fulfillment-19

当已完成资格与占库核对的换货案件 [[after-sales-23](after-sales.md#after-sales-23)] 请求替代商品履约，订单系统应创建关联原订单行、目标变体与售后案件的独立包裹，并按该包裹的实际交运与送达事件推进状态。

## 验证

### orders-fulfillment-15

当在集成环境执行订单状态情形矩阵，验证者应逐项断言持久结果：

| 情形 | 断言 |
| --- | --- |
| 建立含多件商品的待付款订单 | 快照含商品、逐行及按件费用分摊与尾差归属、税务依据、地址、配送费与时效、总额、模式及规则版本 [[orders-fulfillment-1](#orders-fulfillment-1)] |
| 变更商品与政策 | 历史快照不变 [[orders-fulfillment-2](#orders-fulfillment-2)] |
| 顾客和员工查单 | 仅授权内容与事件时间可见 [[orders-fulfillment-3](#orders-fulfillment-3)] |
| 付款失败／待核对、部分交运、取消、退款及售后申请 | 各状态维度按表推进且非法跳转被拒绝 [[orders-fulfillment-4](#orders-fulfillment-4)] |
| 分行拣货 | 仅目标订单行进入待发状态 [[orders-fulfillment-5](#orders-fulfillment-5)] |
| 测试支付请求真实交运 | 实物交运任务被阻止 [[orders-fulfillment-13](#orders-fulfillment-13)] |
| 重复提交履约动作 | 包裹状态和事件不重复 [[orders-fulfillment-14](#orders-fulfillment-14)] |
| 多行分批履约及部分取消 | 汇总与细项一致，退款和售后独立可见 [[orders-fulfillment-18](#orders-fulfillment-18)] |
| 经授权的换货包裹 | 原订单行、目标变体与售后案件关联且状态独立 [[orders-fulfillment-19](#orders-fulfillment-19)] |

### orders-fulfillment-16

当在系统或集成环境执行整车与配件配送情形矩阵，验证者应逐项断言业务记录：

| 情形 | 断言 |
| --- | --- |
| 包装整车 | 检查项目、人员和异常可见 [[orders-fulfillment-6](#orders-fulfillment-6)] |
| 不同组装责任 | 随货指引对应已公布责任 [[orders-fulfillment-7](#orders-fulfillment-7)] |
| 整车与配件分包 | 各行包裹状态和到达情况独立 [[orders-fulfillment-8](#orders-fulfillment-8)] |
| 交运 | 承运、跟踪、时间、来源与顾客视图一致 [[orders-fulfillment-9](#orders-fulfillment-9)] |
| 跟踪来源失效 | 显示来源与最后更新时间，不误报送达 [[orders-fulfillment-10](#orders-fulfillment-10)] |
| 单包裹送达 | 仅该包裹更新且有事件来源 [[orders-fulfillment-11](#orders-fulfillment-11)] |
| 顾客报告损坏 | 包裹、商品、证据和处理入口可追踪 [[orders-fulfillment-12](#orders-fulfillment-12)] |

### orders-fulfillment-17

当在系统环境执行从已成立订单到整车及配件分别送达的组合路径，验证者应断言原订单快照保持不变 [[orders-fulfillment-2](#orders-fulfillment-2)]、各行可独立拣货及分包 [[orders-fulfillment-5](#orders-fulfillment-5)] [[orders-fulfillment-8](#orders-fulfillment-8)]、交运证据可查 [[orders-fulfillment-9](#orders-fulfillment-9)]，且送达只更新有证据的包裹 [[orders-fulfillment-11](#orders-fulfillment-11)]。
