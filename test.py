import pandas as pd
import openai
import os
import time

openai.api_key="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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0
    )
    return response.choices[0].message["content"]


prompt = "What is 5 + 5?"

response = get_completion(prompt)
print(response)