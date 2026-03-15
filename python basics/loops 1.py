list=[12,24,36,48,60,72,84,96,108,120]

x=96

i=0
while i<len(list):
    if(list[i]==x):
     print("found at index:", i)
     break
    else:
       print("finding.....")
       i+=1

print("END OF LOOP---") 
      