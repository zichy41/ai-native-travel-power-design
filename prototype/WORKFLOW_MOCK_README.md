# Workflow Prototype V2

## 当前内容

`workflow_orchestrator_mock.py` 是一个确定性的流程演示，不调用大模型。

它展示：

- 如何读取结构化证据；
- 如何为假设设置证据门槛；
- 如何阻止只有合成用户支持的功能进入核心定义；
- 如何读取候选方案评分；
- 如何生成需要人工裁决的报告。

运行：

```bash
python prototype/workflow_orchestrator_mock.py
```

## 为什么先做 Mock

在接入大模型之前，先固定：

- 输入对象；
- 输出 Schema；
- 决策门槛；
- 失败条件；
- 人工裁决点。

否则多 Agent 很容易变成“多个模型轮流写文章”，没有稳定产品流程。

## 后续替换

下一里程碑将把以下函数替换为实际模型调用：

- Research Scout
- Insight Synthesizer
- Devil's Advocate
- Engineering Reviewer
- Decision Auditor

但证据门槛与最终人工决策不交给模型。
