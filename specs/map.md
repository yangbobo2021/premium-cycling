<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->
<!-- spex-i18n-source: map.md sha256-5dbf6d5bf1f09c74f8bf71209986eca460723957c6861f0a73654b88d9e522d9 -->

# 规约地图

用于快速定位决策和规约包的索引。
规约条目是事实来源。
开发过程中，代码可能与规约暂时不一致。

## 编写和审阅规约

在编写、修改或审阅 DR、IR 或条目前，先了解 [`meta.md`](meta.md) 中的规则。

## 目录结构

```text
decisions/    决策记录（DRs）
intents/      意图记录（IRs）
packages/     规约包（每包一个文件）
map.md        本索引
meta.md       规约的规约
```

## 决策

| ID | 文件 | 摘要 |
| --- | --- | --- |
| [DR-000](decisions/000-spec-structure-format.md) | 000-spec-structure-format.md | 规约结构、格式和命名约定 |
| [DR-001](decisions/001-candidate-business-requirements.md) | 001-candidate-business-requirements.md | 首版中文业务候选需求的来源、边界与待定决策 |
| [DR-002](decisions/002-ai-project-experiment.md) | 002-ai-project-experiment.md | AI 完整项目开发实验的目标与完成判断依据 |

## 规约包

| 文件 | 摘要 |
| --- | --- |
| [git.md](packages/git.md) | 提交信息格式和 AI 共同作者 trailers |
| [licensing.md](packages/licensing.md) | SPDX 头要求与验证检查 |
| [market-catalog.md](packages/market-catalog.md) | 候选：市场、商品、价格、变体与库存 |
| [product-selection.md](packages/product-selection.md) | 候选：搜索、比较、整车选型与配件兼容 |
| [cart-checkout.md](packages/cart-checkout.md) | 候选：购物车、报价、结账与支付边界 |
| [orders-fulfillment.md](packages/orders-fulfillment.md) | 候选：订单快照、状态与整车／配件履约 |
| [after-sales.md](packages/after-sales.md) | 候选：取消、退换、退款、保修与维修 |
| [customer-account.md](packages/customer-account.md) | 候选：顾客身份、地址、收藏、评价与积分 |
| [customer-support.md](packages/customer-support.md) | 候选：客服会话、分配转派与通知 |
| [content-marketing.md](packages/content-marketing.md) | 候选：品牌内容、骑行内容、视频与促销 |
| [merchant-operations.md](packages/merchant-operations.md) | 候选：员工权限、业务规则、队列与审计 |
| [site-quality.md](packages/site-quality.md) | 候选：响应式、无障碍、SEO、安全与恢复 |
| [launch-readiness.md](packages/launch-readiness.md) | 候选：商家资料、政策、渠道与上线就绪 |
