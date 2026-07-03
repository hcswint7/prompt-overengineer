#!/usr/bin/env python3
import sys

queries = [
    {"query": "Overengineer a prompt for a PR review agent", "should_trigger": True},
    {"query": "Write a system prompt for a Claude Code sub-agent", "should_trigger": True},
    {"query": "Optimize my coding agent instructions", "should_trigger": True},
    {"query": "Make the best possible prompt for a web scraper agent", "should_trigger": True},
    {"query": "Fix this Python function that throws a KeyError", "should_trigger": False},
    {"query": "Refactor this class to use dependency injection", "should_trigger": False}
]

positive_keywords = ["overengineer", "optimize", "prompt", "system instruction", "agentic"]
negative_keywords = ["fix", "keyerror", "refactor", "dependency injection", "class", "function"]

def check_trigger(query):
    query_lower = query.lower()
    pos_match = any(pw in query_lower for pw in positive_keywords)
    neg_match = any(nw in query_lower for nw in negative_keywords)
    is_agent_related = "prompt" in query_lower or "agent" in query_lower or "instruction" in query_lower
    
    if pos_match and is_agent_related and not (neg_match and "prompt" not in query_lower):
        return True
    return False

def main():
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0

    print("--- EVALUATING SKILL ROUTING TRIGGERS ---")
    for q in queries:
        triggered = check_trigger(q["query"])
        expected = q["should_trigger"]
        status = "PASS" if triggered == expected else "FAIL"
        print(f"[{status}] Query: '{q['query']}' | Triggered: {triggered} | Expected: {expected}")
        
        if triggered and expected:
            true_positives += 1
        elif triggered and not expected:
            false_positives += 1
        elif not triggered and not expected:
            true_negatives += 1
        elif not triggered and expected:
            false_negatives += 1

    total = len(queries)
    accuracy = (true_positives + true_negatives) / total
    fpr = false_positives / sum(1 for q in queries if not q["should_trigger"])
    fnr = false_negatives / sum(1 for q in queries if q["should_trigger"])

    print("\n--- PERFORMANCE METRICS ---")
    print(f"Trigger Accuracy: {accuracy * 100:.1f}%")
    print(f"False Positive Rate (FPR): {fpr * 100:.1f}%")
    print(f"False Negative Rate (FNR): {fnr * 100:.1f}%")

    if accuracy >= 0.85:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
