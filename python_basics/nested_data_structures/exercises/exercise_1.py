# Iterate through the list so that if the character ‘m’ is in the string, then it should be added to a new list called m_list. 
# Hint: Because this isn’t just a list of lists, think about what type of object you want your data to be stored in.
# Conditionals may help you.
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
m_list = []
for item in d :
    if isinstance(item,str):
        if 'm' in item:
            m_list.append(item)
    elif isinstance(item,list):
        for word in item:
            if isinstance(word,str):
                if 'm' in word:
                    m_list.append(word)
            elif isinstance(word,list):
                for new_word in word:
                    if 'm' in new_word:
                        m_list.append(new_word)
print(m_list)                                
