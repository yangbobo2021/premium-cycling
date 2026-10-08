<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# content-marketing: 品牌内容与促销

## 意图

本候选包帮助顾客理解品牌、骑行技术和商品用途，并使促销承诺与可用规则一致。
正式品牌、站点语言、内容授权和活动政策仍待商家确认。

## 外部行为

### content-marketing-1

当访客进入内容入口，商店应展示当前站点语言 [[market-catalog-1](market-catalog.md#market-catalog-1)] 下已发布的品牌、技术和骑行内容列表。

### content-marketing-2

当访客打开文章，商店应显示标题、正文、发布时间及与内容相关的已发布商品入口 [[market-catalog-4](market-catalog.md#market-catalog-4)]。

### content-marketing-3

当公众请求非公开内容，商店应从公开列表、导航和直接访问中隐藏该内容：

| 内容状态 | 公开结果 |
| --- | --- |
| 草稿或尚未发布 | 不可公开访问 |
| 已撤回 | 不可公开访问，保留员工可见历史 |

### content-marketing-4

当文章包含有权使用的视频，商店应提供标题、封面或替代说明及可用播放入口，并标明外部平台来源。

### content-marketing-5

当视频链接无效或嵌入不可用，商店应呈现可理解的降级状态并保持文章正文可读。

### content-marketing-6

当有权员工编辑内容草稿，商店应保存修改并提供仅授权人员可见的预览。

### content-marketing-7

当有权员工发布促销，商店应保存适用市场 [[market-catalog-1](market-catalog.md#market-catalog-1)]、商品、时间、资格、叠加与使用限制，并只向符合条件的顾客展示。

### content-marketing-8

当促销进入不可再使用的状态，商店应停止向顾客展示可用承诺：

| 状态原因 | 对新购买的结果 |
| --- | --- |
| 到达结束时间 | 不再应用该促销 |
| 被有权员工撤回 | 不再应用该促销 |
| 达到使用上限 | 不再应用该促销 |

### content-marketing-9

当访客查看联系、配送、退换、保修、隐私和服务条款页面，商店应显示适用市场 [[market-catalog-1](market-catalog.md#market-catalog-1)]、已生效政策版本 [[merchant-operations-10](merchant-operations.md#merchant-operations-10)] 及生效时间。

### content-marketing-11

当有权员工发布内容，商店应记录发布时间并使该版本进入公开内容入口。

### content-marketing-12

当有权员工撤回内容，商店应记录撤回时间并停止公开该内容。

## 验证

### content-marketing-10

当在系统环境执行内容与促销情形矩阵，验证者应逐项断言公开结果：

| 情形 | 断言 |
| --- | --- |
| 浏览内容入口 | 仅当前语言已发布内容可见 [[content-marketing-1](#content-marketing-1)] |
| 打开文章 | 标题、正文、时间及商品入口正确 [[content-marketing-2](#content-marketing-2)] |
| 草稿或撤回内容 | 列表、导航及直接访问均不可见 [[content-marketing-3](#content-marketing-3)] |
| 正常视频 | 来源与播放入口可见 [[content-marketing-4](#content-marketing-4)] |
| 视频链接失效 | 有降级提示且文章可读 [[content-marketing-5](#content-marketing-5)] |
| 编辑及预览草稿 | 修改持久且预览仅授权人员可见 [[content-marketing-6](#content-marketing-6)] |
| 发布内容 | 版本进入公开入口并有发布时间 [[content-marketing-11](#content-marketing-11)] |
| 撤回内容 | 内容停止公开并留撤回时间 [[content-marketing-12](#content-marketing-12)] |
| 发布有效及不适用促销 | 仅合格顾客可见且规则完整 [[content-marketing-7](#content-marketing-7)] |
| 失效、撤回或用尽促销 | 不再公开承诺或应用新优惠 [[content-marketing-8](#content-marketing-8)] |
| 查看各服务页面 | 市场、生效时间和版本可见 [[content-marketing-9](#content-marketing-9)] |
