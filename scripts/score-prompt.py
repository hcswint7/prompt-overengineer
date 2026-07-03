#!/usr/bin/env python3
import os
import sys
import argparse
import json

def score_prompt(prompt_content):
    breakdown = {}
    suggestions = []

    # 1. Reasoning Pattern
    reasoning_keywords = ["reasoning", "react", "cot", "chain-of-thought", "plan-and-execute", "tree-of-thought", "reflexion"]
    reasoning_hits = sum(1 for kw in reasoning_keywords if kw in prompt_content.lower())
    breakdown["Reasoning Pattern"] = int(min(10, 2 + reasoning_hits * 2))
    if breakdown["Reasoning Pattern"] < 8:
        suggestions.append("Introduce explicit reasoning protocols such as ReAct or Chain-of-Thought instructions.")

    # 2. Output Contract
    contract_keywords = ["json", "schema", "pydantic", "contract", "format"]
    contract_hits = sum(1 for kw in contract_keywords if kw in prompt_content.lower())
    breakdown["Output Contract"] = int(min(10, 2 + contract_hits * 2))
    if breakdown["Output Contract"] < 8:
        suggestions.append("Define a strict JSON output contract schema to ensure parseable responses.")

    # 3. Token Efficiency & Caching
    caching_keywords = ["cache", "caching", "stable", "volatile", "budget", "token"]
    caching_hits = sum(1 for kw in caching_keywords if kw in prompt_content.lower())
    breakdown["Token Efficiency"] = int(min(10, 2 + caching_hits * 2))
    if breakdown["Token Efficiency"] < 8:
        suggestions.append("Add instructions for prefix caching, splitting stable system rules from volatile session states.")

    # 4. Source Citation
    citation_keywords = ["cite", "citation", "source", "line number", "reference"]
    citation_hits = sum(1 for kw in citation_keywords if kw in prompt_content.lower())
    breakdown["Source Citation"] = int(min(10, 2 + citation_hits * 2))
    if breakdown["Source Citation"] < 8:
        suggestions.append("Require the agent to cite source files or specific lines when modifying code.")

    # 5. Confidence Declaration
    confidence_keywords = ["confidence", "high/medium/low", "certainty", "declare"]
    confidence_hits = sum(1 for kw in confidence_keywords if kw in prompt_content.lower())
    breakdown["Confidence Declaration"] = int(min(10, 2 + confidence_hits * 2))
    if breakdown["Confidence Declaration"] < 8:
        suggestions.append("Enforce a confidence declaration (high, medium, low) in final outputs.")

    # 6. Action Specificity
    action_keywords = ["restrict", "permit", "allow", "forbid", "command", "boundary", "sandbox"]
    action_hits = sum(1 for kw in action_keywords if kw in prompt_content.lower())
    breakdown["Action Specificity"] = int(min(10, 2 + action_hits * 2))
    if breakdown["Action Specificity"] < 8:
        suggestions.append("Clearly itemize allowed tools, restricted operations, and sandbox boundaries.")

    # 7. Quality Gate (linting/testing)
    gate_keywords = ["linter", "lint", "test", "pytest", "unit test", "verify", "run"]
    gate_hits = sum(1 for kw in gate_keywords if kw in prompt_content.lower())
    breakdown["Quality Gate"] = int(min(10, 2 + gate_hits * 2))
    if breakdown["Quality Gate"] < 8:
        suggestions.append("Instruct the agent to run code linters or test commands after editing code.")

    # 8. Concept Coverage
    concept_keywords = ["cot", "react", "tot", "got", "rewoo", "reflexion", "lats", "dspy", "ape", "textgrad", "few-shot", "memory", "rag", "hooks", "compression"]
    concept_hits = sum(1 for kw in concept_keywords if kw in prompt_content.lower())
    breakdown["Concept Coverage"] = int(min(10, 2 + concept_hits * 1.5))
    if breakdown["Concept Coverage"] < 8:
        suggestions.append("Increase coverage of advanced agentic concepts (e.g. hooks, RAG, compression).")

    # 9. Synthesis Instruction
    synthesis_keywords = ["synthesis", "summary", "summarize", "conclusion", "brief"]
    synthesis_hits = sum(1 for kw in synthesis_keywords if kw in prompt_content.lower())
    breakdown["Synthesis Instruction"] = int(min(10, 2 + synthesis_hits * 2))
    if breakdown["Synthesis Instruction"] < 8:
        suggestions.append("Ensure the agent outputs a structured synthesis or summary of modifications.")

    # 10. Trigger Rate Boundaries
    trigger_keywords = ["trigger", "condition", "vocabulary", "exclude", "when to use"]
    trigger_hits = sum(1 for kw in trigger_keywords if kw in prompt_content.lower())
    breakdown["Trigger Rate Boundaries"] = int(min(10, 2 + trigger_hits * 2))
    if breakdown["Trigger Rate Boundaries"] < 8:
        suggestions.append("Provide clear guidelines on when this skill/prompt should be triggered and when to exclude it.")

    average_score = round(sum(breakdown.values()) / len(breakdown), 2)
    passed = average_score >= 8.0

    return {
        "score": average_score,
        "passed": passed,
        "breakdown": breakdown,
        "suggestions": suggestions
    }

def main():
    parser = argparse.ArgumentParser(description="Evaluate prompt files against the agent prompt engineering rubric.")
    parser.add_argument("--prompt-file", required=True, help="Path to the prompt file to score.")
    args = parser.parse_args()

    if not os.path.exists(args.prompt_file):
        print(json.dumps({"error": f"File not found: {args.prompt_file}"}, indent=2))
        sys.exit(1)

    try:
        with open(args.prompt_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(json.dumps({"error": f"Failed to read file: {str(e)}"}, indent=2))
        sys.exit(1)

    results = score_prompt(content)
    print(json.dumps(results, indent=2))

    if not results["passed"]:
        sys.exit(2)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
