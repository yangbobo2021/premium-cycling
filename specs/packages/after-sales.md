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

给定订单付款结果已核清，当有权员工批准未交运商品取消，售后流程应按付款状态记录取消原因、变更对应订单行状态 [[orders-fulfillment-4](orders-fulfillment.md#orders-fulfillment-4)] 并释放已取消商品的库存占用 [[market-catalog-12](market-catalog.md#market-catalog-12)]：

| 付款状态 | 取消后的资金结果 |
| --- | --- |
| 待付款且无在途付款 | 关闭原待付款订单并释放全部行占用；仍需购买的商品须重新报价并建立新订单 [[cart-checkout-22](cart-checkout.md#cart-checkout-22)] |
| 已付款 [[cart-checkout-14](cart-checkout.md#cart-checkout-14)] | 仅取消符合条件的未交运行并建立按原支付模式处理的退款待办，不将待办冒充已退款 |

### after-sales-3

当已核验订单归属的顾客 [[orders-fulfillment-3](orders-fulfillment.md#orders-fulfillment-3)] 对订单行 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 提交售后申请，售后流程应按申请类型收集资料并生成可查询的案件：

| 申请类型 | 必需资料 |
| --- | --- |
| 退货 | 商品、数量、原因和必要证据 |
| 换货 | 原商品、数量、目标商品或规格、原因和必要证据 |
| 运输损坏 [[orders-fulfillment-12](orders-fulfillment.md#orders-fulfillment-12)] | 所涉商品、包裹、损坏说明和证据 |

### after-sales-4

当申请数量超过已购未处理数量，售后流程应拒绝超量申请并指出可申请数量。

### after-sales-5

当退换申请不符合已公布的期限或条件，售后流程应显示适用的订单政策快照 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 与拒绝原因。

### after-sales-6

当有权员工审核退换案件，售后流程应记录接受或拒绝决定、理由、处理人和时间，并向顾客显示下一步。

### after-sales-7

当退回商品被实际接收并检查，售后流程应记录所涉序列号或订单行、状态、检查证据及可退款或换货的结论。

### after-sales-8

当订单行退款被核准，售后流程应将退款同时限制在该行原成交金额及税费／配送分摊 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 加该案件已确认补款 [[after-sales-28](#after-sales-28)]、扣除该行及案件既有退款后的剩余已付金额，以及整单和关联补款的剩余实收金额之内，并保存计算依据、币种、支付模式与核准者。

### after-sales-9

当授权人员执行退款，售后流程应仅通过原订单支付模式快照 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 允许的资金路径发起一次退款，并保存外部或测试模式的退款引用。

### after-sales-10

当退款结果未明，售后流程应将案件标为待核对，保留原退款引用，并在核清前阻止再次执行同笔退款。

### after-sales-11

当整车完成交付且商家取得可核实的序列号，售后流程应将序列号关联到确切订单行并限制重复关联。

### after-sales-12

当顾客提交保修申请，售后流程应依据已公布的保修政策 [[content-marketing-9](content-marketing.md#content-marketing-9)] 与原订单快照 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 判断资格，或说明资料不足并请求补充。

### after-sales-13

当保修或维修案件推进，售后流程应记录诊断、处理责任、修理或更换结果、费用依据及交还状态。

### after-sales-14

当已批准售后案件改变库存占用 [[market-catalog-12](market-catalog.md#market-catalog-12)]、优惠权益 [[content-marketing-7](content-marketing.md#content-marketing-7)] 或积分账本 [[customer-account-13](customer-account.md#customer-account-13)]，售后流程应保存各调整的来源案件、避免重复调整同一权益，并保持原订单快照不变 [[orders-fulfillment-2](orders-fulfillment.md#orders-fulfillment-2)]。

### after-sales-18

当售后案件发生有效业务动作，售后流程应按申请类型与下表推进案件状态，记录动作来源和时间，并拒绝跳过必要审核或检查的转换：

| 案件类型 | 允许的状态路径 |
| --- | --- |
| 取消 | 待审核 → 已拒绝／待付款核对／待退款／已完成；待付款核对 → 待审核；待退款 → 已完成（退款成功后） |
| 退货 | 待审核 → 已拒绝／待退回；待退回 → 待检查；待检查 → 已拒绝／待退款；待退款 → 已完成（退款成功后） |
| 换货 | 待审核 → 已拒绝／待退回；待退回 → 待检查；待检查 → 已拒绝／待补差价／待换货履约；待补差价 → 待换货履约；待换货履约 → 已终止（交运前）／已完成（替代包裹送达后） [[after-sales-27](#after-sales-27)] |
| 运输损坏或保修 | 待审核 → 已拒绝／待补资料／待诊断；待补资料 → 待审核；待诊断 → 已拒绝／待处理；待处理 → 已完成（结果履行后） |
| 退款 | 待核准 → 已拒绝／待执行；待执行 → 结果待核对／已失败／已完成；结果待核对 → 已失败／已完成；已失败 → 待执行（重新核准后） |

### after-sales-19

当退款被确认为失败，售后流程应保留失败原因和可重试的原案件，不增加已退金额或完成状态。

### after-sales-20

当同一退款执行或结果重复到达，售后流程应仅记一次已退金额、库存或积分调整，并保留重复事件的核对记录。

### after-sales-21

当退货或换货申请获批准，售后流程应向顾客显示按原订单政策 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 确定的退回地点、包装与整车拆装要求、费用承担及截止时间；尚未确定的条件应阻止生成寄回指引。

### after-sales-22

当换货目标商品与已检查的退回商品存在价差，售后流程应按原订单可退金额及目标商品当前报价 [[market-catalog-6](market-catalog.md#market-catalog-6)] 展示差额，并在顾客确认补款或退款安排前阻止替代商品交运。

### after-sales-23

当换货案件准备替代商品履约，售后流程应按目标变体可售量 [[market-catalog-13](market-catalog.md#market-catalog-13)]、库存占用 [[market-catalog-11](market-catalog.md#market-catalog-11)] 及价差处理结果 [[after-sales-28](#after-sales-28)] 决定是否请求创建可追踪的替代包裹 [[orders-fulfillment-19](orders-fulfillment.md#orders-fulfillment-19)]：

| 履约条件 | 结果 |
| --- | --- |
| 已检查退回商品、目标变体占库有效、价差已结清且获履约授权 | 请求替代包裹 |
| 目标变体无库存 | 不占库，向顾客提供改选目标或改走退款的路径 |
| 未检查实物、价差未结清或缺少履约授权 | 保留案件待办，不创建包裹 |

### after-sales-24

当员工将售后案件标为已完成，售后流程应按处理结论核对实际结果，并阻止将未履行的决定标为已完成：

| 处理结论 | 完成依据 |
| --- | --- |
| 未付款订单取消 | 原订单全部行已关闭且库存已释放 [[after-sales-2](#after-sales-2)] |
| 已付款取消或退货退款 | 原支付模式退款成功结果已确认 [[after-sales-25](#after-sales-25)] |
| 换货 | 替代包裹已送达 [[orders-fulfillment-11](orders-fulfillment.md#orders-fulfillment-11)] |
| 保修或维修 | 维修或更换结果和交还状态已记录 [[after-sales-13](#after-sales-13)] |

### after-sales-25

当原支付模式的退款结果被核实为成功，售后流程应按获核准的订单行金额 [[after-sales-8](#after-sales-8)] 更新已退余额和退款状态，并保存资金或测试结果证据。

### after-sales-26

当顾客对付款结果待核对的订单 [[cart-checkout-23](cart-checkout.md#cart-checkout-23)] 申请取消，售后流程应将案件标为待付款核对，并在核清前保留库存占用且不声称订单已取消或已退款。

### after-sales-27

当已占用库存的换货案件在替代商品交运前终止，售后流程应释放目标变体库存 [[market-catalog-12](market-catalog.md#market-catalog-12)]、记录原因，并为已确认补款 [[after-sales-28](#after-sales-28)] 建立退款待办及向顾客说明后续退货或退款路径：

| 终止原因 | 记录 |
| --- | --- |
| 顾客撤回换货 | 顾客请求与时间 |
| 目标商品无法继续履约 | 失败原因与责任人 |

### after-sales-28

当顾客确认换货价差安排，售后流程应按原订单支付模式 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] 将差额处理记录为独立于原订单快照的案件资金记录，并在结果未核实成功时保持换货待办：

| 差额 | 处理结果 |
| --- | --- |
| 顾客需补款 | 每次已确认安排只发起一次关联案件的补款；成功后结清，失败后可重新确认，结果未明须核对原尝试且不得再次扣款或交运 |
| 商家需退差额 | 核准未超出该行可退金额 [[after-sales-8](#after-sales-8)] 后通过原支付模式退款 [[after-sales-9](#after-sales-9)]，核实成功 [[after-sales-25](#after-sales-25)] 后标记差额已结清 |
| 无差额 | 记录零差额及顾客确认，不产生资金动作 |

### after-sales-29

当有权人员核对结果未明的售后资金动作，售后流程应依据原退款 [[after-sales-10](#after-sales-10)] 或换货补款 [[after-sales-28](#after-sales-28)] 引用查询受理方结果，并按核实结果推进案件：

| 核实结果 | 处理 |
| --- | --- |
| 退款成功或失败 | 分别按成功 [[after-sales-25](#after-sales-25)] 或失败 [[after-sales-19](#after-sales-19)] 处理 |
| 换货补款成功或失败 | 按原差额安排 [[after-sales-28](#after-sales-28)] 标记结清或保留待办 |
| 仍无法确认 | 保持待核对，不重复退款或扣款 |

## 验证

### after-sales-15

当在系统或集成环境执行取消与退换情形矩阵，验证者应逐项断言案件结果：

| 情形 | 断言 |
| --- | --- |
| 可取消与不可取消状态 | 资格、状态与拒绝原因正确 [[after-sales-1](#after-sales-1)] |
| 批准未付款整单或已付款未交运行取消 | 原报价不被改写，库存和已付款退款待办正确 [[after-sales-2](#after-sales-2)] |
| 付款待核对时申请取消 | 案件等待核对且库存与资金状态不提前变更 [[after-sales-26](#after-sales-26)] |
| 退货、换货与运输损坏申请 | 各类型必需资料和案件可查 [[after-sales-3](#after-sales-3)] |
| 超过未处理数量 | 超量拒绝并显示可申请数量 [[after-sales-4](#after-sales-4)] |
| 超期限或条件不符 | 显示订单政策与拒绝原因 [[after-sales-5](#after-sales-5)] |
| 员工接受或拒绝 | 理由、人员、时间和下一步可见 [[after-sales-6](#after-sales-6)] |
| 实物接收检查 | 序列号或订单行、证据及结论可查 [[after-sales-7](#after-sales-7)] |
| 取消、退货、换货、损坏和保修推进 | 只允许表内状态转换并留来源与时间 [[after-sales-18](#after-sales-18)] |
| 接受退货及缺少退回政策 | 指引完整或阻止生成寄回指引 [[after-sales-21](#after-sales-21)] |
| 换货有价差及顾客未确认 | 差额可见且不交运 [[after-sales-22](#after-sales-22)] |
| 目标缺货、未检查及已具备换货条件 | 仅最后一种可请求替代包裹 [[after-sales-23](#after-sales-23)] |
| 补款成功、失败、未明及退差额 | 仅确认已结清后可履约且重复确认不重复收款 [[after-sales-28](#after-sales-28)] |
| 原退款或补款结果仍未知 | 按原引用核对且不重复资金动作 [[after-sales-29](#after-sales-29)] |
| 已占库换货撤回或无法履行 | 占用释放、原因留存且顾客可选择后续路径 [[after-sales-27](#after-sales-27)] |
| 未履行和已履行售后决定 | 仅已履行的案件可完成 [[after-sales-24](#after-sales-24)] |

### after-sales-16

当在集成环境执行退款与车辆服务情形矩阵，验证者应逐项断言状态及资金边界：

| 情形 | 断言 |
| --- | --- |
| 同一订单含高价与低价行及换货补款 | 每行和案件已付金额上限、模式与核准依据正确 [[after-sales-8](#after-sales-8)] |
| 真实与测试退款配置 | 仅使用原订单允许路径并留结果 [[after-sales-9](#after-sales-9)] |
| 原支付模式确认退款成功 | 按核准订单行金额更新已退余额和状态 [[after-sales-25](#after-sales-25)] |
| 退款结果未明 | 案件待核对且不重复执行 [[after-sales-10](#after-sales-10)] |
| 退款失败 | 保留原因、原案件与可重试状态 [[after-sales-19](#after-sales-19)] |
| 重复退款执行和回报 | 金额及权益只计算一次 [[after-sales-20](#after-sales-20)] |
| 录入及重复录入序列号 | 仅正确订单行关联一次 [[after-sales-11](#after-sales-11)] |
| 有凭据与缺凭据保修 | 资格正确或明确请求补充 [[after-sales-12](#after-sales-12)] |
| 维修处理 | 诊断、费用、结果及交还状态可查 [[after-sales-13](#after-sales-13)] |
| 售后调整权益 | 调整可追溯且原订单快照不变 [[after-sales-14](#after-sales-14)] |

### after-sales-17

当在系统环境执行从订单商品到售后结案的组合路径，验证者应断言申请形成可查询案件 [[after-sales-3](#after-sales-3)]、审核决定与实物检查可追溯 [[after-sales-6](#after-sales-6)] [[after-sales-7](#after-sales-7)]、退款不超额且按原支付模式处理并核实结果 [[after-sales-8](#after-sales-8)] [[after-sales-9](#after-sales-9)] [[after-sales-25](#after-sales-25)]、库存与权益调整能追溯来源 [[after-sales-14](#after-sales-14)]，且案件仅在结果履行后完成 [[after-sales-24](#after-sales-24)]。
