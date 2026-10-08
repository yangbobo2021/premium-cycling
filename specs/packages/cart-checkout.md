<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# cart-checkout: 购物车与结账

## 意图

本候选包使游客和会员以已确认的价格、优惠和费用提交购买，并使支付失败及重试不会造成重复交易。
市场、税费、配送、优惠及真实或测试支付模式均以商家后续确认的配置为准。

## 外部行为

### cart-checkout-1

当顾客将可售变体 [[market-catalog-6](market-catalog.md#market-catalog-6)] 加入购物车，购物车应保存确切变体、数量、当前市场币种和展示价格。

### cart-checkout-2

当顾客修改购物车数量或移除行，购物车应更新行小计和总额，并阻止超出可售量 [[market-catalog-13](market-catalog.md#market-catalog-13)] 的数量。

### cart-checkout-3

当顾客离开并返回购物流程，购物车应恢复尚有效的行并标示失效或变化的商品。

### cart-checkout-4

当顾客切换市场，购物车应按新市场报价 [[market-catalog-2](market-catalog.md#market-catalog-2)] 重新核对各行并阻止沿用旧报价提交。

### cart-checkout-5

当游客进入结账，结账流程应允许其在不注册的情况下提供联系信息和收货地址。

### cart-checkout-6

当已登录顾客进入结账，结账流程应允许其使用已保存地址 [[customer-account-5](customer-account.md#customer-account-5)] 或输入新地址。

### cart-checkout-7

当顾客提交收货地址，结账流程应校验必填信息和当前市场可配送范围，并指出不可配送或缺失项。

### cart-checkout-8

当地址通过校验，结账流程应显示按已生效配送规则 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)] 得出的可用选项、费用及有依据的预计时效，供顾客明确选择。

### cart-checkout-9

当顾客输入优惠码或选择活动，结账流程应依据已发布优惠规则 [[content-marketing-7](content-marketing.md#content-marketing-7)] 计算折扣，或说明无效、过期及不适用原因。

### cart-checkout-10

当结账资料齐备，结账流程应展示商品、折扣、适用积分抵扣 [[customer-account-12](customer-account.md#customer-account-12)]、配送、税费、合计和币种的逐项报价。

### cart-checkout-11

当提交前商品价格、库存、优惠、税费或配送费用变化，结账流程应展示新旧差异并要求顾客重新确认报价。

### cart-checkout-12

当商家所需的市场、税、配送 [[launch-readiness-4](launch-readiness.md#launch-readiness-4)] 或支付配置 [[launch-readiness-5](launch-readiness.md#launch-readiness-5)] 缺失，结账流程应阻止提交并说明缺失的业务条件。

### cart-checkout-13

当顾客确认报价并提交付款，结账流程应只调用经就绪检查的支付方式 [[launch-readiness-5](launch-readiness.md#launch-readiness-5)]，并明确标示真实或测试模式。

### cart-checkout-14

当支付成功结果被确认，结账流程应形成一笔可查询的订单 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)]，并保存支付模式、结果与引用编号。

### cart-checkout-15

当支付失败或结果未明，结账流程应保留可核对的结账上下文，并避免将订单标为已付款。

### cart-checkout-16

当同一提交被重复发送或支付结果重复回报，结账流程应只产生一次有效订单、一次库存占用 [[market-catalog-11](market-catalog.md#market-catalog-11)] 和一次优惠或积分业务效果。

### cart-checkout-17

当顾客在失败后重试付款，结账流程应重新核对当前报价与可售性，并允许顾客确认后继续。

### cart-checkout-18

给定支付方式为测试模式，当顾客确认付款，结账流程应明确标示不会产生真实扣款，且测试结果不得表示真实收款授权。

## 验证

### cart-checkout-19

当在系统环境执行购物车与报价情形矩阵，验证者应逐项断言可见结果：

| 情形 | 断言 |
| --- | --- |
| 加入指定变体 | 行、数量、市场币种和价格正确 [[cart-checkout-1](#cart-checkout-1)] |
| 改数量及移除 | 小计更新且超量被阻止 [[cart-checkout-2](#cart-checkout-2)] |
| 离开再返回 | 有效行恢复，失效行有说明 [[cart-checkout-3](#cart-checkout-3)] |
| 切换市场 | 重新报价且旧报价不能提交 [[cart-checkout-4](#cart-checkout-4)] |
| 游客进入结账 | 无注册门槛且可填联系与地址 [[cart-checkout-5](#cart-checkout-5)] |
| 会员进入结账 | 可选保存或新地址 [[cart-checkout-6](#cart-checkout-6)] |
| 无效或不可配送地址 | 指出具体问题 [[cart-checkout-7](#cart-checkout-7)] |
| 有效地址 | 可选配送服务、费用和时效可见 [[cart-checkout-8](#cart-checkout-8)] |
| 有效和无效优惠 | 折扣正确或原因明确 [[cart-checkout-9](#cart-checkout-9)] |
| 完整结账资料 | 逐项费用、合计和币种一致 [[cart-checkout-10](#cart-checkout-10)] |
| 提交前改价或费用 | 显示差异并要求重新确认 [[cart-checkout-11](#cart-checkout-11)] |
| 缺少商家配置 | 拒绝提交且指出缺项 [[cart-checkout-12](#cart-checkout-12)] |

### cart-checkout-20

当在集成环境执行支付与重试情形矩阵，验证者应逐项断言持久结果：

| 情形 | 断言 |
| --- | --- |
| 已确认报价付款 | 仅使用配置的支付模式 [[cart-checkout-13](#cart-checkout-13)] |
| 支付成功 | 一笔可查询订单及模式、结果、引用编号 [[cart-checkout-14](#cart-checkout-14)] |
| 失败或结果未明 | 上下文保留且无已付款状态 [[cart-checkout-15](#cart-checkout-15)] |
| 双击与重复回报 | 订单、库存、优惠和积分效果均仅一次 [[cart-checkout-16](#cart-checkout-16)] |
| 失败后变价再重试 | 重新核价并再次确认 [[cart-checkout-17](#cart-checkout-17)] |
| 测试模式付款 | 无真实扣款声明或真实收款授权 [[cart-checkout-18](#cart-checkout-18)] |

### cart-checkout-21

当在系统环境执行从选品到下单的组合路径，验证者应断言指定变体进入购物车 [[cart-checkout-1](#cart-checkout-1)]、游客或会员可完成结账 [[cart-checkout-5](#cart-checkout-5)] [[cart-checkout-6](#cart-checkout-6)]、最终报价经确认 [[cart-checkout-10](#cart-checkout-10)] [[cart-checkout-11](#cart-checkout-11)]，且支付成功只形成一笔订单 [[cart-checkout-14](#cart-checkout-14)] [[cart-checkout-16](#cart-checkout-16)]。
