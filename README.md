# Jarvis

中文 | [English](README.en.md)

Jarvis 是一个目标驱动的产品交付 Skill。它通过有限的 Loop Engineering，
把一句产品想法推进为经过验证、可工作的软件，同时避免把交付变成文档和审批关卡。

```text
发现 -> 定义 -> 执行 -> 观察 -> 验证 -> 记录 -> 继续或停止
```

## 用一句话开始新项目

例如：

> 用 Jarvis 做一个面向农场主的农机预约平台。

Jarvis 不会先要求用户填写完整需求表，也不会立即盲目生成全部代码。它会按以下流程开始：

1. **理解目标**
   - 明确用户、核心问题、主要功能、非目标和完成证据。
   - 对普通、可逆的细节采用合理默认值并继续。
   - 只有产品方向、权限、预算或难以撤销的共享决策会询问用户。
2. **检查项目环境**
   - 读取仓库规则、现有代码、依赖、组件库、Git 状态和仍然有效的证据。
   - 空项目选择满足目标的最简单技术路径；已有项目优先沿用附近模式。
3. **确定产品骨架**
   - 提炼核心用户 Journey、必要页面、路由、导航、状态和共享业务规则。
   - 多页面项目只保留粗粒度 Product Plan；Page Overview 和 Development Guide
     仅在真实下游消费者需要时创建。
4. **确定 UI 来源**
   - 新 UI、新页面族和重大视觉重设计默认使用 GPT Image 2 生成视觉基线。
   - 用户已提供或明确选择 Figma/图片设计稿时，将其作为视觉来源；可调用
     `product-design` 辅助理解和还原。
   - 重大视觉方向获得一次人工批准后，再持续实现页面。
5. **选择开发顺序**
   - 默认先交付最小 walking skeleton 或 vertical slice。
   - 契约稳定且需要尽早看到产品时，采用 Visible-first：应用外壳、路由、导航、
     可见页面和状态先完成，再按 Journey 接入后端。
   - 鉴权、支付、库存、迁移等高风险边界先做最小真实探针，避免晚期返工。
6. **实现页面**
   - 优先复用项目已有组件库。功能机制相同但样式不同，也优先保留成品组件行为，
     只覆盖必要样式。
   - UI 直接按最终成品呈现，不向用户显示“暂无接口”“Mock data”“测试成功”、
     TODO 或开发说明等占位文字。
7. **接通真实能力**
   - 从核心 Journey 开始接入 API、数据库、权限和外部副作用。
   - 每完成一个 Journey，就形成一个可观察、可验收的真实切片。
8. **在交付节点验证**
   - 页面切片完成时运行 Focused gate。
   - 共享组件或契约变化时运行 Affected gate。
   - 跨页面流程接通时运行 Journey gate。
   - 准备发布时才运行 Release gate。
   - 不在每次编辑或每个组件完成后重复全量编译和测试。
9. **支持长任务与跨会话恢复**
   - 在真实跨会话、长时间 provider 或不确定外部副作用边界写入
     `project-state/current.json`。
   - 恢复时重新核对代码、Git 和证据，旧状态不能替代当前事实。
10. **根据证据完成**
    - 区分单元完成、Journey 完成和产品可发布。
    - 只有范围内声明都有新鲜证据，且没有剩余必需工作时，才宣布完成。

简化后的启动路径：

```text
一句话目标
  -> 补全最少产品语义
  -> 检查仓库与组件库
  -> 确定核心 Journey 与视觉来源
  -> 建立外壳、路由和可见页面
  -> 按 Journey 接入真实后端
  -> 在交付节点验证
  -> 持续交付至 Product ready
```

核心体验：**少问、先让产品可见、优先复用、按真实 Journey 补齐能力，最后用证据判断完成。**

## 架构

Jarvis 只暴露一个可安装 Skill，并仅在当前交付单元需要时加载三个内部能力：

| 组件 | 职责 |
|---|---|
| `jarvis` | 负责结果、规划层级、集成和最终验收 |
| Product Design | 消除产品、交互和视觉不确定性 |
| Solution Design | 选择技术边界和实现路径 |
| Product Build | 实现并验证可工作的 vertical slice |

