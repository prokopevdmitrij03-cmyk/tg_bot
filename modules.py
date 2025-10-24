from config import API_KEY



async def get_response(answer: str):
    response = client.chat.completions.create(
        model = model,
        messages = [
            {"role": "user", "content": f"{answer}"}
        ]
    )
    return response.choices[0].message.content

def get_credits():
    url = "https://api.sunoapi.org/api/v1/generate/credit"
    headers = {"Autorization": f"Bearer {SUNO_API_TOKEN}"}
    responce = requests.get(url, headers = headers)
    return responce.json()