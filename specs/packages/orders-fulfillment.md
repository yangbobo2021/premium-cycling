<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# orders-fulfillment: 订单与履约

## 意图

本候选包使顾客和员工以不被后续配置改写的订单记录跟踪自行车及配件的实际履约。
整车包装、组装、承运和损坏处理政策仍待商家确认。

## 外部行为

### orders-fulfillment-1

当结账形成有效订单 [[cart-checkout-14](cart-checkout.md#cart-checkout-14)]，订单系统应保存编号、购买人或游客联系途径、商品与确切变体、数量、成交价格、币种、优惠、税费、地址、配送选择、支付模式及政策版本的快照。

### orders-fulfillment-2

当商品资料、价格或政策在下单后改变，订单系统应保留原订单快照而不以新配置覆写历史。

### orders-fulfillment-3

当已核验订单归属的顾客 [[customer-account-3](customer-account.md#customer-account-3)] 或有权员工 [[merchant-operations-3](merchant-operations.md#merchant-operations-3)] 查询订单，订单系统应展示其可访问的当前支付、履约及售后状态和事件时间。

### orders-fulfillment-4

当业务动作推进订单状态，订单系统应按已定义的合法转换保存新状态、操作者、原因和时间，并拒绝无依据的跳转。

### orders-fulfillment-5

当履约人员开始处理已具备付款确认 [[cart-checkout-14](cart-checkout.md#cart-checkout-14)] 和履约授权的订单，订单系统应记录每个整车或配件订单行的拣货与待发状态。

### orders-fulfillment-6

当履约人员包装整车，订单系统应记录适用的包装检查项目、完成者和异常结果。

### orders-fulfillment-7

当整车按已公布的组装责任交付，订单系统应记录需由商家完成或需顾客完成的组装事项及随货指引。

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

## 验证

### orders-fulfillment-15

当在集成环境执行订单状态情形矩阵，验证者应逐项断言持久结果：

| 情形 | 断言 |
| --- | --- |
| 完成有效结账 | 订单快照含商品、费用、地址、模式及政策版本 [[orders-fulfillment-1](#orders-fulfillment-1)] |
| 变更商品与政策 | 历史快照不变 [[orders-fulfillment-2](#orders-fulfillment-2)] |
| 顾客和员工查单 | 仅授权内容与事件时间可见 [[orders-fulfillment-3](#orders-fulfillment-3)] |
| 合法及非法状态操作 | 合法变更可追溯，非法跳转被拒绝 [[orders-fulfillment-4](#orders-fulfillment-4)] |
| 分行拣货 | 仅目标订单行进入待发状态 [[orders-fulfillment-5](#orders-fulfillment-5)] |
| 测试支付请求真实交运 | 实物交运任务被阻止 [[orders-fulfillment-13](#orders-fulfillment-13)] |
| 重复提交履约动作 | 包裹状态和事件不重复 [[orders-fulfillment-14](#orders-fulfillment-14)] |

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
