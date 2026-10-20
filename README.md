<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2026 SubLang International <https://sublang.ai> -->

# Premium Cycling · AI 项目开发实验

这是一个由 AI 编写项目的实验，以“销售高端自行车及配件的出海独立站”为实际业务场景，验证 AI 是否能够完整完成一个具有实际使用需求的项目。

实验的目的在于检验 AI 从需求梳理、方案设计、开发实现，到测试、问题修复和交付的完整能力。
商业上线和经营收益不作为本实验的目标；自行车电商场景用于提供足够具体的业务规则、跨流程协作和可验证的结果。
实验定位见 [DR-002](specs/decisions/002-ai-project-experiment.md)。

## 验证什么

- 能否将实际使用需求整理成清晰、一致、可以验证的规约。
- 能否完成顾客选购、结账、订单履约、售后及商家运营等相互关联的流程。
- 能否通过实际执行和证据发现问题，完成修复并验证最终结果。
- 能否保留需求、决策、实现与验证过程，使他人能够检查完成程度和剩余问题。

## 当前阶段

目前处于需求规约与黑盒测试设计阶段，尚未实现网站，也没有应用启动或部署入口。

| 内容 | 当前状态 |
| --- | --- |
| 需求规约 | 已编写首版中文候选规约，覆盖商品与市场、选型与兼容、结账支付、订单履约、售后、顾客账户、客服、营销、商家运营及站点质量等业务 |
| 业务输入 | 目标市场、品牌、商品资料、支付渠道和经营政策等仍有待确定，边界见 [DR-001](specs/decisions/001-candidate-business-requirements.md) |
| 黑盒测试设计 | 需求快照、场景、方法、设计审查记录及辅助文件已纳入 GitHub 仓库，见 [黑盒场景设计报告](tests/delivery-acceptance/black-box-design-report.md) |
| 应用实现与验收 | 尚未完成应用实现、应用测试执行和交付验收，完整项目开发能力仍待后续实验验证 |

规约中的功能描述表示预期行为，设计审查结果只用于判断测试设计是否充分。
项目最终完成情况需要以可运行的实现、实际测试和交付证据判断。

## 目录结构

当前 GitHub 仓库中的主要文件如下：

```text
premium-cycling/
├── README.md                 # 实验用途、当前阶段与阅读入口
├── AGENTS.md                 # AI 在本项目中的工作约定
├── LICENSE                   # Apache-2.0 许可证
├── specs/
│   ├── map.md                # 规约索引
│   ├── meta.md               # 规约格式、组织与引用规则
│   ├── decisions/            # 项目决策、需求来源与实验定位
│   ├── intents/              # 开发意图、任务与验证计划
│   └── packages/             # 按业务意图组织的规约包及工程约定
└── tests/
    └── delivery-acceptance/   # 需求快照、场景、方法与设计审查台账
        ├── review-history/   # 历史审查及中文化前的快照
        ├── scripts/          # 导出、场景生成、审查等辅助脚本
        └── …                # 设计报告、截图、日志与工作流记录
```

`tests/delivery-acceptance/` 已纳入版本管理，克隆公开仓库即可获得测试设计资产。
历史记录中保留了采集时的本地绝对路径、端口、源码版本和阶段结论，用于追溯当时的过程；其中的路径和服务地址需要结合自己的环境调整。
辅助脚本依赖生成时的工具环境，仓库中的记录与截图不代表相关本地服务仍在运行。

## 如何阅读

1. 从 [规约地图](specs/map.md) 查找业务范围和相关规约包。
2. 阅读 [实验定位](specs/decisions/002-ai-project-experiment.md) 和 [候选需求来源与边界](specs/decisions/001-candidate-business-requirements.md)，了解实验目标与待定事项。
3. 查看 `specs/packages/` 中各包的预期行为和验证要求；编写或修改规约前，先阅读 [规约定义](specs/meta.md)。
4. 从 [黑盒场景设计报告](tests/delivery-acceptance/black-box-design-report.md) 了解设计范围，再查看 [场景说明](tests/delivery-acceptance/black-box-scenarios.md) 和 [待定业务输入](tests/delivery-acceptance/pending-business-inputs.json)。

## 许可证

本项目使用 [Apache License 2.0](LICENSE)。
