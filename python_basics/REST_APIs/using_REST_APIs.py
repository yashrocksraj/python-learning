# import requests

# url = "https://api.datamuse.com/words"
# print(type(url))
# params = {
#     "rel_rhy" : "blue",
#     "max" : 10
# }

# response = requests.get(url,params=params)
# data = response.json()
# # print(type(response))
# # print(response)
# # print(type(data))
# # print(data)
# #data.sort(key=lambda item :item['word'])
# for item in data:
#     print(item['word'],item['score'])



# Create API function

import requests

def get_rhymes(word):
    url ="https://api.datamuse.com/words"


    params = {
        'rel_rhy' : word,
        "max" : 5
    }
    
    response = requests.get(url, params=params)

    data = response.json()

    for item in data:
        print(item["word"])

# get_rhymes('car')        

# Take user input
word = input("Enter word: ")

get_rhymes(word)