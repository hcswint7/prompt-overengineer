# Evaluation Rubric & Quality Gates

This reference guide outlines the criteria and procedures for evaluating prompt quality using automated scoring and human audit.

---

## 1. Rubric Dimensions
Every generated prompt is scored on ten dimensions, each rated from 1 to 10:

1. **Reasoning Pattern**: Does the prompt instruct a structured reasoning style (e.g., CoT, ReAct)?
2. **Output Contract**: Is a strict schema (JSON/Pydantic) defined and enforced?
3. **Token Efficiency**: Does the prompt structure minimize context footprint and support caching?
4. **Source Citation**: Are there rules requiring the agent to cite original files or lines?
5. **Confidence Declaration**: Does the prompt require declaring confidence levels (high/medium/low)?
6. **Action Specificity**: Are the allowed tools and forbidden commands clearly itemized?
7. **Quality Gate Inclusion**: Are there instructions to run linters/tests post-execution?
8. **Concept Coverage**: Does the prompt include 7+ valid optimization concepts?
9. **Synthesis Instruction**: Are rules provided for summarizing findings and actions concisely?
10. **Trigger Rate Boundaries**: Are positive and negative triggers clearly defined?

---

## 2. Evaluation Scorer Script
The prompt scorer runs heuristic and text-matching checks on the prompt file.

### How to Run:
```powershell
python scripts/score-prompt.py --prompt-file <path>
```

### Passing Threshold:
- A minimum average score of **8.0 / 10.0** is required to pass the quality gate.
- Any prompt scoring below 8.0 must be revised according to the suggestions in the JSON output.

---

## 3. Trigger-Rate testing
To prevent prompt activation bloat (skills triggering when they shouldn't, or failing to trigger when they should):
- **Benchmark**: Maintain a set of 20 sample user queries.
  - **12 Positive Queries (60%)**: Queries that *should* activate the prompt.
  - **8 Negative Queries (40%)**: Queries that *should not* activate the prompt.
- **Goal**: Maintain a **≥85%** accuracy rate (correct classifications).
- **Metric**:
  $$\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{20}$$
