# Prompt Patterns & Reasoning Templates

This reference guide provides templates and instructions for structuring reasoning patterns within optimized prompts.

---

## 1. Chain-of-Thought (CoT)
Instruct the model to decompose the task into logical steps before generating the final answer.
```markdown
### Reasoning Protocol
For any task, you must formulate your response using the following steps:
1. **Analysis**: Extract the parameters, limitations, and expectations of the user request.
2. **Intermediate Steps**: Deduce step-by-step logic, stating assumptions and checking intermediate results.
3. **Synthesis**: Construct the final answer based on the deduced facts.
```

---

## 2. ReAct (Reason & Action)
Interleave thoughts and actions. This pattern is ideal for tool-based agents.
```markdown
### Agent Execution Loop
For each step, output your response in this exact format:
- **Thought**: Describe what you need to do next, why, and which tool to use.
- **Action**: Call the tool with the computed arguments.
- **Observation**: Read the result of the tool execution.
(Repeat until the objective is reached, then output the final summary.)
```

---

## 3. Plan-and-Execute
Decouple planning from execution. The agent first writes a full recipe, then works through it.
```markdown
### Execution Plan
1. **Plan**: Write a bulleted list of tasks required to achieve the goal.
2. **Execute**: Work through the tasks one-by-one. Update a checklist file (`task.md`) after each action.
3. **Verify**: Run verification scripts or checks to confirm completion.
```

---

## 4. Reflexion / Self-Critique
Force the model to review and correct its own work before presenting it to the user.
```markdown
### Verification and Critique
Before declaring a task complete, perform a self-reflection pass:
- **Self-Critique**: Inspect the code edits or output text against all user constraints.
- **Error Identification**: Identify any edge cases, off-by-one errors, or stylistic violations.
- **Revision Plan**: If any issues are found, list the corrective edits and execute them immediately.
```

---

## 5. Tree-of-Thought (ToT) / Branching
For complex, multi-variable decisions, instruct the model to explore multiple candidate plans.
```markdown
### Alternative Analysis (Branching)
1. **Identify Candidates**: Formulate three different approaches (A, B, and C) to solve the problem.
2. **Evaluate**: Score each approach from 1 to 5 based on performance, complexity, and safety.
3. **Select**: Execute the approach with the highest score.
```

---

## 6. Meta-Prompting (Prompt Generation)
When prompting the model to write a prompt, use structured variable placeholders and boundary rules.
```markdown
### System Instruction Generator Rule
When generating a system prompt, always define:
- Role & Persona (who the agent is)
- Tool Permissions (what the agent can/cannot execute)
- Core Logic (the step-by-step reasoning pattern)
- Output Schema (the exact response format)
```
