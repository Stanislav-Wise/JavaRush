import requests

article_title = "Python"
api_url = "https://ru.wikipedia.org/w/api.php"

# api.google.com
# google.com/api

params = {
    "action": "query",
    "format": "json",
    "prop": "extracts|pageimages",
    "explaintext": 1,
    "titles": article_title,
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data["query"]["pages"]['2705']['extract'])
    # # page_id = next(iter(data["query"]["pages"].keys()))
    # print(data["query"]["pages"][page_id]["extract"])
    # print(data["query"]["pages"][page_id]["title"])
    # print(data["query"]["pages"][page_id]["pageid"])
    # print(data["query"]["pages"][page_id]["thumbnail"]["source"])
else:
    print(f"Произошла ошибка: {response.status_code}")