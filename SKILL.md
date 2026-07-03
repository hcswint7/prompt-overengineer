---
name: prompt-overengineer
description: |
  Generates overkill, maximally-optimized prompts for coding agents and agentic services.
  Use this skill when you need to optimize system prompts, design custom agentic instructions, configure tool permissions, or construct robust multi-agent orchestration instructions.
  Triggers on requests containing: "overengineer prompt", "optimize agent instructions", "build system prompt", "agentic prompt engineering", "make agentic workflow instructions".
  Exclude when: requests are for general programming, script writing, or unrelated code debugging.
license: Apache-2.0
metadata:
  version: v1
  publisher: custom
---

# Prompt Overengineer

This skill instructs the agent on how to build maximally-optimized, production-grade system prompts for coding agents and agentic workflows. It leverages advanced techniques in context engineering, token discipline, hooks integration, and structured output contracts to design prompts that maximize task completion rate and safety while reducing inference cost.

## Workflow Instructions

When tasked with generating or optimizing an agent prompt, follow these six sequential steps:

### 1. Task Analysis & Requirements Gathering
Analyze the target agent's goals and runtime environment. Identify:
- **Core Objective**: What specific output or action must the agent perform?
- **Agent Architecture**: Is it a single-agent loop or a multi-agent system?
- **Tool Access**: What MCP tools, CLI utilities, or APIs will the agent use?
- **Model Tier**: Which models will execute this prompt (e.g., Haiku/Flash vs Sonnet vs Opus/Pro)?
- **Constraints & Safety**: What directories, commands, or operations must be restricted?

### 2. Just-in-Time (JIT) Context Loading
To keep the active context size lean, do **not** read all reference files upfront. Dynamically view only the reference files matching the task requirements:
- Always read the Master Registry: [references/concept-index.md](file://references/concept-index.md)
- If the agent uses reasoning or planning patterns (e.g., CoT, ReAct): read [references/prompt-patterns.md](file://references/prompt-patterns.md)
- If the agent requires strict JSON or function calling: read [references/output-contracts.md](file://references/output-contracts.md)
- If the prompt is for long sessions or has context limitations: read [references/context-engineering.md](file://references/context-engineering.md)
- If the agent uses lifecycle hooks (e.g., PreToolUse): read [references/hooks-reference.md](file://references/hooks-reference.md)
- If the task uses multi-agent structures: read [references/orchestration-patterns.md](file://references/orchestration-patterns.md)
- Always read the evaluation guidelines: [references/evaluation-rubric.md](file://references/evaluation-rubric.md)

### 3. Concept Selection
Select at least **seven (7)** optimization concepts from [references/concept-index.md](file://references/concept-index.md) that directly benefit the target agent. You must justify your selection (e.g., "Selecting `PREFIX_CACHING` and `TIERED_MEMORY` because...").
- **Mandatory Concepts**: At least one reasoning pattern (e.g., `CoT` or `ReAct`), structured outputs (`OUTPUT_CONTRACT`), context discipline (`TOKEN_BUDGET`), and safety boundaries (`SCOPE_BOUNDARIES`).

### 4. Draft Prompt Synthesis
Draft the optimized prompt by matching the structure of [assets/overkill-template.md](file://assets/overkill-template.md).
- Integrate relevant few-shot examples from [assets/few-shot-examples.md](file://assets/few-shot-examples.md) to ground the model.
- Cross-reference [assets/anti-patterns.md](file://assets/anti-patterns.md) to ensure the draft contains none of the documented prompt failures.
- Organize the sections strictly to optimize prompt caching (stable system instructions first, variable context last).

### 5. Rubric Evaluation & Iterative Refinement
Evaluate your drafted prompt by running the evaluation script:
```powershell
python "${CLAUDE_SKILL_DIR}/scripts/score-prompt.py" --prompt-file <path_to_drafted_prompt>
```
If the prompt scores **below 8.0 out of 10.0**, read the JSON output's suggestions, revise the prompt, and re-run the scorer. Do not output the prompt to the user until it meets or exceeds the 8.0 threshold.

### 6. Deliver Prompt & Walkthrough
Provide the finalized prompt to the user as a markdown code block or file, accompanied by a brief summary explaining:
- The selected optimization concepts.
- The JIT loading references used.
- The evaluation score and how recommendations were addressed.
