from taipy.gui import Gui
import pandas as pd
import openai
import os
import time
from audioInterp import *

openai.api_key="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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system",
         "content": "You are an interviewer preparing questions for a specified role"
        },
        {"role": "user", 
        "content": f"Give me 5 interview questions based on the job title: {prompt}"}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0
    )
    return response.choices[0].message["content"]


prompt = ""
prompt2 = ""
content = ""

# response = get_completion(prompt)

def test(state):
    state.prompt2 = state.prompt
    x = get_completion(state.prompt2)
    state.value = x
    
def printer(state):
    state.value = state.content
    state.value = asyncio.run(main(state.content))

value = "Insert File..."

page = """
#Rendezvous

<|{value}|text|id=hi|>
#
<|{content}|file_selector|extensions=.mp3,.mp4,.m4a|>
<|Test File|button|on_action=printer|>
#
<|{prompt}|input|id=enter|>
<|Submit Resume|button|on_action=test|>

"""

Gui(page).run(use_reloader=True, port=5001)
