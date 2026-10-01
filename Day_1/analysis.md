# Day 1 Practice Task – Chatbot vs Workflow vs AI Agent

## 1. Scenario

For this task, I selected a **college course fee assistant** scenario.

The college has private course fee information that is not available to a public LLM:

| Course |     Fee |
| ------ | ------: |
| CS101  | ₹12,000 |
| AI202  | ₹18,000 |
| DS303  | ₹15,000 |

The same set of questions is given to three different systems:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The purpose is to understand how each approach handles private data, decision-making, tools, multi-step tasks, automation, flexibility, and reliability.

---

# 2. Plain Chatbot

## How it works

The plain chatbot sends the user's question directly to the LLM through the **Groq API**.

```text
User Question
      ↓
   Groq LLM
      ↓
   Response
```

The chatbot does not have access to the college's private course-fee data and does not use any external tools.

## Data Used

The chatbot only receives the user's question and the instructions given to the LLM. It does not directly access the private course-fee dictionary.

Therefore, when the user asks for a course fee that is private information, the chatbot does not have the required data.

## Tools and Rules

The plain chatbot does not use tools or predefined Python rules.

It mainly depends on the LLM to generate the response.

## Handling the User Request

For a question such as:

> What is the fee for AI202?

the chatbot sends the question to the Groq LLM and returns the generated response.

Since the actual fee data is not provided to the chatbot, the LLM may generate an incorrect answer.

## Limitation

The main limitation observed is **hallucination**.

The chatbot may provide a confident answer even though it does not have access to the private course-fee information. The Day 1 lab demonstrates this behaviour with the private course-fee questions.

However, for a question that does not require private data, such as writing a welcome message, the chatbot can generate an appropriate response.

---

# 3. Rule-Based Workflow

## How it works

The rule-based workflow uses predefined Python rules and conditions.

```text
User Question
      ↓
Python Rules
      ↓
Match Condition
      ↓
Response
```

No LLM is involved in this system.

## Data Used

The workflow has direct access to the private course-fee data:

```text
CS101 = ₹12,000
AI202 = ₹18,000
DS303 = ₹15,000
```

## Tools and Rules

The workflow uses predefined rules written in Python.

For example, it can identify course codes and calculate a total fee when the appropriate conditions are satisfied.

## Handling the User Request

For example:

> What is the fee for AI202?

The workflow identifies `AI202`, looks up its fee, and returns:

```text
Fee for AI202: ₹18,000
```

For:

> What is the total fee for CS101 and AI202 after a 10% scholarship?

the workflow calculates:

```text
(₹12,000 + ₹18,000) × 90%
= ₹27,000
```

## Limitation

The workflow is reliable for situations covered by its predefined rules, but it is rigid.

For example, if the user changes the wording or asks a type of question for which no rule was created, the workflow may fail.

The Day 1 lab specifically demonstrates that changing the wording of the scholarship question can cause the workflow rule not to match.

---

# 4. AI Agent

## How it works

The AI agent combines:

```text
LLM + Tools + Loop
```

The agent uses the Groq LLM to decide what action is required and can call tools to obtain information or perform calculations.

```text
User Question
      ↓
   Groq LLM
      ↓
Choose Tool
      ↓
Execute Tool
      ↓
Observe Result
      ↓
Continue / Final Answer
```

This follows the **Reason → Act → Observe** process described in the Day 1 lab.

## Data Used

The agent can access the private course-fee information through the `get_course_fee` tool.

The available course data is:

```text
CS101 = ₹12,000
AI202 = ₹18,000
DS303 = ₹15,000
```

## Tools Used

The agent has two tools:

### 1. `get_course_fee`

Used to retrieve the fee for a course.

Example:

```text
get_course_fee("AI202")
→ ₹18,000
```

### 2. `calculator`

Used to perform arithmetic calculations.

Example:

```text
(12000 + 18000) × 0.9
→ ₹27,000
```

## Handling the User Request

For:

