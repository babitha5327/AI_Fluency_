"""Step 2: simple chatbot. Notice that it does NOT know the private course fees."""

from config import client, MODEL, QUESTIONS, banner

banner("CHATBOT")

for i, question in enumerate(QUESTIONS, start=1):
    print(f"Q{i}: {question}")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful college assistant. "
                    "Answer clearly and briefly."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content.strip()

    print(f"A{i}: {answer}\n")