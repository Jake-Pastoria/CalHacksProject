from taipy.gui import Gui
import pandas as pd
import openai
import os
import time

openai.api_key=""

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

value = 10

page = """
#Rendezvous {response}

Slider value: <|{value}|> <br/>
<|{value}|slider|>

"""

Gui(page).run(use_reloader=True, port=5001)