共享策略位于 `core/`，能力模块位于 `capabilities/`，产品默认值位于
`golden-paths/`，功能默认值位于 `recipes/`。Jarvis 始终保留项目目标、集成和验收责任。

## 核心原则

- 现有仓库事实优先于通用最佳实践。
- 围绕一个有限目标循环，从当前事实和证据选择最有价值、未阻塞的交付单元。
- 远期工作保持粗粒度，只细化当前需要决策和实现的单元。
- 在实质执行前明确声明、证据、权限、预算和停止条件。
- 可逆、低影响的决定自动完成并记录假设；只询问方向、权限、秘密、生产副作用和难逆决策。
- 批量完成 coherent change；按风险而非编辑频率选择检查。
- 使用能推翻完成声明的最小检查；失败证据用于重新规划。
- 只在真实消费者需要时生成 Product Plan、Page Overview、Development Guide 或其他产物。
- 新视觉界面默认使用 GPT Image 2；只有用户提供、选择或明确要求时才使用 Figma。
- Product Truth、Visual Truth、实现选择和验证证据保持分离。
- Skill、插件、模型和服务都是有边界的 provider；Jarvis 保留目标、权限、状态、预算和完成责任。
- 仅委派上下文闭合、可独立验收的工作；子代理自报完成不能替代 Jarvis 验收。
- 发布、部署、发送消息、迁移、删除、收费或创建外部资源前，重新核对权限与外部状态。

## 仓库结构

```text
skills/jarvis/  可安装 Skill、行为评测和触发测试
capabilities/   Product Design、Solution Design、Product Build
core/           共享运行、决策、规划、质量和验证策略
golden-paths/   常见产品类型的默认路径
recipes/        常见功能类型的默认路径
examples/       示例项目
templates/      Product Plan、Page Overview、Development Guide 和状态模板
evals/          评测说明与交付 canary
scripts/        状态、打包、评测和仓库验证工具
tests/          确定性回归测试
docs/           已批准的设计和实施计划
```

## 验证

需要 Python 3.10 或更高版本，无第三方 Python 包依赖。

```powershell
python scripts/validate.py
python scripts/package_skills.py --check
python -m unittest discover -s tests -v
```

持久状态使用 JSON，可以在不引入第三方依赖的情况下验证和恢复：

```powershell
python scripts/state.py init project-state/current.json --goal "Ship the core flow"
python scripts/state.py reconcile project-state/current.json --repo . --write
```

在真实跨会话边界记录安全的下一步和可恢复的进行中工作：

```powershell
python scripts/state.py checkpoint project-state/current.json `
  --goal "Ship the core flow" `
  --next-action "Inspect Image 2 job before retry" `
  --in-flight-id image2-1 --kind provider --target image-generation `
  --resume-action "Query image2-1 and inspect its output"
```

结构检查适合作为低成本 CI gate。模型行为评测和交付 canary 会消耗模型容量，
因此需要显式运行：

```powershell
python scripts/run_evals.py behavior --ids 22 --output .jarvis-evals/behavior-22.json
python scripts/run_evals.py benchmark --ids 22 --model gpt-5.6-sol --output .jarvis-evals/benchmark-22.json
python scripts/run_evals.py canary-benchmark --ids 2 --model gpt-5.6-terra --output .jarvis-evals/canary-benchmark-2.json
python scripts/run_evals.py canary --output .jarvis-evals/canaries.json
python scripts/run_evals.py probe --output .jarvis-evals/capabilities.json
```

## 打包安装

生成一个自包含的 Skill 目录：

```powershell
python scripts/package_skills.py
```

实时开发时，可把 `skills/jarvis` 直接链接到代理使用的 Skill 目录，使源码修改立即生效。
只有需要在仓库外分发独立副本时才使用 `dist/jarvis`；它包含全部引用、状态工具和评测夹具。

## 当前状态

V0.11 使用 Loop Engineering 作为运行模型：一个有限外循环负责发现、定义、执行、
观察、验证、记录和依据证据终止。Goal、浏览器、Skill、worker 和恢复状态都是按需使用的
循环原语，不是强制阶段。

结构检查不能证明定性收敛。显式运行的行为评测器和隔离交付 canary 已覆盖 HTTP Journey、
中断恢复、真实浏览器流程和权限边界；更广泛的项目类型仍需要 Shadow Mode 对照验证。

## 许可证

MIT
