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

当顾客提交购物车行变更，购物车应按操作更新行与总额并阻止超出可售量 [[market-catalog-13](market-catalog.md#market-catalog-13)] 的数量：

| 操作 | 结果 |
| --- | --- |
| 增加或减少数量 | 保留该行并重新计算小计 |
| 删除行 | 移除该行及其小计 |

### cart-checkout-3

当顾客离开并返回购物流程，购物车应恢复尚有效的行并标示已下架或缺货变体 [[market-catalog-7](market-catalog.md#market-catalog-7)] 及当前市场变价 [[market-catalog-2](market-catalog.md#market-catalog-2)]。

### cart-checkout-4

当顾客切换市场，购物车应按新市场报价 [[market-catalog-2](market-catalog.md#market-catalog-2)] 重新核对各行并阻止沿用旧报价提交。

### cart-checkout-5

当游客进入结账，结账流程应允许其在不注册的情况下提供联系信息和收货地址。

### cart-checkout-6

当已登录顾客进入结账，结账流程应允许其使用已保存地址 [[customer-account-5](customer-account.md#customer-account-5)] 或输入新地址。

### cart-checkout-7

当顾客提交收货地址，结账流程应校验必填信息和已启用市场 [[market-catalog-1](market-catalog.md#market-catalog-1)] 的可配送规则 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)]，并指出不可配送或缺失项。

### cart-checkout-8

当地址通过校验，结账流程应显示按已生效配送规则 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)] 得出的可用选项、费用及有依据的预计时效，供顾客明确选择。

### cart-checkout-9

当顾客申请使用优惠，结账流程应依据已发布优惠规则 [[content-marketing-7](content-marketing.md#content-marketing-7)] 计算折扣，或说明优惠码与活动的无效、过期及不适用原因。

### cart-checkout-10

当结账资料齐备，结账流程应按收货地和已生效的计费规则 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)] 展示商品、已发布优惠 [[content-marketing-7](content-marketing.md#content-marketing-7)]、适用积分抵扣 [[customer-account-12](customer-account.md#customer-account-12)]、所选配送、税费、最终应付总额和币种的逐项报价：

| 计费情形 | 报价结果 |
| --- | --- |
| 适用税费规则 | 按收货地、商品类别及生效版本计算并显示税额 |
| 明确免税或零税 | 显示按适用规则得出的零税额及依据 |
| 无法确定适用规则 | 不形成可付款报价，指出缺失的税务依据 |

### cart-checkout-11

当提交前商品价格或库存 [[market-catalog-6](market-catalog.md#market-catalog-6)] [[market-catalog-13](market-catalog.md#market-catalog-13)]、优惠 [[content-marketing-7](content-marketing.md#content-marketing-7)]、税费或配送费用 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)] 变化，结账流程应展示新旧差异并要求顾客重新确认报价。

### cart-checkout-12

当结账准备校验发现必需业务输入缺失，结账流程应阻止付款提交并说明缺失的业务条件：

| 缺失输入 | 阻断依据 |
| --- | --- |
| 目标市场未启用 | 不提供该市场结账 [[market-catalog-3](market-catalog.md#market-catalog-3)] |
| 收货地无适用税／配送／售后规则 | 显示受影响目的地或商品 [[launch-readiness-4](launch-readiness.md#launch-readiness-4)] |
| 支付配置未就绪 | 显示支付模式缺项 [[launch-readiness-5](launch-readiness.md#launch-readiness-5)] |

### cart-checkout-13

给定待付款订单、库存及所需优惠和积分占用已持久确认 [[cart-checkout-22](#cart-checkout-22)]，当顾客提交付款，结账流程应按下表重新核对所选支付模式，仅在对应条件通过后调用经就绪检查 [[launch-readiness-5](launch-readiness.md#launch-readiness-5)] 的支付方式，并明确标示模式：

| 模式 | 付款前条件 |
| --- | --- |
| 真实支付 | 每个订单行对当前收货目的地均通过售卖就绪核验 [[launch-readiness-14](launch-readiness.md#launch-readiness-14)]；任一行未就绪则整单不得发起收款 |
| 测试支付 | 隔离测试流程已就绪 [[launch-readiness-13](launch-readiness.md#launch-readiness-13)]，不得发起真实扣款 |

### cart-checkout-14

给定对应待付款订单及库存占用仍有效 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)] [[market-catalog-11](market-catalog.md#market-catalog-11)]，且订单实际使用的限额优惠 [[content-marketing-13](content-marketing.md#content-marketing-13)] 与积分 [[customer-account-19](customer-account.md#customer-account-19)] 占用仍有效（若有），当支付成功结果被核对，结账流程应原子地将该订单标为已付款并按下表保存模式、已确认付款额度、币种、结果与交易引用，仅对实际使用的优惠 [[content-marketing-14](content-marketing.md#content-marketing-14)] 与积分 [[customer-account-20](customer-account.md#customer-account-20)] 确认使用：

| 支付模式 | 已确认付款额度与引用 |
| --- | --- |
| 真实支付 | 实际收款金额与原收款交易引用 |
| 测试支付 [[cart-checkout-18](#cart-checkout-18)] | 隔离的模拟付款金额与测试交易引用，不记录为真实收款 |

### cart-checkout-15

当支付被确认为失败，结账流程应将待付款订单标为付款失败、释放对应库存占用 [[market-catalog-12](market-catalog.md#market-catalog-12)] 及实际使用的限额优惠占用 [[content-marketing-15](content-marketing.md#content-marketing-15)] 和积分占用 [[customer-account-21](customer-account.md#customer-account-21)]（若有），并保留可重试的结账记录。

### cart-checkout-16

当同一报价提交或付款尝试的事件重复到达，结账流程应按原订单及支付尝试识别重复事件并只保留一次业务效果：

| 重复事件 | 仅一次的效果 |
| --- | --- |
| 重复提交已确认报价 | 待付款订单 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)]、库存 [[market-catalog-11](market-catalog.md#market-catalog-11)]、优惠 [[content-marketing-13](content-marketing.md#content-marketing-13)] 与积分占用 [[customer-account-19](customer-account.md#customer-account-19)] |
| 重复支付结果 | 付款状态、优惠使用 [[content-marketing-14](content-marketing.md#content-marketing-14)] 与积分使用 [[customer-account-20](customer-account.md#customer-account-20)] 或冲回 [[customer-account-13](customer-account.md#customer-account-13)] |

### cart-checkout-17

当顾客在已确认付款失败后重试，结账流程应重新核对当前报价与可售性 [[market-catalog-7](market-catalog.md#market-catalog-7)]，并在顾客确认后建立关联原失败订单的新待付款订单及库存占用 [[cart-checkout-22](#cart-checkout-22)]，保留原订单快照不变。

### cart-checkout-18

给定支付方式为测试模式，当顾客确认付款，结账流程应明确标示不会产生真实扣款，且测试结果不得表示真实收款授权。

### cart-checkout-22

当顾客提交已确认的最终报价，结账流程应先核对真实交易的每个商品行对收货目的地均可售 [[launch-readiness-14](launch-readiness.md#launch-readiness-14)]，再按已选真实或测试交易模式原子地保存待付款订单快照 [[orders-fulfillment-1](orders-fulfillment.md#orders-fulfillment-1)]、占用同模式变体库存 [[market-catalog-11](market-catalog.md#market-catalog-11)] 及报价实际使用的限额优惠资格 [[content-marketing-13](content-marketing.md#content-marketing-13)] 和积分抵扣额 [[customer-account-19](customer-account.md#customer-account-19)]；真实交易有任一行未就绪、任一所需占用失败或测试流程缺少所需隔离资源时，应不创建可付款订单、不发起付款并逐行说明原因，且不得借用正式可售量或正式权益 [[launch-readiness-9](launch-readiness.md#launch-readiness-9)]。

### cart-checkout-23

当付款结果未明，结账流程应将订单标为待核对、保留库存 [[market-catalog-11](market-catalog.md#market-catalog-11)]、实际使用的限额优惠 [[content-marketing-13](content-marketing.md#content-marketing-13)] 与积分占用 [[customer-account-19](customer-account.md#customer-account-19)]（若有）及支付引用、向有权员工展示待核对任务，并在核清结果前阻止再次扣款或实物履约。

### cart-checkout-24

当已核实的付款成功结果无法应用到原订单、库存或本订单实际使用的权益占用 [[cart-checkout-22](#cart-checkout-22)]，结账流程应将异常交给有权人员核对，并在原订单与权益状态修复或原支付模式退款成功 [[after-sales-25](after-sales.md#after-sales-25)] 前保持未结异常，不得生成第二笔扣款或授权实物履约。

### cart-checkout-25

当待付款订单达到已配置的占用期限且付款被核实为未发起，结账流程应将订单标为已失效并释放对应库存占用 [[market-catalog-12](market-catalog.md#market-catalog-12)] 及实际使用的限额优惠占用 [[content-marketing-15](content-marketing.md#content-marketing-15)] 与积分占用 [[customer-account-21](customer-account.md#customer-account-21)]（若有）；结果待核对的付款不得按超时直接释放。

### cart-checkout-26

当有权人员核对结果未明的付款，结账流程应依据原支付尝试引用查询受理方结果，并按核实结果处理原订单：

| 核实结果 | 处理 |
| --- | --- |
| 成功且原订单与占用有效 | 标为已付款 [[cart-checkout-14](#cart-checkout-14)] |
| 成功但原订单或占用无效 | 转入修复或退款异常 [[cart-checkout-24](#cart-checkout-24)] |
| 失败 | 标为失败并释放占用 [[cart-checkout-15](#cart-checkout-15)] |
| 仍无法确认 | 保持待核对且不再次扣款 [[cart-checkout-23](#cart-checkout-23)] |

## 验证

### cart-checkout-19

当在系统环境执行购物车与报价情形矩阵，验证者应逐项断言可见结果：

| 情形 | 断言 |
| --- | --- |
| 加入指定变体 | 行、数量、市场币种和价格正确 [[cart-checkout-1](#cart-checkout-1)] |
| 增减数量及删除行 | 对应行与总额更新且超量被阻止 [[cart-checkout-2](#cart-checkout-2)] |
| 离开再返回 | 有效行恢复，失效行有说明 [[cart-checkout-3](#cart-checkout-3)] |
| 切换市场 | 重新报价且旧报价不能提交 [[cart-checkout-4](#cart-checkout-4)] |
| 游客进入结账 | 无注册门槛且可填联系与地址 [[cart-checkout-5](#cart-checkout-5)] |
| 会员进入结账 | 可选保存或新地址 [[cart-checkout-6](#cart-checkout-6)] |
| 无效或不可配送地址 | 指出具体问题 [[cart-checkout-7](#cart-checkout-7)] |
| 有效地址 | 可选配送服务、费用和时效可见 [[cart-checkout-8](#cart-checkout-8)] |
| 有效和无效优惠 | 折扣正确或原因明确 [[cart-checkout-9](#cart-checkout-9)] |
| 有税、明确零税及无规则地址 | 逐项费用和税务依据正确，无规则时无可付款报价 [[cart-checkout-10](#cart-checkout-10)] |
| 提交前改价或费用 | 显示差异并要求重新确认 [[cart-checkout-11](#cart-checkout-11)] |
| 缺少商家配置 | 拒绝提交且指出缺项 [[cart-checkout-12](#cart-checkout-12)] |

### cart-checkout-20

当在集成环境执行支付与重试情形矩阵，验证者应逐项断言持久结果：

| 情形 | 断言 |
| --- | --- |
| 已确认报价付款 | 仅在订单、库存和所需权益占用持久化后使用配置的支付模式 [[cart-checkout-13](#cart-checkout-13)] |
| 无优惠且积分未启用的普通付款、使用权益的真实付款及测试付款 | 均可确认成功；真实实收与隔离测试模拟额度及各自引用分开保存，仅实际使用的权益被确认 [[cart-checkout-14](#cart-checkout-14)] |
| 确认失败 | 订单标失败，占用释放且可重试 [[cart-checkout-15](#cart-checkout-15)] |
| 双击与重复回报 | 订单、库存、优惠和积分效果均仅一次 [[cart-checkout-16](#cart-checkout-16)] |
| 失败后变价再重试 | 重新核价确认，新待付款订单关联原失败订单且原快照不变 [[cart-checkout-17](#cart-checkout-17)] |
| 测试模式付款 | 无真实扣款声明或真实收款授权 [[cart-checkout-18](#cart-checkout-18)] |
| 一就绪行与一未就绪行混合购物车、并发抢购同一库存或权益，及订单写入失败 | 混合整单不形成可付款订单；仅全部行就绪且订单与所需占用原子成功者可付款，测试订单不占正式资源 [[cart-checkout-22](#cart-checkout-22)] |
| 待付款混合订单中一行变为未就绪 | 整单付款受阻且未发起扣款 [[cart-checkout-13](#cart-checkout-13)] |
| 支付结果未明 | 订单待核对，禁止二次扣款与履约 [[cart-checkout-23](#cart-checkout-23)] |
| 查询原付款引用得到成功、失败或仍未知 | 仅已核实结果推进订单 [[cart-checkout-26](#cart-checkout-26)] |
| 付款成功但订单、库存或权益状态写入失败 | 核对后修复或退款，绝不二次扣款或交运 [[cart-checkout-24](#cart-checkout-24)] |
| 未发起付款超时及付款待核对 | 仅已核实未发起的订单因超时释放占用 [[cart-checkout-25](#cart-checkout-25)] |

### cart-checkout-21

当在系统环境执行从选品到下单的组合路径，验证者应断言指定变体进入购物车 [[cart-checkout-1](#cart-checkout-1)]、游客或会员可完成结账 [[cart-checkout-5](#cart-checkout-5)] [[cart-checkout-6](#cart-checkout-6)]、最终报价经确认 [[cart-checkout-10](#cart-checkout-10)] [[cart-checkout-11](#cart-checkout-11)]、付款前订单、库存与所需权益占用均成立 [[cart-checkout-22](#cart-checkout-22)]，且支付成功只更新该订单一次 [[cart-checkout-14](#cart-checkout-14)] [[cart-checkout-16](#cart-checkout-16)]。
