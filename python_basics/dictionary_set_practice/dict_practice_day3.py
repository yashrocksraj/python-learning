# Problem 1
# Create a dictionary called d that keeps track of all the characters in the string placement and 
# notes how many times each character was seen. 
# Then, find the key with the lowest value in this dictionary and assign that key to key_with_min_value.

# placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
# d ={}
# for ch in placement:
#     d[ch] = d.get(ch,0) + 1
# keys = list(d.keys())
# key_with_min_value = keys[0]
# for key in keys:
#     if d[key] < d[key_with_min_value]:
#         key_with_min_value = key
# print(keys)
# print(key_with_min_value)
#------------------#---------------------#

# Problem 2
# Create a dictionary called lett_d that keeps track of all of the characters in the string product
# and notes how many times each character was seen. 
# Then, find the key with the highest value in this dictionary and assign that key to key_with_max_value.

# product = "iphone and android phones"
# lett_d ={}
# for ch in product:
#     if ch not in lett_d:
#         lett_d[ch] = 0
#     lett_d[ch] = lett_d[ch] +1
# keys = list(lett_d.keys())
# max_value = keys[0]
# for key in keys:
#     if lett_d[key] > lett_d[max_value]:
#         max_value = key
# print(max_value)            
# print(lett_d[max_value])
#------------------#---------------------#

# Problem 3
# Write a program that finds the most used 7 letter word in Scarlet.txt

f = open('python_basics/program_files/scarlet.txt', 'r')
sentence = f.read().split()
#print(sentence)
words = {}
for word in sentence:
    if word not in words:
        words[word] = 0
    words[word] = words[word] + 1
max_word = ''
max_count = 0
for key in words:
    if len(key) == 7:
        if words[key] > max_count:
            max_count = words[key]
            max_word = key
print(max_count,max_word)