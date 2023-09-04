import requests

api_key = "18b05ed1f9f1448e92946cc428595f88/"
url = ("https://newsapi.org/v2/top-headlines?sources="
      "techcrunch&apiKey=18b05ed1f9f1448e92946cc428595f88")

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access content title and decription
for articles in content["articles"]:
    print(f"Title: {articles['title']}")
    print(f"Desc: {articles['description']}")