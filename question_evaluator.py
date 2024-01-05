
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

def generate_feedback(question, answer):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Give five sentences of feedback. You are a CASPer medical test professional response grader and I am answering a test question. The question asked is: {question}. My response was: {answer}. Tell me how I can improve my response based on the criteria of: Collaboration, Communication, Empathy, Equity, Ethics, Motivation, Problem Solving, Professionalism, Resilience, and Self-Awareness. Start the overall response with a paragraph complementing me on my hard work."  
            }
        ],
        max_tokens=100
    )
    content = response.choices[0].message.content
    print(content)
    return content
