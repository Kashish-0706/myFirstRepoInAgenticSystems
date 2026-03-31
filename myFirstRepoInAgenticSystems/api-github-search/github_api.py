import requests
url="https://api.github.com/search/repositories"
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 5
}


response = requests.get(url, params = params)
data = response.json()

 #Output the names and URLs of the top 5 repositories
for item in data['items']:  
    print(f"Name: {item['name']}, Stars: {item['stargazers_count']}")     
