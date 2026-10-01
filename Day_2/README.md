# Day 2 — Reasoning and Acting

This project compares Direct Prompting, Chain-of-Thought (CoT), and ReAct on a campus technical-event scenario.

## Files
- direct_prompt.py
- cot_compare.py
- self_consistency.py
- react_agent.py
- tools.py
- config.py
- analysis.md
- screenshots/

## Setup
Use the existing Day 1 virtual environment if required by your course. Do not create another virtual environment.

```powershell
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set the model. For Ollama, start Ollama and make sure the model is available.

Run:

```powershell
python direct_prompt.py
python cot_compare.py
python self_consistency.py
python react_agent.py
```

After each successful run, take terminal screenshots and save them in `screenshots/`.

Required screenshots:
- direct_prompt.png
- cot_compare.png
- self_consistency.png
- react_agent.png
