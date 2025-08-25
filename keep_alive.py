import requests
import time
from datetime import datetime

# List of URLs you want to keep alive
URLS = [
    "https://movie-recommendation-system-s1ty1.streamlit.app/",
    "https://huggingface.co/spaces/imsatya/spam-message-classification",
    "https://car-price-prediction-s1ty1.onrender.com/",
    "https://ai-image-detection-s1ty1.onrender.com/",
]

def keep_alive():
    for url in URLS:
        try:
            r = requests.get(url, timeout=10)
            print(f"[{datetime.now()}] {url} -> {r.status_code}")
        except Exception as e:
            print(f"[{datetime.now()}] {url} -> ERROR: {e}")

if __name__ == "__main__":
    keep_alive()

