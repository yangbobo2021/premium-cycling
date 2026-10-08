<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# after-sales: 售后与车辆服务

## 意图

本候选包使顾客和员工根据原订单处理取消、退换、退款、保修和维修，并追踪整车身份。
期限、费用承担、保修覆盖和维修网络仍待业务确认。

## 外部行为

### after-sales-1

当有权顾客申请取消订单，售后流程应根据订单当前状态 [[orders-fulfillment-3](orders-fulfillment.md#orders-fulfillment-3)] 显示申请资格、处理状态及不符合条件的原因。

### after-sales-2

当有权员工批准未交运商品的取消，售后流程应记录原因并释放对应库存占用 [[market-catalog-12](market-catalog.md#market-catalog-12)]。

### after-sales-3

当顾客对订单商品申请退货、换货或报告运输损坏，售后流程应收集原因、数量、相关包裹及必要证据，生成可查询的案件。

### after-sales-4

当申请数量超过已购未处理数量，售后流程应拒绝超量申请并指出可申请数量。

### after-sales-5

当退换申请不符合已公布的期限或条件，售后流程应显示适用的订单政策快照 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 与拒绝原因。

### after-sales-6

当有权员工审核退换案件，售后流程应记录接受或拒绝决定、理由、处理人和时间，并向顾客显示下一步。

### after-sales-7

当退回商品被实际接收并检查，售后流程应记录所涉序列号或订单行、状态、检查证据及可退款或换货的结论。

### after-sales-8

当退款被核准，售后流程应限制金额不超过原订单尚可退金额，并保存计算依据、支付模式和核准者。

### after-sales-9

当授权人员执行退款，售后流程应仅通过原订单支付模式快照 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 允许的资金路径处理，并保存外部结果或测试结果。

### after-sales-10

当退款结果未知、失败或重复回报，售后流程应保留可重试的案件状态，且不重复计算已退金额、库存或积分影响。

### after-sales-11

当整车完成交付且商家取得可核实的序列号，售后流程应将序列号关联到确切订单行并限制重复关联。

### after-sales-12

当顾客提交保修申请，售后流程应依据已公布的保修范围与原订单快照判断资格，或说明资料不足并请求补充。

### after-sales-13

当保修或维修案件推进，售后流程应记录诊断、处理责任、修理或更换结果、费用依据及交还状态。

### after-sales-14

当取消、退换或退款改变库存、优惠或积分权益，售后流程应保存各调整的来源案件并保持原订单快照不变。

## 验证

### after-sales-15

当在系统或集成环境执行取消与退换情形矩阵，验证者应逐项断言案件结果：

| 情形 | 断言 |
| --- | --- |
| 可取消与不可取消状态 | 资格、状态与拒绝原因正确 [[after-sales-1](#after-sales-1)] |
| 批准未交运取消 | 原因记录且对应库存释放 [[after-sales-2](#after-sales-2)] |
| 退货、换货与运输损坏 | 数量、包裹、证据及案件可查 [[after-sales-3](#after-sales-3)] |
| 超过未处理数量 | 超量拒绝并显示可申请数量 [[after-sales-4](#after-sales-4)] |
| 超期限或条件不符 | 显示订单政策与拒绝原因 [[after-sales-5](#after-sales-5)] |
| 员工接受或拒绝 | 理由、人员、时间和下一步可见 [[after-sales-6](#after-sales-6)] |
| 实物接收检查 | 序列号或订单行、证据及结论可查 [[after-sales-7](#after-sales-7)] |

### after-sales-16

当在集成环境执行退款与车辆服务情形矩阵，验证者应逐项断言状态及资金边界：

| 情形 | 断言 |
| --- | --- |
| 核准退款及超额请求 | 金额上限、模式与核准依据正确 [[after-sales-8](#after-sales-8)] |
| 真实与测试退款配置 | 仅使用原订单允许路径并留结果 [[after-sales-9](#after-sales-9)] |
| 退款失败及重复回报 | 案件可重试且权益仅调整一次 [[after-sales-10](#after-sales-10)] |
| 录入及重复录入序列号 | 仅正确订单行关联一次 [[after-sales-11](#after-sales-11)] |
| 有凭据与缺凭据保修 | 资格正确或明确请求补充 [[after-sales-12](#after-sales-12)] |
| 维修处理 | 诊断、费用、结果及交还状态可查 [[after-sales-13](#after-sales-13)] |
| 售后调整权益 | 调整可追溯且原订单快照不变 [[after-sales-14](#after-sales-14)] |

### after-sales-17

当在系统环境执行从订单商品到售后结案的组合路径，验证者应断言申请形成可查询案件 [[after-sales-3](#after-sales-3)]、审核决定与实物检查可追溯 [[after-sales-6](#after-sales-6)] [[after-sales-7](#after-sales-7)]、退款不超额且按原支付模式处理 [[after-sales-8](#after-sales-8)] [[after-sales-9](#after-sales-9)]，并使库存与权益调整能追溯来源 [[after-sales-14](#after-sales-14)]。
