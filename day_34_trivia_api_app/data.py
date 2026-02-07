import requests
# https://opentdb.com/api.php?amount=10
# https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean
import html

import time, requests

def get_quiz_data(retries=5):
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
    for attempt in range(retries):
        r = requests.get(url, timeout=10)
        if r.status_code == 429:
            time.sleep(2 ** attempt)
            continue
        r.raise_for_status()
        return r.json().get("results", [])
    return []