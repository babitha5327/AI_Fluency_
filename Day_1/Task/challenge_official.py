"""Day 1 official challenge: course pairs within a budget."""

from config import COURSE_FEES, banner


def find_course_pairs(budget):
    courses = list(COURSE_FEES.keys())

    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            course1 = courses[i]
            course2 = courses[j]

            total = COURSE_FEES[course1] + COURSE_FEES[course2]

            if total <= budget:
                print(
                    f"{course1} + {course2} = Rs. {total:,}"
                )


if __name__ == "__main__":

    banner("DAY 1 OFFICIAL CHALLENGE")

    budget = 30000

    print(
        "I can pay Rs. 30,000. "
        "Which two courses can I take together within this budget?"
    )

    print("\nPossible course pairs:")

    find_course_pairs(budget)