import requests
cache = {}

def search_photos(tags):
    if tags in cache:
        print("Using cache...")
        return cache[tags]
    else:
        print('Calling API...')
        url ="https://api.flickr.com/services/rest/"
        params = {
        "method": "flickr.photos.search",
        "api_key": "YOUR_API_KEY",
        "tags": tags,
        "format": "json",
        "nojsoncallback": 1,
        "per_page": 5
    }

    response = requests.get(url,params=params)  
    data = response.json()
    cache[tags] = data  
    return data

data = search_photos("nature")

print(data)
