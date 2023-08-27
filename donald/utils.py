from __future__ import annotations

import os

import openai

# Set up the OpenAI API key
API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = API_KEY


def query_openai(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": prompt_text}],
        temperature=1.0,
    )
    return response["choices"][0]["message"]["content"].strip()


if __name__ == "__main__":
    question = input("Ask a question to OpenAI: ")
    response = query_openai(question)
    print("OpenAI responds:", response)
