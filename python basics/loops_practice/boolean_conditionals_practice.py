# percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
# resps = []
# for i in percent_rain:
#     if( i > 90):
#         resps.append("Bring an umbrella.")
#     elif(i>80):
#         resps.append("Good for the flowers?")
#     elif(i>50):
#         resps.append("Watch out for clouds!")
#     else:
#         resps.append("Nice day!")        

# print(resps)

#QS---2
# ---------------------------------
#For each string in the list words, find the number of characters in the string. 
# If the number of characters in the string is greater than 3, add 1 to the variable num_words,
# so that num_words should end up with the total number of words with more than 3 characters.



# words = ["water", "chair", "pen", "basket", "hi", "car"]
# num_words = 0
# for word in words:
#     if len(word) > 3:
#         num_words += 1
# print(num_words)        


#-------------------------------------------------------------
#QS3-- 
# For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. 
# Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_list = []

for word in words:
    if ( word.endswith("e")):
        past_list.append(word + "d")
    else:
        past_list.append(word + "ed")
print(past_list)            
    

       