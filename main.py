import requests
from send_email import send_email

topic = "techcrunch"
api_key = "18b05ed1f9f1448e92946cc428595f88/"
url = ("https://newsapi.org/v2/top-headlines?sources"
       f"={topic}&apiKey=18b05ed1f9f1448e92946cc428595f88&language=en")

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
