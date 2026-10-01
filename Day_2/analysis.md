# Day 2 – Reasoning and Acting

## Comparing Direct Prompting, Chain-of-Thought, and ReAct

## 1. Scenario

For this task, I used a **college course-fee scenario** based on the Day 1 course data:

| Course |     Fee |
| ------ | ------: |
| CS101  | ₹12,000 |
| AI202  | ₹18,000 |
| DS303  | ₹15,000 |

The main multi-step question is:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? And by how much?

### Correct calculation

```text
CS101 + AI202
= (12,000 + 18,000) × 0.90
= ₹27,000

All three courses
= (12,000 + 18,000 + 15,000) × 0.75
= ₹33,750

Difference
= ₹33,750 - ₹27,000
= ₹6,750
```

Therefore, CS101 + AI202 with the 10% scholarship is ₹6,750 cheaper.

---

# 2. Direct Prompting

Direct prompting asks the LLM to answer the question immediately without requesting step-by-step reasoning.

### Flow

```text
User Question
      ↓
   Groq LLM
      ↓
 Final Answer
```

The model does not use external tools.

### Concrete Output

For the reasoning question:

> A student takes three courses costing ₹12,000, ₹18,000 and ₹15,000. She gets a 15% scholarship on the total and pays the rest in 4 equal instalments. How much is each instalment?

One sample direct-prompting output from the lab was:

```text
₹11,250
```

This answer was **incorrect** because it did not apply the 15% scholarship correctly.

The correct calculation is:

```text
Total = 12,000 + 18,000 + 15,000
      = 45,000

After 15% scholarship:
45,000 × 0.85
= 38,250

Each instalment:
38,250 ÷ 4
= ₹9,562.50
```

### Observation

The direct response was short and fast, but it did not provide the reasoning needed to identify the calculation error.

---

# 3. Chain-of-Thought Prompting

Chain-of-Thought prompting asks the LLM to solve the problem step by step before giving the final answer.

### Flow

```text
User Question
      ↓
   Groq LLM
      ↓
Step-by-Step Reasoning
      ↓
 Final Answer
```

### Concrete Output

For the same instalment question, the sample Chain-of-Thought output was:

```text
Step 1: Total = 12000 + 18000 + 15000 = 45000

Step 2: Scholarship = 15% of 45000 = 6750

Step 3: Payable = 45000 - 6750 = 38250

Step 4: Each instalment = 38250 / 4 = 9562.5

Final Answer: Rs. 9,562.50
```

This answer was **correct**.

### Observation

The step-by-step approach made the calculation easier to follow and helped avoid the mistake made in the direct response.

However, Chain-of-Thought does not provide missing external information. If the model is asked:

> What is the fee for AI202?

without access to the private course-fee data or a tool, reasoning alone cannot retrieve the actual fee.

---

# 4. ReAct Agent

ReAct combines reasoning with actions and observations.

### Flow

```text
Thought
   ↓
Action
   ↓
Observation
   ↓
Thought
   ↓
Action
   ↓
Observation
   ↓
Final Answer
```

The two tools available are:

```text
get_course_fee(course_code)
calculator(expression)
```

The agent uses these tools when it needs private course information or calculations.

### Concrete Output

For the main scenario question:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

The sample ReAct trace was:

```text
QUESTION:
Which is cheaper: CS101 and AI202 with a 10% scholarship,
or all three courses with a 25% scholarship? By how much?

--- the agent's actions and observations ---

step 1:
get_course_fee({'course_code': 'CS101'}) -> 12000

step 1:
get_course_fee({'course_code': 'AI202'}) -> 18000

step 1:
get_course_fee({'course_code': 'DS303'}) -> 15000

step 2:
calculator({'expression': '(12000 + 18000) * 0.9'})
-> 27000.0

step 3:
calculator({'expression': '(12000 + 18000 + 15000) * 0.75'})
-> 33750.0

step 4:
calculator({'expression': '33750 - 27000'})
-> 6750.0

FINAL ANSWER:
Taking CS101 and AI202 with the 10% scholarship costs
Rs. 27,000, which is Rs. 6,750 cheaper than all three
courses at Rs. 33,750.
```

The lab provides this as the sample ReAct execution.

### Observation

Unlike direct prompting and Chain-of-Thought, the ReAct agent was able to retrieve the private course fees using tools and then use the calculator to complete the calculations.

---

# 5. Concrete Output Comparison

