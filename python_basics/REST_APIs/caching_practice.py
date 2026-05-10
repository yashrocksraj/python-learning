# Simple Cache Dictionary
#cache = {}

# cache['apple'] = 'fruit'
# print(cache)

# # Simulate Cache
# cache = {}

# word = 'happy'

# if word in cache:
#     print("cache found")
# else:
#     print("Not Found")
#     cache[word] = ['sappy','snappy']    
# print(cache)    

# # Create fake API Cache
# cache ={}
# def get_a_word(word):
    
#     if word in cache:
#         print("cache found")
#         return cache[word]
#     else:
#         print("Calling fake API...")
#         fake_data =[
#             word + '1',
#             word + '2',
#             word + '3',
#         ]
#         cache[word] = fake_data
        
#         print("Data saved in cache")

#         return fake_data
# print(get_a_word('happy'))  

# print()

# print(get_a_word("happy"))


# -----Create Real API Cache-----

import requests

cache = {}

def get_a_word(word):

    if word in cache:
        print("Cache found")
        return cache[word]

    else:
        print("Calling real API...")

        url = "https://api.datamuse.com/words"

        response = requests.get(
            url,
            params={'rel_rhy': word}
        )

        data = response.json()
        sorted_data = sorted(data,key=lambda item:item['word'])

        words = [item['word'] for item in sorted_data]

        cache[word] = words

        print("Data saved in cache")
        return words


# print(get_a_word("happy"))
print()
# print(get_a_word("happy"))
# print(get_a_word('blue'))
print(get_a_word('blue'))
print('----------')
# get_a_word('blue')
print(get_a_word('blue'))
print("cache is :-")
print(cache)