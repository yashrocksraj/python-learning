# import json
# with open("C:\Python-learning\python_basics\program_files\itunes.txt","r") as file:
#     content = file.read()
#     #print(content)
#     content_python = json.loads(content)
#     #print(content_python.keys())
#     trackid = []
#     print(type(content_python['results']))
#     print(len(content_python['results']))
#     for i in range(len(content_python['results'])):
#         if content_python['results'][i]['trackId'] not in trackid:
#             trackid.append(content_python['results'][i]['trackId'])
#     print(trackid)    
    
   
# Practice REST APIs --

# 1.) Create:URL, params, requests.get(), Print: status_code and url

import requests

url = "https://api.datamuse.com/words"
params = {'ml':'happy'} 
# params = {'ml':'happy',
#           'max':5}
response = requests.get(url,params=params)
print(response.status_code)
print(response.url)
#print(response.text[:100])
data = response.json()
print(type(data))
print(data[0])

# 2.) Print firts 5 words
for info in data:
    print(info['word'])
    
# 3.) Sort words alphabetically
sorted_data = sorted(data,key=lambda info:info['word'])
for info in sorted_data:
    print(info['word'])





# 4.) print only words having more than 6 letters
for info in data:
    if len(info['word']) > 6:
        print(info['word'])    

# 5.) Print word and score together  
for info in data:
    print(info['word'],info['score'])


