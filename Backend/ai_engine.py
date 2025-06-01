import openai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

openai.api_key = os.getenv("OPENAI_API_KEY")
print("Loaded OpenAI API Key:", openai.api_key)

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set it in your .env file.")

class OpenAIChatEngine:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model

    def get_response(self, user_input: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices[0].message.content.strip()
        except openai.error.AuthenticationError:
            return "Invalid OpenAI API key. Please check your `.env` file."
        except Exception as e:
            return f"Unexpected Error: {str(e)}"
