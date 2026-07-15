# Prototype

## 1. Deterministic Workflow Mock

```bash
python prototype/workflow_orchestrator_mock.py
```

它不调用 LLM，而是演示证据门槛、假设审计、候选方案排序和人类决策节点。

## 2. Static Dashboard

直接用浏览器打开：

```text
prototype/dashboard/index.html
```

它用于展示项目流程和当前证据，不代表真实在线多 Agent 系统。

## 3. 下一步

入围后可将每个角色替换成安克内部 AI 工具或允许的大模型调用，并保留相同 JSON Schema 和审计日志。
