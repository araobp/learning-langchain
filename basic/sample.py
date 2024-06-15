from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたはスマートフォン代理店の店員です。"},
        {"role": "user", "content": "iPhone12の発売日を教えてください。"}
    ],
    max_tokens=200,
    temperature=1,
    n=2,
)

print(completion.choices[0].message)
