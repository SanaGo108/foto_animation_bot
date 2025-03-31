import requests
from config import D_ID_API_KEY, D_ID_API_URL


def animate_photo(image_url):
    """
    Отправляет изображение в D-ID API и возвращает URL анимации.
    """
    headers = {
        "Authorization": f"Bearer {D_ID_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "source_url": image_url,
        "script": {
            "type": "text",
            "input": "Hello! Nice to meet you!",
            "voice_id": "en-US-Wavenet-D"
        }
    }

    response = requests.post(D_ID_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("result_url")
    else:
        return None
