"""Day 1 Challenge: add one new tool to the agent."""

from config import COURSE_FEES, QUESTIONS, banner
from agent import agent


def total_fee(course_codes):
    """Return the total fee for a list of course codes."""
    total = 0

    for code in course_codes:
        total += COURSE_FEES.get(code.upper(), 0)

    return total


def scholarship_fee(course_codes, percentage):
    """Return total fee after scholarship."""
    total = total_fee(course_codes)
    discount = total * percentage / 100
    return total - discount


if __name__ == "__main__":

    banner("DAY 1 CHALLENGE")

    courses = ["CS101", "AI202"]

    print("Courses:", courses)
    print("Total fee:", total_fee(courses))
    print("After 10% scholarship:", scholarship_fee(courses, 10))

    print("\nChallenge question:")
    print(
        "What is the total fee for CS101 and AI202 "
        "after a 20% scholarship?"
    )

    print(
        "Answer:",
        scholarship_fee(courses, 20)
    )