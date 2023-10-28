from taipy.gui import Gui, notify
import pandas as pd
import openai
import os
import time
import InternshipTracler

openai.api_key="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"

def getPosition(selectCompany,InternshipTracker=InternshipTracler.InternshipTracker):
    listofOpp = InternshipTracker.getApplication(selectCompany)
    return listofOpp[0].position


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages =  messages = [
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

# Main
tracker = InternshipTracler.InternshipTracker()
tracker.addAplication("Amazon", "SWE", "applied")
tracker.addAplication("Amazon", "data engineer", "interviewd")
tracker.addAplication("Google", "front end developer", "interviewd")
# print(getPosition("Google", tracker))
prompt = getPosition("Google", tracker)

response = get_completion(prompt)
print(response)