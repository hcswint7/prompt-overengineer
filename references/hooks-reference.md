# Hooks Lifecycle & Event Gating

This reference details the full lifecycle hooks that can be configured to intercept, validate, and control agent execution.

---

## 1. Lifecycle Events List

| Lifecycle Event | Execution Point | Primary Purpose |
|---|---|---|
| `SessionStart` | Agent starts up | Load configurations, verify workspace status. |
| `Setup` | Environment initialization | Setup tool environments, test paths. |
| `UserPromptSubmit` | User sends input | Scan for prompt injection, validate format. |
| `UserPromptExpansion` | Agent expands input | Fetch relevant documents or file structures. |
| `PreToolUse` | Right before tool runs | Validate arguments, block unsafe commands. |
| `PostToolUse` | Tool finishes successfully | Auto-format edits, trigger test runner. |
| `PostToolUseFailure` | Tool exits with error | Parse compiler errors, suggest fixes. |
| `PostToolBatch` | Group of tools completes | Sync file tree status, run check-ins. |
| `PermissionRequest` | Tool needs permission | Check allowlist, prompt user if required. |
| `SubagentStart` | Dispatching sub-agent | Validate output contract schema before run. |
| `SubagentStop` | Sub-agent returns | Parse response and check contract adherence. |
| `PreCompact` | Prior to context compaction| Create backup of checklist and constraints. |
| `PostCompact` | After context compaction | Verify that no active constraints were deleted. |
| `Stop` | Agent attempts to exit | Verify checklist completion and test passes. |

---

## 2. Hook Exit Codes

Hook handlers must return standardized exit codes to control agent behavior:
- **`0` (Allow/Proceed)**: Validation passed. The agent proceeds with the planned operation.
- **`2` (Intercept & Modify)**: The handler blocks the immediate operation and either prompts the user, or dynamically rewrites the arguments (e.g., correcting an absolute path to a workspace-relative path).
- **`Other` (Error/Abort)**: Gating failed. The task is aborted or returned with an explicit error trace.

---

## 3. Core Hook Implementations

### PreToolUse (Safety & Blast Radius Guard)
- **Rules**: Validate that any path passed to file tools resides inside the authorized workspace. Block commands containing destructive keywords (`rm -rf /`, `gcloud projects delete`) unless verified.
- **Speculative Fast-Path**: If the tool is read-only (e.g., `list_dir`), return exit code `0` automatically.

### PostToolUse (Quality & Syntax Guard)
- **Rules**: After editing any file, automatically trigger linting and test commands (e.g., `npm run lint` or `pytest`). If tests fail, return the error traceback to the agent's observation log.

### Stop (Completion & Delivery Guard)
- **Rules**: Parse the current workspace `task.md`. If there are any incomplete tasks (`[ ]` or `[/]`), or if tests are failing, block the exit and force the agent to resolve the remaining items.
