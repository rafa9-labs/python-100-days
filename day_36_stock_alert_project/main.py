import requests
from twilio.rest import Client


# params = {
#     # Make a Json here for the params to input in the API request.
# }

# After that create request with endpoint + key
# create request. and verificate status.

# Get the json.
# Check what you want from the json and in format is your required information.

# Get the information and make the message that you will send.

# Create a Client for the message API we have. 
# Then create / call the message method and with the sender numbers the message and the recivers number.

# TRIAL VERSION BLOCKS THE WORDS.

import config  # must contain: STOCK_API_KEY, NEWS_API_KEY, sms_account_sid, auth_token, from_, to

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def clamp(s: str, n: int) -> str:
    """Shorten text to n characters to avoid Twilio trial multi-segment SMS (30044)."""
    s = (s or "").strip().replace("\n", " ")
    return s if len(s) <= n else s[: n - 3] + "..."


def get_pct_change_or_none() -> float | None:
    """Fetch latest 2 daily closes from Alpha Vantage and compute % change. Returns None if rate-limited."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": config.STOCK_API_KEY,
    }

    r = requests.get(STOCK_ENDPOINT, params=params, timeout=10)
    r.raise_for_status()
    stock_data = r.json()

    # Alpha Vantage "not data" shapes
    info = stock_data.get("Information")
    note = stock_data.get("Note")
    err = stock_data.get("Error Message")

    if info or note or err:
        print("Alpha Vantage problem:", info or note or err)
        return None

    ts = stock_data.get("Time Series (Daily)")
    if not ts:
        print("Alpha Vantage unexpected response keys:", list(stock_data.keys()))
        return None

    # latest two trading days
    dates = sorted(ts.keys(), reverse=True)[:2]
    if len(dates) < 2:
        print("Not enough daily data returned.")
        return None

    latest, prev = dates
    latest_close = float(ts[latest]["4. close"])
    prev_close = float(ts[prev]["4. close"])

    pct_change = (latest_close - prev_close) / prev_close * 100
    return pct_change


def get_top_3_articles_with_descriptions() -> list[dict]:
    """Fetch news and return up to 3 article dicts that have title and description."""
    params = {
        "qInTitle": "Tesla OR TSLA",
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 20,  # fetch extra so we can filter out missing descriptions
        "apiKey": config.NEWS_API_KEY,
    }

    r = requests.get(NEWS_ENDPOINT, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    articles = data.get("articles") or []
    selected = []

    for a in articles:
        title = a.get("title")
        desc = a.get("description")

        # We only want description, nothing else (no content fallback)
        if title and desc:
            selected.append(a)

        if len(selected) == 3:
            break

    return selected


def main():
    pct_change = get_pct_change_or_none()

    # If rate-limited, you can either:
    # - stop, or
    # - use a dummy value for testing SMS
    if pct_change is None:
        pct_change = 0.50
        print(f"Skipping stock calculation due to API limits. Using pct_change={pct_change:.2f}% for testing.")

    arrow = "🔺" if pct_change > 0 else "🔻"
    pct_str = f"{abs(pct_change):.2f}%"

    articles = get_top_3_articles_with_descriptions()
    if not articles:
        print("No suitable articles found (no descriptions).")
        return

    client = Client(config.sms_account_sid, config.auth_token)

    for a in articles:
        headline = clamp(a.get("title", "No title"), 80)
        brief = clamp(a.get("description", "No brief available."), 120)

        message_text = (
            f"{STOCK}: {arrow}{pct_str}\n"
            f"Headline: {headline}\n"
            # f"Brief: {brief}"
        )

        msg = client.messages.create(
            body=message_text,
            from_=config.from_,
            to=config.to,
        )
        
        import time
        last = None
        for _ in range(15):
            m = client.messages(msg.sid).fetch()
            if m.status != last:
                print("status:", m.status, "error_code:", m.error_code, "error_message:", m.error_message)
                last = m.status
            if m.status in ("delivered", "failed", "undelivered"):
                break
            time.sleep(1)


        print("Sent:", msg.sid, "status:", msg.status)


if __name__ == "__main__":
    main()


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required
to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