> What is the total fee for CS101 and AI202 after a 10% scholarship?

the agent can perform multiple steps:

```text
Step 1:
Get CS101 fee
→ ₹12,000

Step 2:
Get AI202 fee
→ ₹18,000

Step 3:
Use calculator
→ (12000 + 18000) × 0.9

Final Result:
→ ₹27,000
```

For:

> Is DS303 more expensive than CS101, and by how much?

the agent can retrieve both fees and use the calculator:

```text
DS303 = ₹15,000
CS101 = ₹12,000

₹15,000 - ₹12,000
= ₹3,000
```

Therefore, the agent can answer that DS303 costs ₹3,000 more than CS101.

## Limitation

The agent is more flexible because it can select and use tools, but its behaviour can vary between runs.

The Day 1 lab notes that small local models can sometimes skip a tool, guess an answer, repeat a tool call, or fail to complete the loop. This shows that tool-using agents can have reliability issues.

---

# 5. Comparison Table

| Basis                        | Plain Chatbot                                                             | Rule-Based Workflow                           | AI Agent                                                           |
| ---------------------------- | ------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| **Flexibility**              | High for natural-language responses, but limited by available information | Low because it depends on predefined rules    | High because the LLM can decide which tools and actions are needed |
| **Decision-making**          | Generates a response using the LLM                                        | Decisions are predefined by Python conditions | LLM decides which tool to use and what action to take              |
| **Tool usage**               | No tools                                                                  | No external AI tools                          | Uses `get_course_fee` and `calculator`                             |
| **Private-data access**      | No direct access                                                          | Yes, directly through Python data             | Yes, through tools                                                 |
| **Multi-step task handling** | Limited for private-data tasks                                            | Limited to programmed rules                   | Can perform multiple tool calls in a loop                          |
| **Automation**               | Automates response generation                                             | Automates predefined tasks                    | Automates tasks involving decisions and tool usage                 |
| **Reliability**              | Can hallucinate when information is unavailable                           | Reliable for predefined rules but rigid       | Can solve flexible tasks, but tool use and execution can vary      |

---

# 6. Suitability Analysis

For this college course-fee scenario, the three approaches have different characteristics.

The **plain chatbot** is useful when the task mainly requires natural-language conversation or generating content that does not depend on private data. However, it is not suitable for answering private fee questions when the required information is not provided to the LLM because it may generate an incorrect answer.

The **rule-based workflow** is useful for predictable and well-defined fee-related operations. When the question matches an existing rule, the workflow can provide consistent results. However, new question types or different wording may require additional rules.

The **AI agent** can access the private course information through tools and can perform multiple actions to complete a task. For example, it can retrieve multiple course fees and use the calculator to perform the required calculation. This makes it suitable for tasks that require private data, tool usage, and multiple steps.

Therefore, for this particular scenario, the AI agent demonstrates the required combination of **LLM + Tools + Loop** and can handle more varied requests than the fixed workflow. At the same time, the workflow remains useful for simple, fixed operations where predefined behaviour is sufficient.

---

# 7. General Conclusion

The experiment demonstrates the difference between a plain chatbot, a rule-based workflow, and an AI agent.

A **chatbot** mainly uses an LLM to understand a question and generate a response. It is suitable for conversational tasks, content generation, and questions that do not require unavailable private information.

A **rule-based workflow** follows predefined steps and conditions without using an LLM. It is useful when the task is predictable, the rules are known in advance, and consistent behaviour is important.

An **AI agent** combines an LLM, tools, and a loop. It can reason about the task, select appropriate tools, observe the results, and continue taking actions until the task is completed.

The main difference can be summarized as:

```text
Chatbot
= LLM + Conversation

Workflow
= Rules + Predefined Steps

AI Agent
= LLM + Tools + Loop
```

The choice of approach depends on the problem. Simple conversational tasks can use a chatbot, predictable tasks can use a rule-based workflow, and tasks requiring private data, tool usage, decision-making, and multiple steps can use an AI agent.
