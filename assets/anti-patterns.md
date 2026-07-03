# Prompting Anti-Patterns & Failure Modes

This document details common prompt engineering failures and how to correct them.

---

## 1. Conversational Preambles & Filler
- **Anti-Pattern**:
  `"Sure, I can write that script for you! Let me think... Okay, here is the script."`
- **Why it fails**: Wastes output tokens, increases latency, and makes programmatic parsing of the output difficult or impossible.
- **Correction**: Define a strict output format (e.g., JSON only) and instruct the agent: `"Begin your response directly with the output, skipping any conversational preambles."`

---

## 2. Dynamic Variables in Caching Sections
- **Anti-Pattern**:
  ```markdown
  # SYSTEM INSTRUCTIONS
  Current Time: {{timestamp}}
  Active Folder: {{cwd}}
  ...
  ```
- **Why it fails**: Placing dynamic variables at the beginning of the prompt invalidates the LLM prefix cache on every single turn, increasing input token costs by up to 90%.
- **Correction**: Move all dynamic variables (timestamps, file trees, user queries) to a designated `CURRENT STATE` section at the very end of the prompt.

---

## 3. Lack of Exit Gating & Checklist Tracking
- **Anti-Pattern**:
  `"Work on the files until you are done."`
- **Why it fails**: The agent may terminate prematurely when encountering a minor error or return a half-finished result if a tool output is verbose.
- **Correction**: Enforce a Plan-and-Execute workflow with a checklist file (`task.md`) and a `Stop` hook that blocks exit unless all checklist items are marked complete.

---

## 4. Unconstrained Blast Radius
- **Anti-Pattern**:
  `"You have access to a terminal command execution tool to run tests."`
- **Why it fails**: The agent can run arbitrary destructive commands (`rm -rf /` or deleting cloud databases) if a prompt injection is present.
- **Correction**: Define strict `PreToolUse` hook validations that block command execution outside the workspace directory or filter out dangerous command flags.

---

## 5. Overly Verbose Compaction (Passive Summarization)
- **Anti-Pattern**:
  `"First I did X, then Y, then Z..."`
- **Why it fails**: Passive summaries retain noise and conversational flow, failing to keep context size down while losing sight of active constraints.
- **Correction**: Force a "Directive Compression" structure containing active target files, verified facts, and the remaining checklist.
