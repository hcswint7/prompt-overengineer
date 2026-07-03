# prompt-overengineer

[![Skill: prompt-overengineer](https://img.shields.io/badge/Skill-prompt--overengineer-blue.svg)](#)
[![Version: v1.0](https://img.shields.io/badge/Version-v1.0-green.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

## What It Does

`prompt-overengineer` is a production-grade Agent Skill that generates overkill, maximally-optimized prompts for coding agents and autonomous workflows. It guides agents through task analysis, JIT reference loading, and strict constraint engineering to assemble prompts that maximize cache hit rates, enforce execution safety, and guarantee structured JSON outputs.

## Compatibility

- Google Antigravity
- Claude Code
- Codex

## Installation

To install this skill, clone or copy the skill folder into your agent's global skills directory:

### Google Antigravity
```bash
cp -r prompt-overengineer/ ~/.gemini/config/skills/
```

### Claude Code
```bash
cp -r prompt-overengineer/ ~/.agent/skills/
```

### Codex
```bash
cp -r prompt-overengineer/ ~/.codex/skills/
```

## Usage

### Example Trigger Query
> "overengineer prompt for a code auditor agent that reads python code and scans for SQL injections"

### What the Output Contains
1. **Persona / Role**: Sets up a focused persona (e.g., `SQLGuard`).
2. **Trigger Conditions**: Explicitly targets specific queries and excludes general code edits.
3. **Security Boundaries**: Gated path permissions and blocked destructive operations.
4. **Structured Output Contract**: A JSON schema ensuring the final summary and list of vulnerabilities can be programmatically parsed.
5. **Citations & Verification**: Enforces referencing exact source files and line numbers.

## File Structure

```
prompt-overengineer/
├── SKILL.md                          # Main skill entry point (YAML metadata + 6-step workflow)
├── references/
│   ├── concept-index.md              # Registry of 34 core prompt optimization concepts
│   ├── prompt-patterns.md            # CoT, ReAct, and Reflexion templates
│   ├── output-contracts.md           # JSON schema definitions and speculative tool rules
│   ├── context-engineering.md        # Prefix caching guidelines and active compression rules
│   ├── hooks-reference.md            # Lifecycle hooks (PreToolUse, PostToolUse) and exit codes
│   ├── orchestration-patterns.md     # Fan-out supervisor patterns and model tiering rules
│   └── evaluation-rubric.md          # 10 rubric dimensions and trigger-rate testing rules
├── assets/
│   ├── overkill-template.md          # Annotated template prompt structure
│   ├── few-shot-examples.md          # 3 detailed input-output optimization examples
│   └── anti-patterns.md              # Documents common prompt engineering failure modes
└── scripts/
    ├── score-prompt.py               # 10-dimension heuristic scorer returning JSON
    └── test-triggers.py              # Automates Trigger Triad accuracy evaluations
```

## Concepts Covered

`CoT` `ToT` `GoT` `ReAct` `Plan-Execute` `ReWOO` `Reflexion` `LATS` `Meta-Prompting` `DSPy` `APE` `TextGrad` `Self-Consistency` `Few-Shot` `Example-Selection` `Output-Contract` `Speculative-Tools` `Token-Budget` `JIT-Loading` `Prefix-Caching` `KV-Cache` `ACC` `Pre-Post-Compact` `Lifecycle-Hooks` `Exit-Codes` `Scope-Boundaries` `Injection-Defense` `RAG` `Agentic-RAG` `Tiered-Memory` `Supervisor` `Semantic-Routing` `Model-Tiering` `Iteration-Ceiling`

## Scoring

Every prompt drafted by the workflow is evaluated against 10 rubric dimensions (each scored 1–10):
1. **Reasoning Pattern**
2. **Output Contract**
3. **Token Efficiency**
4. **Source Citation**
5. **Confidence Declaration**
6. **Action Specificity**
7. **Quality Gate**
8. **Concept Coverage**
9. **Synthesis Instruction**
10. **Trigger Rate Boundaries**

A prompt must score **$\ge$ 8.0 / 10.0** to pass the evaluation gate and be returned to the user.

## Validation Results

| Test Type | Metric Evaluated | Result | Status |
|---|---|---|---|
| **Rubric Scorer** | Template prompt score | **9.2 / 10.0** | **PASSED** (Threshold $\ge 8.0$) |
| **Trigger Routing** | Trigger Triad accuracy (6 queries) | **100% Accuracy** (0.0% FPR, 0.0% FNR) | **PASSED** (Threshold $\ge 85\%$) |

## License

This project is licensed under the MIT License - see the LICENSE file for details.
