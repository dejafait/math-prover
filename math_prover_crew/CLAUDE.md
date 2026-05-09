# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
crewai install        # Install dependencies (uses uv under the hood)
crewai run            # Run the crew
crewai test -n 3 -m gpt-4o-mini   # Evaluate over N iterations
crewai replay -t <task_id>         # Replay from a specific task
crewai reset-memories -a           # Clear all agent memories
crewai log-tasks-outputs           # Show latest task outputs
```

Always use `uv add <package>` to add dependencies, never `pip install`.

## Architecture

A single sequential CrewAI crew for Riemann Hypothesis exploration. Five agents run in order, each writing its output to a numbered markdown file:

| # | Agent | Task | Output file |
|---|-------|------|-------------|
| 1 | `researcher` | Survey current state of RH research | `report_task1_research.md` |
| 2 | `conjecturer` | Generate novel ideas and connections | `report_task2_conjecture.md` |
| 3 | `tester` | Deep-explore each idea to extremes | `report_task3_testing.md` |
| 4 | `critic` | Find every logical gap and fatal flaw | `report_task4_critic.md` |
| 5 | `reporting_analyst` | Compile everything into a final report | `report_task5_reporting.md` |

Each agent receives the accumulated outputs of all prior tasks as context (sequential process).

## Key files

- `src/math_prover_crew/config/agents.yaml` — agent role/goal/backstory
- `src/math_prover_crew/config/tasks.yaml` — task descriptions and expected outputs
- `src/math_prover_crew/crew.py` — wires agents and tasks; LLM selection lives here
- `src/math_prover_crew/main.py` — entry points; `run()` is called by `crewai run`

## Switching LLMs

`crew.py` has two LLM definitions and a toggle:

```python
current_llm = local_llm    # Ollama/gemma4:e4b — free, no API key
# current_llm = pro_llm    # gpt-5.4-pro via OpenAI Responses API — expensive (~$24/run at medium reasoning)
```

The `pro_llm` uses `api="responses"` and `reasoning_effort` (low/medium/high/xhigh), which is required for OpenAI's extended thinking models. Both LLMs are constructed at import time regardless of which is active.

Observed costs (full 5-agent run):

| Model | Reasoning effort | Cost |
|-------|-----------------|------|
| gpt-5.4 | low | ~$0.94 |
| gpt-5.4 | xhigh | ~$0.93 |
| gpt-5.4-pro | medium | ~$24.04 |

## Template variables

Tasks interpolate `{topic}` and `{current_year}` from the `inputs` dict passed at kickoff. Both are set in `main.py:run()`. The `tasks.yaml` currently hardcodes "2026" in one description — if updating that file, use `{current_year}` instead.

## CrewAI reference

`AGENTS.md` in the project root is the authoritative CrewAI API reference (auto-generated). **Before writing or modifying any CrewAI code**, follow the mandatory research steps at the top of that file: check the installed version, fetch the live docs for the relevant feature, and cross-check against the patterns listed there. Live docs win over training data.