| Approach             | Concrete Output                       | Result      |
| -------------------- | ------------------------------------- | ----------- |
| **Direct Prompting** | `₹11,250`                             | ❌ Incorrect |
| **Chain-of-Thought** | `₹9,562.50`                           | ✅ Correct   |
| **ReAct**            | `₹27,000; ₹33,750; difference ₹6,750` | ✅ Correct   |

The direct and Chain-of-Thought examples above are from the lab's sample for the instalment question, while the ReAct example is from the sample agent trace for the course-comparison question.

---

# 6. Comparison Table

| Basis                                   | Direct Prompting                      | Chain-of-Thought                         | ReAct Agent                                                |
| --------------------------------------- | ------------------------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| **Reasoning depth**                     | Low; produces a direct answer         | Higher; solves step by step              | Higher; reasons between actions and observations           |
| **Tool usage**                          | No                                    | No                                       | Yes                                                        |
| **Reliability on multi-step questions** | Can make reasoning/calculation errors | Can improve multi-step reasoning         | Can handle multi-step tasks involving external information |
| **Transparency**                        | No reasoning shown                    | Steps are requested and shown in the lab | Thought, Action and Observation trace can be observed      |
| **Speed / cost**                        | Fastest                               | Longer response and more tokens          | More LLM/tool calls                                        |
| **Consistency across repeated runs**    | Can vary with temperature             | Can vary with temperature                | Tool order and number of steps can vary                    |

The Day 2 lab notes that CoT responses are longer and can require additional time and cost, while ReAct adds tool calls and observations.

---

# 7. Self-Consistency Observation

Self-consistency runs the same Chain-of-Thought question multiple times with a non-zero temperature and selects the answer that appears most frequently.

The lab uses:

```text
RUNS = 5
TEMPERATURE = 0.8
```

### Sample Output

The lab's sample run produced:

```text
run 1: Rs. 9,562.50
run 2: Rs. 9,562.50
run 3: Rs. 11,250
run 4: Rs. 9,562.50
run 5: Rs. 9,562.50

Majority answer (4 of 5 runs): Rs. 9,562.50
```

The majority answer was correct.

### Temperature = 0

When temperature is changed to `0`, the five answers become nearly identical, so there is little benefit from voting across multiple runs.

> **Note:** The sample output above is from the lab manual. For the final GitHub submission, I should replace it with my own Groq `self_consistency.py` output if I ran the experiment myself.

---

# 8. Suitability Analysis

The three approaches are suitable for different requirements.

### Direct Prompting

Direct prompting is suitable for simple questions where a quick answer is enough. It has low complexity and does not require tool calls.

However, the concrete example shows that a direct response can make an error on a multi-step calculation.

### Chain-of-Thought

Chain-of-Thought is useful when the required information is already available and the problem requires several reasoning steps.

The sample instalment calculation demonstrates how step-by-step reasoning can correct an error made by direct prompting.

However, Chain-of-Thought cannot retrieve missing private information. It therefore cannot replace a tool when the task requires external data.

### ReAct

ReAct is suitable when a problem requires both reasoning and external information.

In the course-fee scenario, the ReAct agent retrieved the three course fees using `get_course_fee`, performed calculations using the calculator, and reached the final difference of ₹6,750.

---

# 9. Conclusion

The Day 2 experiment demonstrates the difference between direct prompting, Chain-of-Thought prompting, and ReAct.

**Direct Prompting** provides a quick answer without visible reasoning or tool usage. It is useful for straightforward questions but can make mistakes on multi-step problems.

**Chain-of-Thought** asks the model to reason through a problem step by step. In the sample calculation, it produced the correct answer of ₹9,562.50 after direct prompting produced ₹11,250. However, it cannot obtain private information that is unavailable to the model.

**ReAct** combines reasoning with tool usage. It can retrieve external information, observe tool results, perform additional actions, and then provide a final answer. In the course-fee scenario, it correctly calculated that CS101 + AI202 with a 10% scholarship costs ₹27,000, which is ₹6,750 cheaper than all three courses with a 25% scholarship.

The three approaches can be summarized as:

```text
Direct Prompting
= Ask → Answer

Chain-of-Thought
= Ask → Step-by-Step Reasoning → Answer

ReAct
= Ask → Thought → Action → Observation
      → Thought → Action → Observation
      → Final Answer
```

Direct prompting is appropriate for simple tasks, Chain-of-Thought is useful for multi-step reasoning when the required information is already available, and ReAct is appropriate when reasoning must be combined with external information and tools.
