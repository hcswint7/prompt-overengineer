# Context Engineering & Active Context Compression

This reference guide details context window budgeting, prompt caching, and active context compression strategies.

---

## 1. Prompt Caching Structure
To maximize LLM prefix cache hits (reducing input cost by up to 90% and improving response latency), prompts must order content from most stable to most volatile:

```
┌────────────────────────────────────────────────────────┐
│ 1. System Prompt (Highest stability, rarely changes)  │
├────────────────────────────────────────────────────────┤
│ 2. Tool Declarations (Highly stable schemas)           │
├────────────────────────────────────────────────────────┤
│ 3. References & Guidelines (Static files, JIT-loaded)  │
├────────────────────────────────────────────────────────┤
│ 4. Few-Shot Examples (Static example templates)        │
├────────────────────────────────────────────────────────┤
│ 5. Session History (Volatile, appends over time)       │
├────────────────────────────────────────────────────────┤
│ 6. Current User Turn (Most volatile, changes every run)│
└────────────────────────────────────────────────────────┘
```

### Cache Rules:
- **No dynamic variables in early blocks**: Avoid injecting timestamps, working directory paths, or user IDs into the System Prompt or Tool section.
- **Consistent Order**: Never reorder tool definitions or system blocks between turns.

---

## 2. JIT Context Loading
- **Budget**: Keep the main system prompt under 500 lines.
- **JIT Trigger**: Use trigger-based file reads. Instruct the agent to read `/references/` or `/assets/` only when a specific sub-task is encountered, rather than dumping all documentation into the context window at start.

---

## 3. Active Context Compression (ACC)
As conversational context grows, the agent must perform an autonomous compression cycle to discard redundant data while preserving necessary constraints.

### The ACC Lifecycle
- **Trigger**: Execute compression every 10–12 tool calls or when context usage exceeds 50% of the window.
- **Hook Gating**:
  - `PreCompact`: Write a backup of critical constraints and intermediate variables.
  - `PostCompact`: Verify that the compressed context includes the active checklist and core rules.

### Directive Compression vs. Passive Summarization
- **Passive Summarization (Inefficient, ~6% savings)**: "First I listed the directory, then I found main.py, then I run a command that failed, and then I fixed it..."
- **Directive Compression (Efficient, ~22.7% savings)**:
  ```markdown
  ### Active Context State
  - **Focus Phase**: IMPLEMENTATION
  - **Target File**: `main.py`
  - **Verified Facts**: Database connection succeeds; user authentication is handled via API key.
  - **Current Task List**:
    - [x] Configure connection pools
    - [/] Implement token refresh handler
    - [ ] Add unit tests
  - **Discarded data**: CLI outputs from git commit and npm build runs.
  ```

---

## 4. MCP Context Bloat Mitigation
- **Schema Compression**: If MCP tool descriptions contain verbose prose, compress them to raw parameter schemas.
- **CLI-as-MCP Pattern**: For tools used rarely, invoke them via standard CLI commands rather than mounting a heavy MCP server.
