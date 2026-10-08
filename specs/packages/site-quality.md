<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# site-quality: 站点体验与可信运行

## 意图

本候选包使顾客与员工在不同设备和异常条件下仍能理解、访问和安全使用独立站。
具体品牌视觉、法域义务及资料保留规则仍待确认。

## 外部行为

### site-quality-1

当顾客或员工在桌面或窄屏设备执行主要任务，站点应保持任务所需内容与操作可见、可完成且不发生横向遮挡：

| 用户任务 | 覆盖行为 |
| --- | --- |
| 顾客选品与购物车 | 商品发现 [[product-selection-1](product-selection.md#product-selection-1)]、购物车变更 [[cart-checkout-2](cart-checkout.md#cart-checkout-2)] |
| 顾客结账与查单 | 最终报价 [[cart-checkout-10](cart-checkout.md#cart-checkout-10)]、订单查询 [[orders-fulfillment-3](orders-fulfillment.md#orders-fulfillment-3)] |
| 顾客售后与客服 | 售后申请 [[after-sales-3](after-sales.md#after-sales-3)]、实时消息 [[customer-support-2](customer-support.md#customer-support-2)] 与客服回复 [[customer-support-20](customer-support.md#customer-support-20)] |
| 员工工作区 | 订单待办 [[merchant-operations-7](merchant-operations.md#merchant-operations-7)]、客服队列 [[merchant-operations-9](merchant-operations.md#merchant-operations-9)] |

### site-quality-2

当顾客浏览主要页面，站点应以一致的字体、色彩、图像比例、留白和信息层级清楚呈现自行车商品及主要操作。

### site-quality-3

当用户仅用键盘操作主要流程，站点应提供可见焦点、合理顺序和可操作的控件。

### site-quality-4

当用户使用辅助技术阅读表单、图片、状态或费用变化，站点应提供语义标签、适当替代文本及可感知反馈。

### site-quality-5

当用户提交无效输入或操作失败，站点应指出具体问题并提供可继续的修正或重试路径。

### site-quality-6

当公开商品与分类 [[market-catalog-4](market-catalog.md#market-catalog-4)] 或文章 [[content-marketing-11](content-marketing.md#content-marketing-11)] 已发布，站点应提供可读地址、独立标题与描述、可索引正文及规范地址。

### site-quality-7

当页面不属于可索引的公开内容，站点应避免将其加入公开站点地图或向搜索引擎声明可索引：

| 页面类型 | 排除依据 |
| --- | --- |
| 未发布内容 | 尚未面向公众 [[content-marketing-3](content-marketing.md#content-marketing-3)] |
| 账户资料与结账 | 包含私有资料或交易状态 [[customer-account-4](customer-account.md#customer-account-4)] [[cart-checkout-5](cart-checkout.md#cart-checkout-5)] |
| 内部搜索与员工页面 | 不属于稳定公开内容或需要授权 [[merchant-operations-4](merchant-operations.md#merchant-operations-4)] |

### site-quality-8

当用户请求其他人的账户、订单、客服或员工资料，站点应拒绝访问且不泄露该资料是否存在的敏感细节。

### site-quality-9

当用户登录或执行敏感操作，站点应限制滥用尝试并保护凭据、会话和传输中的敏感资料。

### site-quality-10

当商店收集顾客资料，站点应说明已批准的用途与适用政策，并提供查询、更正及删除或保留请求入口。

### site-quality-11

当业务事件被记录或错误被报告，站点应避免在公开响应与普通日志中暴露密码、完整支付凭据或不必要的个人资料。

### site-quality-12

当业务写入中断或外部服务超时，站点应显示可理解状态并保留可核对的交易记录，使重试不重复产生业务效果。

### site-quality-13

当关键业务错误持续未解决，站点应使有权员工查看错误、影响范围和处理状态。

### site-quality-14

当按已批准的备份计划执行备份，站点应保存备份结果、覆盖的数据范围及声明的恢复点。

### site-quality-17

当按已批准的计划执行恢复演练，站点应验证订单、库存、账户及审计数据可恢复到声明的恢复点并保存演练结果。

### site-quality-18

给定正式品牌视觉规范已确认，当顾客浏览主要页面，站点应使已发布页面的字体、色彩与图像处理符合该规范。

## 验证

### site-quality-15

当在系统环境执行体验与可发现性情形矩阵，验证者应逐项断言页面结果：

| 情形 | 断言 |
| --- | --- |
| 桌面及窄屏完成选品、购物车、结账、查单、售后、聊天及员工待办 | 每项任务可完成且关键内容无横向遮挡 [[site-quality-1](#site-quality-1)] |
| 浏览主要页面 | 字体、色彩、图像、留白和层级一致 [[site-quality-2](#site-quality-2)] |
| 应用已批准视觉规范 | 已发布页面符合规范 [[site-quality-18](#site-quality-18)] |
| 仅键盘操作 | 焦点可见且控件可完成任务 [[site-quality-3](#site-quality-3)] |
| 辅助技术阅读 | 表单、图像、状态和费用可感知 [[site-quality-4](#site-quality-4)] |
| 输入错误及操作失败 | 问题与恢复路径明确 [[site-quality-5](#site-quality-5)] |
| 发布公开内容 | 标题、描述、正文及规范地址可索引 [[site-quality-6](#site-quality-6)] |
| 草稿与私有页面 | 不进入公开地图或可索引声明 [[site-quality-7](#site-quality-7)] |

### site-quality-16

当在系统或集成环境执行安全与恢复情形矩阵，验证者应逐项断言保护及可恢复结果：

| 情形 | 断言 |
| --- | --- |
| 越权读取私有资料 | 请求被拒且无敏感存在性信息 [[site-quality-8](#site-quality-8)] |
| 登录滥用与敏感操作 | 尝试受限且凭据、会话、传输受保护 [[site-quality-9](#site-quality-9)] |
| 资料收集和资料请求 | 用途可见且入口可用 [[site-quality-10](#site-quality-10)] |
| 错误响应和日志 | 无密码、完整支付凭据或多余个人资料 [[site-quality-11](#site-quality-11)] |
| 写入中断与超时重试 | 状态清楚且业务效果不重复 [[site-quality-12](#site-quality-12)] |
| 持续业务错误 | 授权员工可见影响与处理状态 [[site-quality-13](#site-quality-13)] |
| 执行备份 | 结果、数据范围与恢复点可核验 [[site-quality-14](#site-quality-14)] |
| 执行恢复演练 | 关键数据恢复到声明点并留结果 [[site-quality-17](#site-quality-17)] |
