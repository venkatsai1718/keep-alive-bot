import requests
import time
from datetime import datetime

# List of URLs you want to keep alive
URLS = [
    "https://your-render-app.onrender.com",
    "https://your-hf-space.hf.space"
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
