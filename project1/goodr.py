import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "sf9H2SyVbPGVR1f7PMAg", "isbns": "9781632168146"})
print(res.json())