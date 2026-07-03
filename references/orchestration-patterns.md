# Multi-Agent Orchestration & Model Tiering

This reference guide provides orchestration patterns, model configurations, and concurrency rules for multi-agent workflows.

---

## 1. Fan-Out Supervisor Pattern

The Supervisor pattern partitions a complex project into distinct, non-overlapping sub-tasks, dispatches them to parallel agents, and synthesizes the outputs.

```
                  ┌──────────────────────┐
                  │      Supervisor      │
                  └──────────┬───────────┘
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
     ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
     │ Sub-Agent A │  │ Sub-Agent B │  │ Sub-Agent C │
     └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
            └────────────────┼────────────────┘
                             ▼
                  ┌──────────────────────┐
                  │      Synthesis       │
                  └──────────────────────┘
```

### Steps:
1. **Partition**: Split the goal into independent domains.
2. **Dispatch**: Spawn sub-agents with strict domain boundaries and task descriptions.
3. **Contract**: Enforce that each agent returns data conforming to the standard JSON Output Contract.
4. **Synthesis**: Aggregate the outputs and resolve dependencies.

---

## 2. Model Tiering Matrix
Match the task requirements to the appropriate model strengths to balance latency, cost, and capability.

| Model Tier | Strengths | Target Tasks |
|---|---|---|
| **Haiku / Flash** | Ultra-low latency, cheap, large context. | - Web searches & document retrieval.<br>- Regex file search & listing.<br>- Simple syntax corrections. |
| **Sonnet** | Strong programming ability, high reasoning. | - Code modifications & refills.<br>- Writing unit tests.<br>- Refactoring components. |
| **Opus / Pro** | Exceptional architectural reasoning & synthesis.| - High-level planning & task partitioning.<br>- Multi-agent dispatch coordination.<br>- Synthesis of domain research. |

---

## 3. Concurrency & Iteration Discipline
- **Sweet Spot**: Maintain between **3 and 5** concurrent sub-agent executions. Exceeding 5 triggers API rate limits and increases token contention.
- **Iteration Ceiling**: Set a hard maximum tool-call limit (e.g., 20) for any individual agent. If reached, the agent must halt execution, construct a fallback synthesis report of what was achieved, and return control to the supervisor.

---

## 4. Semantic Routing
Forward incoming user requests to specialized prompts or agent roles based on embedding-similarity or keyword routing:
- **UI/Layout tasks** -> Route to a layout specialist agent with css/canvas tool access.
- **Database/Data tasks** -> Route to a SQL/BigQuery specialist agent with database credentials.
- **Security/Audit tasks** -> Route to a read-only sandboxed auditing agent.
