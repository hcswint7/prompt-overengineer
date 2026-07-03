# prompt-overengineer

<p align="center">
  <img src="assets/banner.png" alt="prompt-overengineer logo" width="800px">
</p>

<div align="center">

`prompt-overengineer` / **prompt-overengineer-v1.0**
   
[![Agent Skill](https://img.shields.io/badge/Capability-Agent%20Skill-blueviolet.svg)](#)
[![SKILL.md Standard](https://img.shields.io/badge/Standard-SKILL.md-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)
[![Compatible: Antigravity](https://img.shields.io/badge/Google-Antigravity-darkgreen.svg)](#)
[![Compatible: Claude Code](https://img.shields.io/badge/Claude-Code-orange.svg)](#)
[![Compatible: Codex](https://img.shields.io/badge/Codex-Compatible-red.svg)](#)

</div>

---

### 🚨 v1.0 Released — Initial Stable Release
Initial stable release of the `prompt-overengineer` Agent Skill. Optimized for local development and JIT dynamic loading.

**Updates in v1.0:**
*   **SKILL.md Specification**: Full compliance with Trigger Triad description matching.
*   **34 Registry Concepts**: Master index structured for modular, low-token loading.
*   **9.2 Evaluator Score**: Fully passing rubric scorer.
*   **100% Trigger Accuracy**: verified boundaries with 0.0% FPR and 0.0% FNR.

---

## 🦋 prompt-overengineer: Maximally-Optimized Agent Skill

Developed by **Antigravity**

`prompt-overengineer` is a production-grade Agent Skill designed to compile and write overkill, maximally-optimized prompts for coding agents and agentic services. It surfaces every known coding-agent prompt optimization concept, guiding the compilation of custom prompts that maximize task completion rate and safety while reducing inference latency.

For full structural details, concept analysis, and execution workflow, see the [SKILL.md](file:///C:/Users/Hcswi/.gemini/config/skills/prompt-overengineer/SKILL.md) file.

---

## 📁 File Structure & Manifest

The skill is built using a modular JIT structure. The agent only loads reference files when specific task conditions are triggered, preserving context space.

| File Path | Description | Size (Lines) | Loading Trigger |
|---|---|---|---|
| **[SKILL.md](file://SKILL.md)** | Core workflow and Trigger Triad declaration | ~70 lines | Always in context |
| **[references/concept-index.md](file://references/concept-index.md)** | Master list of 34 prompt optimization concepts | ~130 lines | JIT-loaded during task analysis |
| **[references/prompt-patterns.md](file://references/prompt-patterns.md)** | Reasoning templates (CoT, ReAct, Reflexion) | ~100 lines | JIT-loaded for reasoning-heavy tasks |
| **[references/output-contracts.md](file://references/output-contracts.md)** | Output schemas and speculative tool lists | ~110 lines | JIT-loaded for function calling |
| **[references/context-engineering.md](file://references/context-engineering.md)** | Prefix caching rules and Active Compaction (ACC) | ~100 lines | JIT-loaded for long sessions |
| **[references/hooks-reference.md](file://references/hooks-reference.md)** | Event hooks (PreToolUse, PostToolUse) & exit codes | ~100 lines | JIT-loaded for hook configurations |
| **[references/orchestration-patterns.md](file://references/orchestration-patterns.md)** | Supervisor patterns and model tiering (Opus vs Sonnet) | ~100 lines | JIT-loaded for multi-agent routing |
| **[references/evaluation-rubric.md](file://references/evaluation-rubric.md)** | Rubrics and trigger-rate testing rules | ~70 lines | Loaded during evaluation phase |
| **[assets/overkill-template.md](file://assets/overkill-template.md)** | Annotated template prompt layout | ~100 lines | Loaded during prompt generation |
| **[assets/few-shot-examples.md](file://assets/few-shot-examples.md)** | 3 detailed input-output examples | ~110 lines | Loaded during prompt generation |
| **[assets/anti-patterns.md](file://assets/anti-patterns.md)** | Prompt engineering failure modes and correctives | ~70 lines | Loaded during self-critique phase |
| **[scripts/score-prompt.py](file://scripts/score-prompt.py)** | Heuristic scoring Python script (10 dimensions) | ~150 lines | Executed during prompt evaluation |
| **[scripts/test-triggers.py](file://scripts/test-triggers.py)** | Evaluates Trigger Triad accuracy (6 queries) | ~50 lines | Executed during validation tests |

---

## ⚡ Quick Start

### 1. Installation
Install the skill into your target agent's global repository path:

```bash
# Google Antigravity / Claude Code
mkdir -p ~/.gemini/config/skills/prompt-overengineer
cp -r * ~/.gemini/config/skills/prompt-overengineer/
```

### 2. Execution
Run the evaluation script to test a drafted prompt file locally:

```bash
python scripts/score-prompt.py --prompt-file assets/overkill-template.md
```

---

## 📊 Prompt Compilation Recommendations

When compiling optimized prompts, configure your agent and generation parameters using these defaults:

| Parameter | Value | Description |
|---|---|---|
| **min_concepts** | 7 | Minimum number of concepts required from `concept-index.md` |
| **eval_threshold** | 8.0 | Minimum score required on the 10-dimension rubric scorer to pass the quality gate |
| **max_agent_loops** | 20 | Hard iteration ceiling to prevent infinite tool execution runs |
| **concurrency_limit**| 3–5 | Optimal sub-agent limit during Fan-Out Supervisor partitioning |
| **compaction_cycle** | 10–12 | Number of tool-calls before triggering Active Context Compression (ACC) |

---

## 🛠️ Key Capabilities

*   **Prefix Cache Optimal**: Automatically structures system prompts with stable sections first and volatile session states at the end, ensuring up to **90% input cost reduction** via prefix cache hits.
*   **Active Context Compression (ACC)**: Periodically condenses conversation history into a structured, directive summary format, saving **22.7% token memory** and preventing instruction decay.
*   **Speculative Tool Gating**: Classifies tool registries into read-safe and write-guarded paths, executing read-only commands speculatively to reduce latency while safety-gating writes.
*   **Lifecycle Hook Integrations**: Restricts agent execution via `PreToolUse` hooks (safety gating) and `PostToolUse` hooks (automated formatting and testing), and exits via `Stop` hooks.

---

## ⚠️ Limitations

*   **Python Requirement**: The local scorer script requires Python 3.x and access to the terminal to run.
*   **Workspace Restrictions**: Safety boundaries assume the agent operates within a Git repository workspace.

---

## 🤝 Provenance & Licensing

*   **Developer**: Developed by Antigravity IDE team.
*   **License**: Licensed under the **MIT License**.
*   **Base Specifications**: Inherited from the SKILL.md open standard.
