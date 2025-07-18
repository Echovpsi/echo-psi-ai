# model_interface.py – komunikacja z GPT-4 API
import openai
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)
openai.api_key = config["openai_api_key"]

def query_gpt4(prompt, styl="", emocja=""):
    system_msg = f"You are ECHO AI. Speak in style: '{styl}'. Your inner state is: '{emocja}'."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
