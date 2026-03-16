# Problem 1
# Count how many times each word appears
sentence = "python is good python is easy"
words = sentence.split()
word_count = {}
for word in words:
    count_word = sentence.count(word)
    word_count[word] =  count_word
print(word_count)    