from taipy.gui import Gui, notify
# import pandas as pd
# import openai
# import os
# import time

# openai.api_key=""

# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#     model=model,
#     messages=messages,
#     temperature=0
#     )
#     return response.choices[0].message["content"]


# prompt = "What is 5 + 5?"

# response = get_completion(prompt)
section_1 = """
<layout|columns=1 1 1|
#Rendezvous 

<|navbar|lov={[("section_1", "Resume Builder"), ("section_2", "Internship Tracker")]}|>
|>

Dashboard
Section1
"""

value = 10

page = """


Slider value: <|{value}|> <br/>
<|{value}|slider|>

"""
section_2="""
#Rendezvous 

<|navbar|lov={[("section_1", "Resume Builder"), ("https://www.taipy.io/project/creating-a-data-dashboard/", "Internship Tracker")]}|>
|>

Section 2
"""

Gui(section_1 + page).run(use_reloader=True, port=5001)