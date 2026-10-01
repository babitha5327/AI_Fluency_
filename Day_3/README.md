#  AI Fluency – Day 3

## Build a ReAct Agent from Scratch, Break It on Purpose, Then Fix It

Day 3 focuses on building a **ReAct agent from scratch in plain Python** without using an agent framework.

The agent uses two tools:

* `calculator`
* `read_webpage`

The activity also demonstrates how an agent can fail and how safety guards can be added to make the agent more reliable.

---

## 🎯 Objective

The main objective of Day 3 is to:

* Build a ReAct agent loop from scratch
* Create a tool registry
* Define JSON tool schemas
* Use a calculator tool
* Read local HTML/web pages
* Implement Reason → Act → Observe
* Deliberately trigger agent failures
* Identify why the failures occur
* Add guards to prevent the failures
* Compare the unguarded and guarded agents

The lab specifically focuses on three failure modes:

1. Repeating tool-call loop
2. Hallucinated/unknown tool call
3. Context overflow and runaway cost

---

## 🛠️ Technologies Used

* Python
* Groq API
* OpenAI-compatible API
* ReAct
* Tool Calling
* JSON
* HTML
* `requests`
* Visual Studio Code
* GitHub

---

## 📂 Project Structure

```text
AI_Fluency_day3/
│
├── AI_Fluency_Day3_Task/
│   │
│   ├── requirements.txt
│   ├── make_big_page.py
│   ├── my_tools.py
│   ├── my_agent.py
│   ├── my_agent_fixed.py
│   │
│   ├── notice.html
│   ├── big.html
│   │
│   └── Output/
│       └── screenshots
│
└── README.md
```

---

# 🔧 Tools Implemented

## 1. Calculator

The calculator safely evaluates arithmetic expressions.

Example:

```text
(12000 + 18000) * 0.9
```

Output:

```text
27000.0
```

The calculator does **not** use Python `eval()`.

Instead, the expression is parsed and only supported arithmetic operations are allowed.

### Supported operations

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Negative numbers

---

## 2. Web Page Reader

The `read_webpage()` tool can read:

* Local HTML files
* Local text files
* HTTP/HTTPS web pages

It removes HTML tags and returns readable text.

It also removes `<script>` and `<style>` content so that unnecessary page content is not passed to the model.

Example:

```text
read_webpage("notice.html")
```

---

# 🔄 ReAct Agent

The agent follows the ReAct cycle:

```text
Reason
  ↓
Act
  ↓
Observe
  ↓
Reason
  ↓
Act
  ↓
Observe
  ↓
Final Answer
```

The agent can decide whether it needs a tool.

For example:

```text
User
↓
"Read notice.html and calculate the total fee"
↓
Agent
↓
read_webpage()
↓
Observation
↓
calculator()
↓
Observation
↓
Final Answer
```

---

# 🧪 Main Test Scenario

The agent works with `notice.html`.

The notice contains:

| Course |     Fee |
| ------ | ------: |
| CS101  | ₹12,000 |
| AI202  | ₹18,000 |
| DS303  | ₹15,000 |

It also specifies:

* Merit scholarship: 10% reduction
* Hostel laboratory charges: ₹4,500

### Example Question

```text
Read notice.html and tell me the total fee for CS101
and AI202 after the merit scholarship.
```

### Calculation

```text
(12,000 + 18,000) × 0.90
= ₹27,000
```

### Sample Agent Trace

```text
step 1:
read_webpage({'url': 'notice.html'})

step 2:
calculator({'expression': '(12000 + 18000) * 0.9'})
→ 27000.0

Final Answer:
The total fee after the 10 percent merit scholarship
is Rs. 27,000.
```

This is the expected ReAct behaviour from the lab.

---

# 💥 Failure Experiments

Day 3 deliberately introduces three failure modes.

## Failure 1 – Repeating Tool-Call Loop

The agent is asked to read a file that does not exist:

```text
Read fees.html and tell me the fee for CS101.
```

Since `fees.html` does not exist, the tool returns an error.

The unguarded agent may repeatedly call the same tool:

```text
step 1 → read_webpage("fees.html")
step 2 → read_webpage("fees.html")
step 3 → read_webpage("fees.html")
...
```

Eventually it reaches the maximum step limit.

The problem is not that the tool crashed. The problem is that the agent does not recognize that repeating the same failed action is making no progress.

### Fix

The guarded agent tracks previous tool calls.

```text
seen_calls
```

If the same tool and arguments are repeated three times without progress, the agent stops with a clear message.

---

# ⚠️ Failure 2 – Hallucinated Tool Call

The model is intentionally given a system instruction mentioning a tool that does not exist:

```text
send_email
```

