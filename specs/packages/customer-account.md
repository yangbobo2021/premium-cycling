<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# customer-account: 顾客身份与权益

## 意图

本候选包使顾客安全管理身份、地址、收藏和评价，并为可能启用的积分建立可核对的行为边界。
积分是否上线及数值规则仍待确认。

## 外部行为

### customer-account-1

当访客注册账户，账户系统应验证必要联系渠道并阻止重复或无效身份占用。

### customer-account-2

当顾客提交登录请求，账户系统应验证其凭据并仅向验证成功者建立可访问本人资料的会话。

### customer-account-3

当游客请求查看订单或发起订单相关操作，账户系统应要求其证明对下单联系渠道的控制权，不能仅凭订单编号或可猜测资料授权。

### customer-account-4

当顾客提交个人资料访问操作，账户系统应只允许其访问本人资料，并按操作保存结果：

| 操作 | 结果 |
| --- | --- |
| 查看 | 仅返回本人可访问的资料 |
| 修改 | 保存本人改动及可核实的修改记录 |

### customer-account-5

当已登录顾客提交地址列表变更，账户系统应仅在本人账户保存变更，并阻止未授权用户读取：

| 操作 | 结果 |
| --- | --- |
| 新增 | 加入本人地址列表 |
| 修改 | 仅更新所选本人地址 |
| 删除 | 从本人可选地址中移除所选地址 |

### customer-account-6

当已登录顾客提交收藏列表变更，账户系统应跨会话保存本人选择并标示仍保留变体的下架或缺货状态 [[market-catalog-7](market-catalog.md#market-catalog-7)]：

| 操作 | 结果 |
| --- | --- |
| 收藏变体 | 加入本人收藏列表 |
| 移除变体 | 从本人收藏列表删除所选项 |

### customer-account-7

当已登录顾客查看订单历史，账户系统应只展示其已归属订单的摘要及查询入口 [[orders-fulfillment-3](orders-fulfillment.md#orders-fulfillment-3)]。

### customer-account-8

当顾客对符合已公布资格的已购订单行 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 提交评价，账户系统应记录评分、文字、订单行和待审核状态，并阻止同一订单行产生重复有效评价。

### customer-account-9

当有权员工审核评价，账户系统应记录发布或驳回结果及理由，并使前台只显示已发布评价。

### customer-account-10

给定商家已启用积分计划，当合格订单达到所需状态 [[orders-fulfillment-4](orders-fulfillment.md#orders-fulfillment-4)] 并满足已公布的获得条件，账户系统应依据该订单币种及规则记录一笔可追溯积分取得事件。

### customer-account-11

给定商家已启用积分计划，当顾客查看积分，账户系统应展示余额、来源订单及取得、使用、冲回或过期记录，且余额不得为负。

### customer-account-12

给定商家已启用积分计划，当顾客在结账使用积分，账户系统应仅按已公布的币种与兑换规则提供可用抵扣，并记录对应订单。

### customer-account-13

给定商家已启用积分计划，当原订单的积分资格发生已核实的变化，账户系统应按原订单行、原账本和已公布规则计算尚需调整的差额，且不同事件不得重复冲回同一权益：

| 资格变化 | 账本结果 |
| --- | --- |
| 付款失败 [[cart-checkout-15](cart-checkout.md#cart-checkout-15)] | 释放尚未最终使用的抵扣，不取得购买积分 |
| 订单行取消 [[after-sales-2](after-sales.md#after-sales-2)] | 按该行及原记录冲回取得或使用的积分 |
| 退款成功 [[after-sales-25](after-sales.md#after-sales-25)] | 按实际退款范围与原记录调整积分 |
| 同一事件重复 | 不再增加或扣减余额 |

### customer-account-14

给定商家未启用积分计划，当顾客浏览或结账，账户系统应不展示可兑换积分或暗示可获得积分。

### customer-account-17

当已登录顾客退出，账户系统应撤销该会话对私有资料的后续访问。

### customer-account-18

当顾客请求重置凭据，账户系统应验证其对已登记渠道的控制权并使旧凭据或过期重置凭据失效。

## 验证

### customer-account-15

当在系统环境执行身份与关系情形矩阵，验证者应逐项断言权限及持久结果：

| 情形 | 断言 |
| --- | --- |
| 注册有效及重复身份 | 联系渠道验证且重复占用受阻 [[customer-account-1](#customer-account-1)] |
| 登录 | 验证成功者才建立本人会话 [[customer-account-2](#customer-account-2)] |
| 退出 | 会话后续访问受阻 [[customer-account-17](#customer-account-17)] |
| 重置凭据 | 需证明渠道控制权，旧凭据与过期凭据失效 [[customer-account-18](#customer-account-18)] |
| 游客查单或售后 | 需证明原联系渠道控制权 [[customer-account-3](#customer-account-3)] |
| 本人及他人改资料 | 仅本人成功且记录持久 [[customer-account-4](#customer-account-4)] |
| 增改删地址 | 仅本人列表按操作变化，他人不可读取 [[customer-account-5](#customer-account-5)] |
| 收藏、移除及保留缺货变体 | 列表跨会话正确且保留项标示不可售 [[customer-account-6](#customer-account-6)] |
| 查询本人及他人订单 | 仅本人订单可见 [[customer-account-7](#customer-account-7)] |
| 合格评价及重复提交 | 一条有效待审核评价 [[customer-account-8](#customer-account-8)] |
| 发布及驳回评价 | 理由留存，仅发布内容公开 [[customer-account-9](#customer-account-9)] |

### customer-account-16

当在集成环境执行积分启用与关闭情形矩阵，验证者应逐项断言账本结果：

| 情形 | 断言 |
| --- | --- |
| 合格订单取得积分 | 按币种和规则只记一笔来源事件 [[customer-account-10](#customer-account-10)] |
| 查询积分 | 余额与历史一致且不为负 [[customer-account-11](#customer-account-11)] |
| 结账抵扣 | 仅允许规则内币种和额度 [[customer-account-12](#customer-account-12)] |
| 失败、取消、退款及重复事件 | 各情形按原账本调整一次 [[customer-account-13](#customer-account-13)] |
| 未启用积分 | 前台与结账无积分承诺 [[customer-account-14](#customer-account-14)] |
