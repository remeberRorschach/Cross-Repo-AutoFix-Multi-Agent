# 🛠️ Cross-Repo AutoFix Multi-Agent

### 基于多智能体协作的跨仓库级联代码自动化修复系统

#### 核心痛点解决
* **消除人工检索成本**：利用 Graph RAG 技术精准定位受影响的跨仓库代码块。
* **解决长链推理难题**：Planner Agent 生成跨越多个依赖层级的修复策略。
* **自动化验证闭环**：通过 Reviewer Agent 与单元测试的 Reflection 机制，确保修复 PR 100% 可用。

#### 核心技术栈
* **多智能体编排**：基于长链推理 (Long-chain Reasoning) 的四角色协作。
* **自我反思机制 (Reflection)**：Reviewer 发现错误后反馈给 Coder 进行多轮迭代修正。。

#### 快速开始
1. 配置 `config.yaml`。
2. 运行 `python run_workflow.py` 启动模拟修复流程。