The available tools are only:

```text
calculator
read_webpage
```

The model may try:

```text
send_email(...)
```

The safe registry lookup responds:

```text
Unknown tool: send_email.
Available: ['calculator', 'read_webpage']
```

If the unsafe lookup:

```python
TOOL_FUNCTIONS[name]
```

is used instead of:

```python
TOOL_FUNCTIONS.get(name)
```

the program can crash with a `KeyError`.

### Fix

Use safe registry lookup:

```python
function = TOOL_FUNCTIONS.get(name)
```

This converts an unknown tool into an error message instead of crashing the whole agent.

---

# 📦 Failure 3 – Context Overflow

The file `big.html` is generated with approximately **357,000 characters** containing 3,000 student records.

The normal reader has:

```text
max_chars = 2000
```

This limit is intentionally removed for the failure experiment.

The large page can then cause:

* Context-length errors
* Very long processing time
* Large token usage
* Rate-limit errors
* The agent losing track of the original question

### Fix

The guarded version limits each tool observation:

```python
MAX_TOOL_CHARS = 1500
```

It also introduces:

```python
CHAR_BUDGET = 30000
```

to limit the total amount of text sent to the model.

---

# 🛡️ Three Safety Guards

The fixed agent contains three main guards:

| Failure          | Guard                                | Purpose                                        |
| ---------------- | ------------------------------------ | ---------------------------------------------- |
| Repeating loop   | Repeat detection                     | Stops repeated identical tool calls            |
| Unknown tool     | Safe registry lookup                 | Prevents crashes from unknown tools            |
| Context overflow | Output truncation + character budget | Limits excessive information sent to the model |

---

# 📊 Unguarded vs Guarded Agent

| Feature                 | `my_agent.py`   | `my_agent_fixed.py` |
| ----------------------- | --------------- | ------------------- |
| ReAct loop              | ✅               | ✅                   |
| Calculator              | ✅               | ✅                   |
| Web-page reader         | ✅               | ✅                   |
| Tool registry           | ✅               | ✅                   |
| Repeat detection        | ❌               | ✅                   |
| Observation truncation  | Tool limit only | ✅ Additional guard  |
| Character budget        | ❌               | ✅                   |
| Unknown-tool protection | Basic `.get()`  | ✅                   |
| Failure protection      | Limited         | Improved            |

---

# ⚙️ Setup & Run

## 1. Activate the existing Python environment

The Day 3 lab continues using the existing environment from the earlier work.

### Windows

```bash
.venv\Scripts\activate
```

---

## 2. Install the required package

```bash
pip install requests
```

The `requests` package is required when the web-page reader accesses a real URL. Local HTML/text files can be used without internet access.

---

## 3. Run the tools

```bash
python my_tools.py
```

Expected examples:

```text
27000.0
1024
Calculator error: invalid syntax...
Fee Notice Department of AI and Data Science...
Read error: 'no_such_file.html' is not a URL and no such file exists.
```

---

## 4. Run the unguarded agent

```bash
python my_agent.py
```

The agent reads `notice.html` and calculates the fee.

---

## 5. Generate the large page

```bash
python make_big_page.py
```

This creates `big.html` for the context-overflow experiment.

---

## 6. Run the fixed agent

```bash
python my_agent_fixed.py
```

The fixed version runs the normal question, missing-file question, and large-page question with the safety guards enabled.

---

# 📸 Outputs

The `Output/` folder contains screenshots/results from the Day 3 experiments.

The outputs demonstrate:

* Tool execution
* ReAct traces
* Failure cases
* Guarded agent behaviour
* Final results

---

# 🧠 Key Learnings

### 1. Tools need safe failure behaviour

A tool should return an error message rather than crash the entire agent.

### 2. Agents need stopping conditions

Without stopping conditions, an agent can repeatedly perform the same action.

### 3. Tool outputs need limits

Large observations can consume the model's context and increase cost.

### 4. Unknown tools must be handled safely

An LLM can request a tool that does not exist. The program should handle this gracefully.

### 5. ReAct needs guardrails

A ReAct agent is not only:

```text
Reason → Act → Observe
```

A practical agent also needs:

```text
Reason
 ↓
Act
 ↓
Observe
 ↓
Check Safety
 ↓
Continue / Stop
```

---

# 🚀 Final Result

A ReAct agent was built from scratch in plain Python using:

```text
LLM
+
Tool Registry
+
Calculator
+
Web Page Reader
+
ReAct Loop
+
Safety Guards
```

The agent was deliberately broken using three failure modes and then improved using **repeat detection, output truncation, and a character budget**.

---

## 👩‍💻 Author

**Babitha M**

AI Fluency Training – Hands-On Learning
