<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# merchant-operations: 商家运营与权限

## 意图

本候选包使商家以可追责的个人账号维护商品、订单、规则和服务，并及时发现待办与异常。
具体岗位分工和审批级别仍待商家确认。

## 外部行为

### merchant-operations-1

当商家受控初始化首位管理员，运营系统应建立可识别的个人账号，并阻止未经授权的重复初始化。

### merchant-operations-2

当有权管理员创建员工，运营系统应建立其个人账号并记录身份、创建者与时间。

### merchant-operations-3

当管理员授予或撤销角色，运营系统应使员工后续操作立即遵守新权限，并记录权限变化。

### merchant-operations-4

当员工请求超出其角色的商品、订单、退款、内容或客户资料操作，运营系统应拒绝该操作且不改变业务记录。

### merchant-operations-5

当商品运营人员维护商品、变体、市场价格或发布状态，运营系统应仅允许其通过商品管理行为 [[market-catalog-8](market-catalog.md#market-catalog-8)] 修改获授权字段。

### merchant-operations-6

当库存人员盘点或调整库存，运营系统应要求原因并保留库存调整记录 [[market-catalog-10](market-catalog.md#market-catalog-10)]。

### merchant-operations-7

当订单或履约员工处理待办，运营系统应显示其有权访问的订单、包裹和异常队列，并仅允许合法状态推进 [[orders-fulfillment-4](orders-fulfillment.md#orders-fulfillment-4)]。

### merchant-operations-8

当售后员工处理取消、退换或退款，运营系统应按其权限开放对应案件动作 [[after-sales-6](after-sales.md#after-sales-6)]，并记录决定依据。

### merchant-operations-9

当客服主管查看会话队列，运营系统应显示其可分配与转派的待办 [[customer-support-6](customer-support.md#customer-support-6)]，并隐藏无权访问的客户资料。

### merchant-operations-10

当有权员工维护税、配送、保修、退换、优惠或通知规则，运营系统应保存适用范围、生效时间、版本及操作者，并阻止缺少必需值的规则生效。

### merchant-operations-11

当价格、库存、订单、退款、积分、权限、内容发布或客服转派发生敏感变更，运营系统应写入不可由普通员工删改的审计事件。

### merchant-operations-12

当有权人员按市场和时间查看经营汇总，运营系统应展示订单、销量、待发、退货及客服积压，并区分测试交易与真实交易。

### merchant-operations-13

当有权人员从经营汇总打开异常指标，运营系统应提供可核对的相应工作队列入口。

### merchant-operations-16

当有权管理员停用员工，运营系统应记录操作者与时间并阻断该员工后续访问。

### merchant-operations-17

当有权管理员发起员工凭据重置，运营系统应记录发起者与时间并要求员工在受控渠道验证身份后完成重置。

## 验证

### merchant-operations-14

当在系统或集成环境执行身份与权限情形矩阵，验证者应逐项断言授权结果：

| 情形 | 断言 |
| --- | --- |
| 初始化及重复初始化 | 仅一次受控管理员建立 [[merchant-operations-1](#merchant-operations-1)] |
| 创建员工 | 个人账号、创建者和时间可查 [[merchant-operations-2](#merchant-operations-2)] |
| 停用员工 | 动作留痕且后续访问受阻 [[merchant-operations-16](#merchant-operations-16)] |
| 重置员工凭据 | 发起者留痕且员工需验证身份 [[merchant-operations-17](#merchant-operations-17)] |
| 授予与撤销角色 | 后续权限即时变化 [[merchant-operations-3](#merchant-operations-3)] |
| 越权操作 | 业务数据不变 [[merchant-operations-4](#merchant-operations-4)] |
| 维护商品及价格 | 仅授权字段按商品流程更新 [[merchant-operations-5](#merchant-operations-5)] |
| 盘点库存 | 原因和调整记录可查 [[merchant-operations-6](#merchant-operations-6)] |
| 订单履约队列 | 仅授权待办和合法推进可用 [[merchant-operations-7](#merchant-operations-7)] |
| 售后案件 | 权限及决定依据正确 [[merchant-operations-8](#merchant-operations-8)] |
| 客服队列 | 可分配待办可见，私有资料受限 [[merchant-operations-9](#merchant-operations-9)] |

### merchant-operations-15

当在集成环境执行运营规则与审计情形矩阵，验证者应逐项断言记录：

| 情形 | 断言 |
| --- | --- |
| 发布完整及不完整规则 | 完整规则有版本，不完整规则不生效 [[merchant-operations-10](#merchant-operations-10)] |
| 敏感业务变更 | 审计事件不可由普通员工删改 [[merchant-operations-11](#merchant-operations-11)] |
| 查看市场经营汇总 | 业务数量正确且测试与真实分离 [[merchant-operations-12](#merchant-operations-12)] |
| 打开异常指标 | 定位相应工作队列 [[merchant-operations-13](#merchant-operations-13)] |
