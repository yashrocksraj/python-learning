import json
with open("C:\Python-learning\python_basics\program_files\itunes.txt","r") as file:
    content = file.read()
    #print(content)
    content_python = json.loads(content)
    #print(content_python.keys())
    trackid = []
    print(type(content_python['results']))
    print(len(content_python['results']))
    for i in range(len(content_python['results'])):
        if content_python['results'][i]['trackId'] not in trackid:
            trackid.append(content_python['results'][i]['trackId'])
    print(trackid)    
    
   
