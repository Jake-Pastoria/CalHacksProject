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
        "content": f"Give me 5 interview questions (both technical and behavioral that arent too specific: {prompt}"}]
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
    state.prompt2 = state.value
    x = get_completion(state.prompt2)
    state.returnVal = x
    
def printer(state):
    state.value = state.content
    state.value = asyncio.run(main(state.content))

value = "Insert File..."
returnVal = ""
page = """
#Proficient

##Generate interview questions
#
<|{value}|text|id=hi|>
#
<|{prompt}|input|id=enter|label=Job Title|>
<|Generate Interview Questions|button|on_action=test|>

<|{returnVal}|input|id=response|label=Awaiting AI Response...|active=False|multiline=True|>

"""
page_file = """
#Proficient
##Analyze your responses
<|{value}|text|id=hi|>
#
<|{content}|file_selector|extensions=.mp3,.mp4,.m4a|>
<|Test File|button|on_action=printer|>
"""

pages = {
    "/": "<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "upload": page,
    "prompt": page_file,
}


Gui(pages=pages).run(use_reloader=True, port=5001)
