import os

api_url = "https://api.xty.app/v1/chat/completions"
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}


import requests as rq
def prompt(_prompt: str):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": _prompt}
        ]
    }
    response = rq.post(api_url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
