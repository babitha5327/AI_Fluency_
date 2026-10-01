# AI Fluency – Day 1

## Agentic AI: Foundations and Open-Source Practice

### 📌 Lab Title

**Python in VS Code: Chatbot vs Rule-Based Workflow vs AI Agent**

## 🎯 Objective

Set up a Python environment in VS Code and connect it with an LLM using the **Groq API**.

The lab implements and compares:

* LLM Chatbot
* Rule-Based Workflow
* AI Agent

## 🛠️ Technologies Used

* Python 3.11+
* Visual Studio Code
* Groq API
* OpenAI Python package
* python-dotenv
* Large Language Model (LLM)

## 📂 Project Structure

```text
Day1/
│
├── README.md
├── .gitignore
├── requirements.txt
├── .env
├── config.py
├── check_setup.py
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
└── challenge.py
```

## 🔑 LLM Configuration

For this lab, I used **Groq** as the LLM provider.

```text
Provider: Groq
API: OpenAI-compatible API
```

The API key is stored in the `.env` file and is **not uploaded to GitHub**.

```text
.env
```

is added to `.gitignore` to protect the API key.

## 🤖 Systems Implemented

### 1. LLM Chatbot

The chatbot sends the user's question directly to the LLM.

```text
User
  ↓
Groq LLM
  ↓
Response
```

The chatbot does not have access to the private course-fee data or external tools.

### 2. Rule-Based Workflow

The workflow uses predefined Python rules.

```text
User
  ↓
Python Rules
  ↓
Matching Rule
  ↓
Response
```

It provides reliable results for predefined questions but can be rigid when the question changes.

### 3. AI Agent

The AI agent combines:

```text
LLM + Tools + Loop
```

The agent can decide which tool to use based on the user's question.

Available tools:

* `get_course_fee`
* `calculator`

### Agent Flow

```text
User
  ↓
Groq LLM
  ↓
Choose Tool
  ↓
Execute Tool
  ↓
Observe Result
  ↓
Final Response
```

The agent follows the **Reason → Act → Observe** process.

## 💰 Sample Problem

The lab uses private college course-fee data:

| Course |     Fee |
| ------ | ------: |
| CS101  | ₹12,000 |
| AI202  | ₹18,000 |
| DS303  | ₹15,000 |

### Test Questions

1. What is the fee for AI202?
2. What is the total fee for CS101 and AI202 after a 10% scholarship?
3. Is DS303 more expensive than CS101, and by how much?
4. Write a two-line welcome message for new AI students.

## 🧠 Key Observations

### Chatbot

The chatbot may generate an incorrect answer when the required private data is not available to the LLM.

This demonstrates **hallucination**.

### Workflow

The workflow gives correct results for questions covered by its rules.

However, it can fail when the question is written differently or when no rule exists for that type of question.

### Agent

The agent can use tools to retrieve course fees and perform calculations.

For example:

```text
CS101 → ₹12,000
AI202 → ₹18,000

(12000 + 18000) × 0.9

= ₹27,000
```

The agent can also use the calculator to compare course fees.

## 🆚 Comparison

| Feature             | Chatbot | Workflow | Agent |
| ------------------- | ------- | -------- | ----- |
| LLM                 | ✅       | ❌        | ✅     |
| Tools               | ❌       | ❌        | ✅     |
| Fixed Rules         | ❌       | ✅        | ❌     |
| Private Data Access | ❌       | ✅        | ✅     |
| Flexible            | ✅       | ❌        | ✅     |
| Tool Calling        | ❌       | ❌        | ✅     |

## 🧪 Challenge

The challenge question is:

```text
I can pay ₹30,000.
Which two courses can I take together within this budget?
```

The agent can use the available course-fee information and calculator to evaluate the possible combinations.

## 📚 Concepts Learned

* Large Language Models
* Chatbots
* Rule-Based Workflows
* AI Agents
* Tool Calling
* Reason → Act → Observe
* Hallucination
* Virtual Environments
* OpenAI-Compatible APIs
* Environment Variables
* `.env`
* `.gitignore`

## 🔐 Security

The Groq API key is stored in `.env`.

**The API key must never be uploaded to GitHub.**

```text
.env
```

is included in `.gitignore`.

## ✅ Result

Successfully set up a Python AI development environment in VS Code using **Groq**, and implemented and compared a chatbot, rule-based workflow, and AI agent.

## 🚀 Day 1 Takeaway

```text
Chatbot
= LLM + Conversation

Workflow
= Fixed Rules + Execution

Agent
= LLM + Tools + Loop
```

Day 1 provided the foundation for understanding how AI agents differ from simple chatbots and predefined workflows.
