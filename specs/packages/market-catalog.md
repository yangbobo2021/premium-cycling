<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# market-catalog: 市场与商品目录

## 意图

本候选包使顾客按可服务市场识别真实可售的自行车与配件，并使商家维护可核对的商品、价格和库存。
所售类别、市场、币种及真实数据仍待业务确认。

## 外部行为

### market-catalog-1

给定商家已启用一个市场，当顾客进入商店，商店应显示当前市场、适用的站点语言和报价币种。

### market-catalog-2

当顾客切换到另一个已启用市场，商店应重新展示该市场可售商品及其独立报价，并标示原市场商品的不可售或变价结果。

### market-catalog-3

当顾客请求未启用的市场，商店应说明该地区暂不可购买，且不提供该地区的结账入口。

### market-catalog-4

当顾客浏览目录，商店应按自行车与配件的已配置类别展示已发布商品，并清楚标示缺货商品。

### market-catalog-5

当顾客打开已发布商品详情，商店应显示名称、类别、品牌、图片或明确的无图状态、可核实规格、价格币种及购买条件。

### market-catalog-6

当顾客选择商品变体，商店应显示该变体的唯一标识、规格、当前市场价格和可售状态。

### market-catalog-7

当某变体在当前市场下架或无可售库存，商店应阻止该变体进入新的有效订单并说明原因。

### market-catalog-8

当有权员工新增或修改商品及变体，商店应保存其类别、规格、市场可售性、价格、媒体来源和发布状态。

### market-catalog-9

当有权员工发布商品，商店应拒绝缺少该商品类别所需的真实规格、当前市场价格或合法使用的素材，并指出缺项。

### market-catalog-10

当有权员工调整库存，商店应记录目标变体、调整前后数量、原因、操作者和时间。

### market-catalog-11

当有效订单占用某变体库存，商店应仅减少该变体可售量并保留可追溯占用记录。

### market-catalog-12

当有效订单的库存占用被合法释放，商店应仅恢复对应变体的可售量且重复释放不产生额外库存。

### market-catalog-13

当同一变体的购买请求超过可售量，商店应拒绝超量部分并向顾客显示可用数量或缺货状态。

### market-catalog-14

当商品媒体不可用，商店应展示明确的无图状态而不显示破损图片或未经授权的替代素材。

## 验证

### market-catalog-15

当在系统环境执行市场与目录情形矩阵，验证者应逐项断言可见结果：

| 情形 | 断言 |
| --- | --- |
| 进入已启用市场 | 显示该市场、语言和币种 [[market-catalog-1](#market-catalog-1)] |
| 切换市场 | 重新报价并标示不可售或变价 [[market-catalog-2](#market-catalog-2)] |
| 进入未启用市场 | 无该地区结账入口 [[market-catalog-3](#market-catalog-3)] |
| 浏览目录 | 已发布自行车与配件分类、缺货标记正确 [[market-catalog-4](#market-catalog-4)] |
| 打开详情 | 必要规格、价格、币种与图片状态可见 [[market-catalog-5](#market-catalog-5)] |
| 选择两个变体 | 标识、规格、报价和可售状态分别正确 [[market-catalog-6](#market-catalog-6)] |
| 下架或售罄 | 新订单被阻止且显示原因 [[market-catalog-7](#market-catalog-7)] |
| 媒体失效 | 显示无图状态且不显示破图 [[market-catalog-14](#market-catalog-14)] |

### market-catalog-16

当在集成环境执行商品维护与库存情形矩阵，验证者应逐项断言持久结果：

| 情形 | 断言 |
| --- | --- |
| 保存商品与变体 | 各字段和发布状态重载后保持 [[market-catalog-8](#market-catalog-8)] |
| 发布资料不完整的商品 | 发布失败并指出缺项 [[market-catalog-9](#market-catalog-9)] |
| 调整库存 | 数量、原因、操作者与时间可追溯 [[market-catalog-10](#market-catalog-10)] |
| 订单占用库存 | 仅目标变体可售量变化 [[market-catalog-11](#market-catalog-11)] |
| 重复释放占用 | 仅恢复一次目标变体库存 [[market-catalog-12](#market-catalog-12)] |
| 并发超量购买 | 超量请求被拒绝且可售量不为负 [[market-catalog-13](#market-catalog-13)] |
