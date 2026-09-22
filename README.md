# AI_Fluency

Day 1 AI Fluency Lab — LLM APIs, rule-based workflows, tools, and AI agents.

## Overview

This project demonstrates the basics of building AI applications using an LLM API and progressively adding deterministic tools and agent workflows.

## Systems

### System 1 — Chatbot

- Connects to the Groq API
- Uses `openai/gpt-oss-20b`
- Answers general questions using the LLM

### System 2 — Rule-Based Workflow

- Uses predefined rules for course-fee questions
- Retrieves course fees
- Performs scholarship calculations
- Compares course fees

### System 3 — Tools

Available tools:

- `get_course_fee()`
- `calculator()`

### System 4 — AI Agent

The AI agent decides when to use available tools.

Example workflow:

1. Retrieve CS101 fee
2. Retrieve AI202 fee
3. Calculate scholarship
4. Generate the final answer

## Course Fees

| Course | Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

## Example

Question:

> What is the total fee for CS101 and AI202 after a 10% scholarship?

Calculation:

```text
CS101 + AI202 = Rs. 30,000
10% scholarship = Rs. 3,000
Final fee = Rs. 27,000
