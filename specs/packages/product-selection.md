<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# product-selection: 商品发现与选型

## 意图

本候选包帮助顾客找到适合用途的自行车和配件，并在尺码、几何或兼容资料不足时避免作出无依据的保证。
具体车种、尺码表、几何数据和配件类型仍待商家提供及确认。

## 外部行为

### product-selection-1

当顾客按关键词搜索，商店应返回当前市场已发布商品 [[market-catalog-4](market-catalog.md#market-catalog-4)] 的相关结果，或说明无结果并提供继续浏览的入口。

### product-selection-2

当顾客组合商品类别与规格 [[market-catalog-5](market-catalog.md#market-catalog-5)]、当前价格 [[market-catalog-6](market-catalog.md#market-catalog-6)] 或可售状态 [[market-catalog-7](market-catalog.md#market-catalog-7)] 筛选，商店应只显示同时满足条件的商品并允许清除任一条件。

### product-selection-3

当顾客选择排序规则，商店应按所标示规则排序结果并保持筛选条件。

### product-selection-4

当顾客选择多个可比较商品，商店应并列展示商品详情中已核实的规格 [[market-catalog-5](market-catalog.md#market-catalog-5)]，并将缺失值明确标为未知。

### product-selection-5

当顾客打开整车选型信息，商店应显示对应商品详情 [[market-catalog-5](market-catalog.md#market-catalog-5)] 中商家提供的尺码范围、几何参数及各数据的适用车型或变体。

### product-selection-6

给定商家提供了适用的选型规则，当顾客输入规则要求的身体尺寸和骑行偏好，商店应返回候选车架尺码及所用依据。

### product-selection-7

当顾客的选型输入不能得出唯一有依据的尺码，商店应提示不确定性和需补充的信息，且不宣称唯一合适尺码：

| 原因 | 提示重点 |
| --- | --- |
| 落在相邻尺码边界 | 展示有依据的候选尺码与需核对的骑姿信息 |
| 超出规则适用范围 | 说明规则不适用并引导人工确认 |
| 必需数据缺失 | 指明缺失的身体尺寸或车型参数 |

### product-selection-8

当顾客查看配件与整车的兼容信息，商店应显示已验证的适配结论、对应变体 [[market-catalog-6](market-catalog.md#market-catalog-6)] 的型号／规格及资料来源或核验时间。

### product-selection-9

当所选配件与整车变体的兼容结论缺乏充分依据 [[market-catalog-6](market-catalog.md#market-catalog-6)]，商店应标示尚不能确认适配，并提供核对规格或咨询的路径：

| 资料问题 | 提示重点 |
| --- | --- |
| 资料缺失 | 指明待核对的接口或尺寸 |
| 核验资料过期 | 标示最后核验时间 |
| 资料与所选变体不匹配 | 指明不匹配的型号或规格 |

### product-selection-10

当员工更新选型或兼容资料，商店应保存适用型号、数据来源、核验者与更新时间，并使公开结论随有效资料更新。

## 验证

### product-selection-11

当在系统环境执行发现与比较情形矩阵，验证者应逐项断言顾客看到的结果：

| 情形 | 断言 |
| --- | --- |
| 命中与无命中搜索 | 仅出现适用商品，空结果有浏览路径 [[product-selection-1](#product-selection-1)] |
| 叠加和清除筛选 | 结果同时符合条件并正确恢复 [[product-selection-2](#product-selection-2)] |
| 改变排序 | 顺序符合标示规则且筛选保留 [[product-selection-3](#product-selection-3)] |
| 比较不同车型 | 相同含义规格对齐，缺值标未知 [[product-selection-4](#product-selection-4)] |

### product-selection-12

当在系统或集成环境执行选型与兼容情形矩阵，验证者应逐项断言信息边界：

| 情形 | 断言 |
| --- | --- |
| 查看有数据的整车 | 尺码和几何参数对应正确变体 [[product-selection-5](#product-selection-5)] |
| 输入规则内尺寸 | 候选尺码及规则依据可见 [[product-selection-6](#product-selection-6)] |
| 边界、超范围和缺数据 | 提示不确定性且无唯一适配保证 [[product-selection-7](#product-selection-7)] |
| 查看有依据的配件 | 结论、型号和来源可见 [[product-selection-8](#product-selection-8)] |
| 资料缺失或不匹配 | 显示不能确认及核对路径 [[product-selection-9](#product-selection-9)] |
| 更新来源资料 | 公开结论与可追溯来源一致 [[product-selection-10](#product-selection-10)] |
