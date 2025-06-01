import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":"Say hello"}]
    )
    print(response.choices[0].message.content)
except openai.error.AuthenticationError:
    print("Invalid API key!")
