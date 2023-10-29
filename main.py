from taipy.gui import Gui
import pandas as pd
import openai
import os
import time
from audioInterp import *

openai.api_key="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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    print(prompt)
    messages = [
        {"role": "system",
         "content": "You are an interviewer preparing questions"
        },
        {"role": "user", 
        "content": f"Give me 5 interview questions for this job position: {prompt}"}]
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
    state.returnVal = x
    
def printer(state):
    # state.value = state.content
    state.value = get_top_emotions(run(state.content))

def change(state):
    state.value = "Submitted!"

value = "Insert File..."
returnVal = ""
page = """

<center><|Generate interview questions|text|id=hdr|></center>
#
<center><|{prompt}|input|id=enter|label=Job Title|><|Generate Interview Questions|button|on_action=test|></center>
#
<center><|{returnVal}|input|id=response|label=Awaiting AI Response...|active=False|multiline=True|height=50|></center>

"""
page_file = """
<center><|AI Analyzations of your responses|text|id=hdr1|></center>

#
<center><|Upload a video of you answering the questions for, the previous page to receive feedback|></center>
#
<center><|{value}|text|id=hi|></center>
<center><|{content}|file_selector|extensions=.mp3,.mp4,.m4a|on_action=change|></center>
<center><|Submit|button|on_action=printer|></center>
"""

pages = {
    "/": "<|Proficient|text|id=title|height=30px|width=30px|><|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "generate-questions": page,
    "receive-feedback": page_file,
}


Gui(pages=pages).run(use_reloader=True, port=5001)
