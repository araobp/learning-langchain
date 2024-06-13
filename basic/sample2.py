import json
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "そばの原材料を教えて"
        },
    ],
    max_tokens=50,
    temperature=1,
    n=2,
)

print(json.dumps(response, indent=2, ensure_ascii=False))