import requests
from send_email import send_email

api_key = "18b05ed1f9f1448e92946cc428595f88/"
url = ("https://newsapi.org/v2/top-headlines?sources="
       "techcrunch&apiKey=18b05ed1f9f1448e92946cc428595f88")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

body = ""
# Access content title and description and send email
for article in content["articles"]:
    body = body + article['title'] + "\n" + article['description'] + 2*'\n'

body = body.encode("utf-8")
send_email(message=body)
