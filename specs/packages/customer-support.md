<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# customer-support: 客服与通知

## 意图

本候选包使顾客在线或离线获得可接续的帮助，并通过可用渠道获知订单和售后进展。
客服时段、通知渠道及留存期仍待商家确认。

## 外部行为

### customer-support-1

当顾客打开客服入口，客服系统应如实显示在线或离线状态及可用联系途径。

### customer-support-2

给定客服在线，当顾客发送实时消息，客服系统应将消息持久送达会话并向双方显示发送状态。

### customer-support-3

给定客服离线，当顾客留下消息和可用联系渠道，客服系统应保存待跟进会话并说明后续回复方式。

### customer-support-4

当顾客断线后重新进入会话，客服系统应在身份核验后恢复其可访问的消息历史。

### customer-support-5

当顾客请求将会话关联订单，客服系统应验证其订单归属 [[customer-account-3](customer-account.md#customer-account-3)] 并只向有权客服展示必要的订单摘要。

### customer-support-6

当新会话进入队列，客服系统应将其标为待分配并使有权人员可见。

### customer-support-7

当有权主管或客服分配会话，客服系统应在同一时点只记录一位负责人并通知该负责人。

### customer-support-8

当有权人员转派会话，客服系统应保存原负责人、接手人、原因和时间，并将未处理状态交给新负责人。

### customer-support-9

当客服结束会话后顾客继续发送消息，客服系统应恢复待跟进状态并保留原历史。

### customer-support-10

当订单状态 [[orders-fulfillment-4](orders-fulfillment.md#orders-fulfillment-4)]、付款结果 [[cart-checkout-14](cart-checkout.md#cart-checkout-14)] [[cart-checkout-15](cart-checkout.md#cart-checkout-15)]、交运状态 [[orders-fulfillment-9](orders-fulfillment.md#orders-fulfillment-9)]、售后决定 [[after-sales-6](after-sales.md#after-sales-6)]、退款执行 [[after-sales-9](after-sales.md#after-sales-9)] 或客服回复产生需要通知的事件，通知系统应向已配置的顾客渠道发送对应状态与下一步。

### customer-support-11

当游客订单发生通知事件，通知系统应使用下单时可用的联系渠道 [[cart-checkout-5](cart-checkout.md#cart-checkout-5)]，而非依赖账户站内消息。

### customer-support-12

当通知发送失败，通知系统应保存失败原因和可重试状态，且重试不重复触发原业务动作。

### customer-support-13

当通知渠道未配置或不可用，通知系统应向有权员工显示待处理异常，且不声称顾客已收到消息。

### customer-support-17

当客服打开尚未选择会话的工作区，客服系统应显示选择会话或等待分配的明确提示。

### customer-support-18

当客服会话工作区加载失败，客服系统应显示故障状态和可执行的重试路径。

### customer-support-19

当员工打开无权访问的会话，客服系统应拒绝读取内容并显示返回其授权队列的路径。

## 验证

### customer-support-14

当在系统或集成环境执行会话情形矩阵，验证者应逐项断言消息与责任归属：

| 情形 | 断言 |
| --- | --- |
| 在线与离线进入 | 状态及联系途径真实可见 [[customer-support-1](#customer-support-1)] |
| 在线发消息 | 双方状态和持久消息一致 [[customer-support-2](#customer-support-2)] |
| 离线留言 | 待跟进记录及回复方式可见 [[customer-support-3](#customer-support-3)] |
| 断线后回访 | 核验后恢复本人历史 [[customer-support-4](#customer-support-4)] |
| 游客与会员关联订单 | 仅核验归属后可见必要摘要 [[customer-support-5](#customer-support-5)] |
| 新会话 | 待分配队列可见 [[customer-support-6](#customer-support-6)] |
| 分配会话 | 同时只有一位负责人 [[customer-support-7](#customer-support-7)] |
| 转派会话 | 历史留存，新负责人收到待办 [[customer-support-8](#customer-support-8)] |
| 结束后追加消息 | 会话重新待跟进且历史保留 [[customer-support-9](#customer-support-9)] |
| 无选中会话 | 工作区有可理解的选择或等待提示 [[customer-support-17](#customer-support-17)] |
| 会话加载失败 | 故障与重试路径可见 [[customer-support-18](#customer-support-18)] |
| 员工越权打开会话 | 内容不泄露且可返回授权队列 [[customer-support-19](#customer-support-19)] |

### customer-support-15

当在集成环境执行通知情形矩阵，验证者应逐项断言送达和异常记录：

| 情形 | 断言 |
| --- | --- |
| 各关键业务事件 | 内容含正确状态与下一步 [[customer-support-10](#customer-support-10)] |
| 游客订单事件 | 发向下单联系渠道 [[customer-support-11](#customer-support-11)] |
| 发送失败后重试 | 留原因，业务动作不重复 [[customer-support-12](#customer-support-12)] |
| 渠道缺失或失效 | 员工见异常且无虚假送达状态 [[customer-support-13](#customer-support-13)] |

### customer-support-16

当在系统环境执行从顾客留言到客服接续的组合路径，验证者应断言离线消息持久保存 [[customer-support-3](#customer-support-3)]、会话进入待分配队列 [[customer-support-6](#customer-support-6)]、分配或转派只保留一位负责人 [[customer-support-7](#customer-support-7)] [[customer-support-8](#customer-support-8)]，且回复通知可追踪 [[customer-support-10](#customer-support-10)] [[customer-support-12](#customer-support-12)]。
