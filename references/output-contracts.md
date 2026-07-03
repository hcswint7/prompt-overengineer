# Output Contracts & Function Calling

This reference guide details structured output design, schema enforcement, and tool execution boundaries.

---

## 1. Structured Output Contracts
Using structured JSON schemas guarantees that agent outputs can be programmatically parsed and piped into other services.

### Sub-Agent Output Schema (Standard 6-Field Contract)
All sub-agents dispatched in a fan-out workflow must return their findings in this exact JSON structure:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "domain": {
      "type": "string",
      "description": "The specific domain name assigned to this agent."
    },
    "key_findings": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Core factual findings with citations/paths."
    },
    "actionable_directives": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Specific implementation instructions derived from the findings."
    },
    "template_candidates": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Code templates or markdown snippets."
    },
    "confidence": {
      "type": "string",
      "enum": ["high", "medium", "low"],
      "description": "Confidence level in the findings."
    },
    "gaps": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Any unresolved issues or missing context."
    }
  },
  "required": ["domain", "key_findings", "actionable_directives", "template_candidates", "confidence", "gaps"]
}
```

---

## 2. Structured Outputs vs. Prose
- **Use Structured Output (JSON)**: For automated pipelines, API integrations, multi-agent messages, scoring scripts, and routing decisions.
- **Use Freeform Prose (Markdown)**: For user-facing explanations, design reviews, interactive chat, and general Q&A.

---

## 3. Tool Classification & Speculative Execution
To optimize agent latency, tools should be categorized into two categories:

### Speculative (Read-Safe) Tools
These tools do not modify the environment or codebase. The agent can trigger these tools speculatively in parallel.
- `list_dir`, `grep_search`, `view_file`, `list_permissions`
- `read_resource`, `list_resources`
- `search_web`, `read_url_content`

### Write-Guarded Tools
These tools modify state, write files, or execute commands. They must run sequentially and require strict confirmation or hook gating.
- `write_to_file`, `replace_file_content`, `multi_replace_file_content`
- `run_command` (especially containing write flags)
- `call_mcp_tool` (if the tool has mutating side-effects)
