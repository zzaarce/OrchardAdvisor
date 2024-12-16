import requests
import json
from config import Config

class LLMInterface:
    def __init__(self):
        self.api_key = Config.MODEL_API_KEY
        self.endpoint = Config.MODEL_ENDPOINT
        self.model_name = Config.MODEL_NAME

    def chat(self, messages, temperature=0):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": messages,
            "temperature": temperature
        }
        response = requests.post(self.endpoint, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            resp_json = response.json()
            return resp_json["choices"][0]["message"]["content"]
        else:
            raise Exception(f"LLM API request failed. Status: {response.status_code}, Msg: {response.text}")
