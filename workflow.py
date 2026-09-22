"""Step 3: deterministic workflow. No LLM is needed for the fee questions."""

from config import COURSE_FEES, QUESTIONS, banner


def get_course_fee(course_code):
    return COURSE_FEES[course_code.upper()]


def workflow(question):
    q = question.lower()

    # Q1: single course fee
    if "fee for ai202" in q:
        return f"Fee for AI202: Rs. {get_course_fee('AI202'):,}"

    # Q2: total fee after 10% scholarship
    if "total fee" in q and "cs101" in q and "ai202" in q:
        total = get_course_fee("CS101") + get_course_fee("AI202")
        discounted = total * 0.90
        return f"Total fee: Rs. {discounted:,.0f}"

    # Q3: compare DS303 and CS101
    if "ds303" in q and "cs101" in q and "more expensive" in q:
        difference = get_course_fee("DS303") - get_course_fee("CS101")
        return f"DS303 is more expensive by Rs. {difference:,}"

    # Q4: no rule has been written for this
    return "No rule for this question."


banner("RULE-BASED WORKFLOW")

for i, question in enumerate(QUESTIONS, start=1):
    print(f"Q{i}: {question}")
    print(f"A{i}: {workflow(question)}\n")