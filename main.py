import requests
from send_email import send_email
from datetime import datetime
import os

now = datetime.now()

current_month = now.month

modified = now.replace(month=current_month-1)

date = modified.strftime("%Y-%m-%d")

topic = "techCrunch"
language = "en"

api_key = os.getenv("news_api")

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch" \
      f"&from={date}" \
      "sortBy=publishedAt" \
      f"&apiKey={api_key}" \
       f"&language={language}"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

body = "Subject: Today's News" + '\n'

# Access content title and description and send email
for article in content["articles"][:20]:
    body = (body + '\n' + article['title'] + '\n'
            + article['description'] + '\n' + article['url'] + 2 * '\n')

body = body.encode("utf-8")
send_email(message=body)
