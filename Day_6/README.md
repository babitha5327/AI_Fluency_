# Day 6 – Reliable Tool Calling

## Student Study Planner

This is my Day 6 assessment project on **Reliable Tool Calling** using an OpenAI-compatible API.

In this project, I implemented tool calling with validation, retry handling, fault injection, and structured outputs.

---

## Objective

The main objective of this assessment is to understand how to make tool calling more reliable.

I learned how to:

* Create tools using JSON Schema
* Define required arguments
* Use enum values
* Validate tool arguments
* Handle malformed tool calls
* Handle missing and extra arguments
* Handle wrong data types
* Handle invalid enum values
* Handle multiple tool calls
* Retry truncated responses
* Detect repeated tool calls
* Test failures using fault injection
* Compare JSON mode and schema mode

---

## Scenario

I selected **Student Study Planner** as my scenario.

I created two tools:

### 1. `get_subject_info`

This tool gives information about a subject.

Example:

```json
{
  "subject": "java",
  "priority": "high"
}
```

The priority can be:

```text
low
medium
high
```

### 2. `calculate_study_time`

This tool calculates the total study time.

Example:

```json
{
  "subjects": 3,
  "hours_per_subject": 2
}
```

Output:

```text
Total study time: 6 hours
```

---

## Files

```text
day6_assessment/
│
├── tools.py
├── validator.py
├── agent.py
├── fault_injection.py
├── structured_outputs.py
├── analysis.md
├── README.md
├── screenshots/
└── .gitignore
```

### File Description

| File                    | Description                          |
| ----------------------- | ------------------------------------ |
| `tools.py`              | Contains my tools and JSON schemas   |
| `validator.py`          | Validates tool arguments             |
| `agent.py`              | Contains the main tool-calling agent |
| `fault_injection.py`    | Tests different malformed tool calls |
| `structured_outputs.py` | Tests JSON and schema outputs        |
| `analysis.md`           | Contains my detailed analysis        |
| `README.md`             | Project documentation                |
| `.gitignore`            | Prevents `.env` from being uploaded  |

---

## Tool Schema

I used JSON Schema for defining the tool arguments.

The schemas contain:

* `type`
* `properties`
* `required`
* `enum`
* `additionalProperties: false`

For example, the priority argument uses an enum:

```text
low
medium
high
```

This prevents invalid values such as:

```text
urgent
```

---

## Validation

Before executing a tool, my program validates the arguments.

I tested:

1. Missing argument
2. Extra/invented argument
3. Wrong type
4. Invalid enum value
5. Invalid JSON
6. Unknown tool
7. Invalid argument structure

The validation prevents invalid model-generated arguments from directly reaching the Python function.

---

## Tool Calling Flow

The flow of my agent is:

```text
User Question
      ↓
Language Model
      ↓
Tool Call
      ↓
Parse JSON
      ↓
Find Tool
      ↓
Validate Arguments
      ↓
Execute Tool
      ↓
Return Tool Result
      ↓
Final Answer
```

---

## Multiple Tool Calls

I also tested a question that can require more than one tool.

For example:

```text
Tell me about Java and calculate the total study time
for 3 subjects at 2 hours per subject.
```

The agent can call:

```text
get_subject_info
```

and:

```text
calculate_study_time
```

The program processes the tool calls and returns the results to the model.

---

## Retry Handling

I added handling for:

```text
finish_reason = length
```

If the response is truncated, my program increases the token limit and retries.

This prevents the agent from stopping immediately when the response reaches the token limit.

---

## Repeated Tool Calls

I also added a check for repeated identical tool calls.

If the same tool is repeatedly called with the same arguments, the agent stops after the configured limit.

This helps prevent an infinite loop.

---

## Fault Injection

I created `fault_injection.py` to deliberately test incorrect tool calls.

I tested cases such as:

* Invalid JSON
* Unknown tool
* Missing argument
* Wrong type
* Invalid enum
* Invented argument
* Wrong argument structure
* Wrong numeric type
* Negative value

The purpose was to check whether my program could handle these cases without crashing.

---

## Structured Outputs

I compared three approaches:

### 1. No Constraint

The model is allowed to generate a normal response.

### 2. JSON Mode

The model is asked to return JSON.

### 3. Schema Mode

The model is given a specific JSON Schema.

This helped me understand that structured outputs are useful when I need predictable data from the model.

---

## Tool Calling vs Structured Outputs

I understood the difference as:

**Tool Calling**

Used when the model needs my program to perform an action.

Example:

```text
Calculate study time
```

**Structured Outputs**

Used when I want the model to return information in a fixed format.

Example:

```json
{
  "subject": "Java",
  "priority": "high",
  "needs_tool": true
}
```

---

## What I Learned

Through this assessment, I learned that I should not directly trust tool arguments generated by a language model.

The tool call should first go through:

```text
Parse → Validate → Execute
```

I also learned how to handle malformed JSON, invalid arguments, multiple tool calls, truncated responses and repeated tool calls.

Fault injection helped me test the reliability of my validation code using deliberately incorrect inputs.

I also understood that tool calling and structured outputs have different purposes.

---

## How to Run

First activate my virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install openai python-dotenv
```

Then run:

```powershell
python validator.py
```

```powershell
python fault_injection.py
```

```powershell
python agent.py
```

```powershell
python structured_outputs.py
```

---

## Screenshots

I included screenshots of my execution results in the `screenshots` folder.

The screenshots cover:

* Validator output
* Fault injection
* Single tool call
* Multiple tool calls
* Invalid-value handling
* No-tool question
* Structured outputs

---

## Security

My API configuration is stored in `.env`.

I added `.env` to `.gitignore` so that my API key is not uploaded to GitHub.

```text
.env
__pycache__/
*.pyc
```

---

## Conclusion

This assessment helped me understand how reliable tool calling works in an AI agent.

I learned that a model can generate incorrect or malformed tool arguments, so validation and error handling are important.

By adding validation, retry logic, fault injection and repeated-call protection, I made my tool-calling system more reliable.

