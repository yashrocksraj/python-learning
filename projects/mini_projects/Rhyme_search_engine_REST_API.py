import requests

cache = {}
def get_rhy_word(word):
    if word in cache:
        print('Using cache...')
        return cache[word]
    else:
        print('Calling api...')
        url = "https://api.datamuse.com/words"
        params ={'rel_rhy':word}
        response = requests.get(url,params=params)
        data = response.json()
        words = [item['word'] for item in sorted(data,key=lambda item:item['word'])]
        cache[word] = words
        return words 


print("Type 'done!' to end searching...")    

while True:

    user_input = input("Enter word: ")

    if user_input == "":
        print("Please enter a valid word")
        continue

    if user_input == "done!":
        print("Thanks for using the rhyme search engine!")
        break

    print(get_rhy_word(user_input))
