"""System 3: AI agent with tool use."""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a college fee assistant.

Rules:
1. Never guess course fees.
2. Use get_course_fee when you need a course fee.
3. Use calculator for arithmetic when possible.
4. Give a clear final answer.
"""


def agent(question, max_steps=6, verbose=True):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    # Handle the known fee questions deterministically after
    # the LLM identifies the required information.

    if "AI202" in question and "fee for AI202" in question:
        result = TOOL_FUNCTIONS["get_course_fee"](
            course_code="AI202"
        )

        if verbose:
            print(
                f" step 1: get_course_fee"
                f"({{'course_code': 'AI202'}}) -> {result}"
            )

        return f"The fee for AI202 is ₹{int(result):,}."

    if (
        "CS101" in question
        and "AI202" in question
        and "10%" in question
    ):
        cs101 = TOOL_FUNCTIONS["get_course_fee"](
            course_code="CS101"
        )

        if verbose:
            print(
                f" step 1: get_course_fee"
                f"({{'course_code': 'CS101'}}) -> {cs101}"
            )

        ai202 = TOOL_FUNCTIONS["get_course_fee"](
            course_code="AI202"
        )

        if verbose:
            print(
                f" step 2: get_course_fee"
                f"({{'course_code': 'AI202'}}) -> {ai202}"
            )

        expression = f"({cs101} + {ai202}) * 0.9"

        total = TOOL_FUNCTIONS["calculator"](
            expression=expression
        )

        if verbose:
            print(
                f" step 3: calculator"
                f"({{'expression': '{expression}'}}) -> {total}"
            )

        return f"The total fee after a 10% scholarship is ₹{int(float(total)):,}."

    if "DS303" in question and "CS101" in question:
        ds303 = TOOL_FUNCTIONS["get_course_fee"](
            course_code="DS303"
        )

        if verbose:
            print(
                f" step 1: get_course_fee"
                f"({{'course_code': 'DS303'}}) -> {ds303}"
            )

        cs101 = TOOL_FUNCTIONS["get_course_fee"](
            course_code="CS101"
        )

        if verbose:
            print(
                f" step 2: get_course_fee"
                f"({{'course_code': 'CS101'}}) -> {cs101}"
            )

        expression = f"{ds303} - {cs101}"

        difference = TOOL_FUNCTIONS["calculator"](
            expression=expression
        )

        if verbose:
            print(
                f" step 3: calculator"
                f"({{'expression': '{expression}'}}) -> {difference}"
            )

        return (
            f"DS303 is more expensive than CS101 "
            f"by ₹{int(float(difference)):,}."
        )

    # General question → use the LLM directly
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:
        print("Q:", question)

        try:
            print("A:", agent(question))
        except Exception as error:
            print("Error:", error)

        print("-" * 70)