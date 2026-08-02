# Jarvis

**把一句产品想法，持续推进成经过验证、真正可用的软件。**

中文 | [English](README.en.md)

Jarvis 是一个面向 Codex 等 AI 编程代理的目标驱动产品交付 Skill。它让代理不只“写完代码”，还会围绕用户目标持续完成产品定义、设计、实现、验证与收尾。

你只需说：

> 用 Jarvis 做一个面向农场主的农机预约平台。

Jarvis 会从仓库真实状态出发，找到最重要的下一步，交付一个可观察、可验收的产品切片，再依据证据继续推进，直到目标完成或明确说明阻塞。

```text
一句话目标 → 产品可见 → 核心 Journey 可用 → 证据验证 → Product ready
```

## 为什么需要 Jarvis

普通编程代理擅长完成单个指令，却容易在长任务中偏离目标：需求越写越多、页面与后端脱节、测试通过但用户流程不可用，或者在脚手架刚搭好时就宣布完成。

Jarvis 解决的是“完整交付”问题：

- **目标不丢失**：跨页面、跨能力、跨会话仍围绕同一个产品结果推进。
- **少问，继续做**：可逆的小决定采用合理默认值；只把方向、权限和难以撤销的选择交给用户。
- **尽早看到产品**：优先建立 walking skeleton 或 vertical slice，让真实界面和核心流程尽快可见。
- **按 Journey 交付**：页面、API、数据、权限和外部服务围绕用户旅程接通，不堆孤立功能。
- **用证据判断完成**：检查真实代码、测试、浏览器、API 和数据，不把“生成了文件”当成交付成功。
- **长任务可恢复**：只在真正需要跨会话或等待外部能力时记录安全、可核对的恢复状态。
- **控制过程负担**：计划和文档按需生成，不把开发变成表格、审批和仪式。

## 适合什么任务

Jarvis 适合：

- 从一句想法启动新产品；
- 交付跨页面、前后端联动的完整功能；
- 接手中断、状态复杂或需要多轮推进的项目；
- 需要 AI 在较少人工干预下持续开发，同时保留权限与风险边界；
- 对 UI 一致性、真实业务流程和最终验收有要求的产品。

一次机械修改、只读审查、概念解释等简单任务，不需要启用 Jarvis。

## 快速开始

### 1. 安装

开发时，将 [`skills/jarvis`](skills/jarvis) 链接或复制到代理的 Skill 目录。这样源码修改可以立即生效。

需要分发自包含版本时运行：

```powershell
python scripts/package_skills.py
```

生成的 `dist/jarvis` 包含运行所需的能力模块、策略、状态工具和评测夹具，可以直接安装到目标环境。

### 2. 给出目标

不必先写完整 PRD。用自然语言说明想交付什么：

```text
用 Jarvis 为现有 CRM 增加从线索筛选、批量分配到跟进记录的完整流程。
```

如果有明确边界，一并说明即可：

```text
沿用现有技术栈和组件库；不要修改登录模块；以真实浏览器走通主管分配线索为验收标准。
```

### 3. 让证据驱动交付

Jarvis 会读取仓库规则与现有实现，补全最少的产品语义，选择当前最有价值的交付单元，并在每个关键边界验证结果。你可以随时补充、纠正、暂停或恢复目标。

## 它如何工作

Jarvis 使用有限的 **Loop Engineering**：

```text
发现 → 定义 → 执行 → 观察 → 验证 → 记录 → 继续或停止
```

每一轮只做一个连贯的交付切片：

1. **发现**：读取代码、Git、项目规则和已有证据，选择最高价值的未完成 Journey。
2. **定义**：明确本轮结果、非目标、权限边界、完成证据和停止条件。
3. **执行**：用最少的能力完成一个 coherent change。
4. **观察**：检查真实页面、API、数据、测试或外部反馈。
5. **验证**：将证据与声明逐项对照；失败就依据新事实调整。
6. **记录**：只保存后续确实会使用的产品真相或恢复状态。
7. **继续或停止**：接受当前切片并进入下一轮，重新定义路径，或诚实终止。

这不是无限自我反思，也不是把所有工作拆成流程关卡。简单、明确、可逆的任务会走快速路径；鉴权、支付、迁移、生产数据等高风险边界才会提高验证和确认强度。

## 产品交付方式

### UI 先有可信视觉基线

新 UI、新页面族和重大视觉重设计默认使用 GPT Image 2 生成视觉基线。用户已经提供或明确选择 Figma/图片设计稿时，以该设计为视觉来源。实现时优先复用现有组件库，并同时检查局部细节与完整页面效果。

### 后端围绕真实 Journey 接通

Jarvis 从核心用户旅程开始连接 API、数据库、权限和外部副作用。它不会用“Mock 成功”“暂无接口”或 TODO 冒充成品，也不会因为单元测试通过就宣称完整流程可用。

### 验证强度随风险变化

- 页面切片完成：运行聚焦检查；
- 共享组件或契约变化：验证受影响边界；
- 跨页面流程接通：运行 Journey 验收；
- 准备发布：执行 Release gate；
- 鉴权、收费、删除、迁移和生产副作用：重新核对权限与真实外部状态。

## 核心设计

Jarvis 对外只暴露一个可安装 Skill，内部能力按当前交付缺口加载：

| 组件 | 作用 |
|---|---|
| `jarvis` | 保持目标、权限、计划、集成与最终验收一致 |
| Product Design | 消除产品、交互和视觉不确定性 |
| Solution Design | 选择技术边界与实现路径 |
| Product Build | 实现并验证可工作的 vertical slice |

项目结构保持克制：

```text
skills/jarvis/  对外安装入口、行为评测与触发测试
core/           共享运行、决策、规划、质量与验证策略
capabilities/   Product Design、Solution Design、Product Build
golden-paths/   常见产品类型的默认交付路径
recipes/        常见功能的实现与验证默认值
templates/      按需使用的计划、页面、开发与恢复模板
evals/          行为评测与隔离交付 canary
scripts/        打包、状态、评测和仓库验证工具
tests/          确定性回归测试
```

## 开发与验证

要求 Python 3.10+，无第三方 Python 包依赖。

```powershell
python scripts/validate.py
python scripts/package_skills.py --check
python -m unittest discover -s tests -v
```

结构检查只能证明仓库和包结构有效，不能单独证明代理行为改善。行为评测与交付 canary 需要显式运行：

```powershell
python scripts/run_evals.py behavior --ids 22 --output .jarvis-evals/behavior-22.json
python scripts/run_evals.py benchmark --ids 22 --model gpt-5.6-sol --output .jarvis-evals/benchmark-22.json
python scripts/run_evals.py canary --output .jarvis-evals/canaries.json
python scripts/run_evals.py probe --output .jarvis-evals/capabilities.json
```

持久恢复状态使用 JSON，可通过 [`scripts/state.py`](scripts/state.py) 初始化、核对和更新。常规编辑无需创建状态文件。

参与贡献前，请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。版本变化见 [`CHANGELOG.md`](CHANGELOG.md)。

## 当前状态

当前版本以 Loop Engineering 为运行模型，并提供 HTTP Journey、中断恢复、真实浏览器流程和权限边界的隔离交付 canary。更广泛的项目类型仍需要通过 Shadow Mode 对照验证。

## License

[MIT](LICENSE)
