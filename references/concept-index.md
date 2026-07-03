# Master Concept Registry

This registry lists the 34 core optimization concepts used to engineer production-grade, overkill prompts for AI agents.

| Canonical Tag | Concept Name | Terse Definition |
|---|---|---|
| `CoT` | Chain-of-Thought | Generating step-by-step reasoning sequences before outputting the final answer. |
| `ToT` | Tree-of-Thought | Exploring multiple reasoning paths in a branching structure to find the optimal solution. |
| `GoT` | Graph-of-Thought | Modeling reasoning as a network of non-linear nodes, allowing cycles and feedback loops. |
| `ReAct` | Reason & Action | Interleaving internal thoughts with tool execution to adapt to environment feedback. |
| `Plan-Execute` | Plan-and-Execute | Generating a multi-step plan first, then systematically executing each step. |
| `ReWOO` | Reason Without Obs. | Planning a sequence of tool calls using variables before executing any of them. |
| `Reflexion` | Self-Critique | Evaluating intermediate outputs against constraints and revising based on self-reflection. |
| `LATS` | Language Agent Search | Combining search trees with LLM evaluations to perform Monte Carlo tree-like searches. |
| `Meta-Prompting` | Meta-Prompting | Constructing prompts that command LLMs to design, optimize, or evaluate other prompts. |
| `DSPy` | DSPy Compiler | Declarative prompt engineering where examples and instructions are optimized via compilation. |
| `APE` | Auto Prompt Eng. | Using an LLM to generate and search over candidate instructions to optimize outcomes. |
| `TextGrad` | Text Gradients | Using LLM critique as "gradients" to backpropagate textual feedback for prompt tuning. |
| `Self-Consistency` | Self-Consistency | Generating multiple independent reasoning paths and taking the majority/consistent vote. |
| `Few-Shot` | Few-Shot Prompting | Providing explicit input-output examples to teach the model formatting and logic. |
| `Example-Selection` | Example Selection | Selecting diverse, edge-case, and failure-mode examples to improve generalizability. |
| `Output-Contract` | Output Contract | Enforcing strict formatting (e.g., JSON Schema/Pydantic) for model outputs. |
| `Speculative-Tools`| Speculative Tools | Running read-safe tools in parallel while waiting for final model generations. |
| `Token-Budget` | Token Budgeting | Capping token consumption in prompts and outputs to control cost and latency. |
| `JIT-Loading` | JIT Context Loading | Reading reference files or documentation only when specific triggers require them. |
| `Prefix-Caching` | Prefix Caching | Structuring prompts with stable segments first to maximize prefix cache hit rates. |
| `KV-Cache` | KV Cache Management | Minimizing context volatility to maintain key-value cache persistence in long runs. |
| `ACC` | Context Compression | Periodically condensing conversation history into a structured, directive summary block. |
| `Pre-Post-Compact` | Pre/Post Compact Hooks | Gating compaction with backup and validation loops to prevent constraint loss. |
| `Lifecycle-Hooks` | Lifecycle Hooks | Defining trigger-action routines for events like PreToolUse, PostToolUse, and Stop. |
| `Exit-Codes` | Lifecycle Exit Codes | Gating tool or execution flow using standard codes (0 to allow, 2 to modify/intercept). |
| `Scope-Boundaries` | Scope Boundaries | Restricting tool execution parameters to a pre-defined path or command sub-domain. |
| `Injection-Defense`| Injection Defense | Hardening input handlers to reject prompts that attempt system escape or instruction override. |
| `RAG` | retrieval RAG | Statically querying database index to append context before prompt evaluation. |
| `Agentic-RAG` | Agentic RAG | Allowing the agent to autonomously generate search queries and retrieve data dynamically. |
| `Tiered-Memory` | Tiered Memory | Segregating state into short-term chat, active task checklists, and long-term storage. |
| `Supervisor` | Fan-Out Supervisor | An orchestrator that partitions tasks, dispatches to agents, and synthesizes results. |
| `Semantic-Routing` | Semantic Routing | Dynamically dispatching prompts to specialized handlers based on task similarity. |
| `Model-Tiering` | Model Tiering | Assigning simple tasks to fast/cheap models and complex logic to powerful models. |
| `Iteration-Ceiling`| Iteration Ceiling | Enforcing a maximum limit on agent loops to prevent infinite tool execution runs. |
