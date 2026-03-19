# Olympics Analyser - Project 1

import csv
with open("python_basics/program_files/olympics.txt","r") as f:
   reader = csv.DictReader(f)
   data = list(reader)
   # Count Total Medals
   medals = {}
   for row in data:
      medal = row["Medal"]
      if medal not in medals:
         medals[medal] = 0
      medals[medal]+=1    

   total_medals = 0   
   
   for key in sorted(medals):
      if key != "NA":
       total_medals = total_medals + medals[key]
       print(f"{key}:{medals[key]}")  
   
   print(f"Total medals:{total_medals}")
   
   # Most Frequent medal
   
   max_medal = None
   max_value = 0
   for key in medals:
      if key != "NA":
         if medals[key] > max_value:
            max_value = medals[key]
            max_medal = key
   print(f"most frequent medal is : {max_medal} , value: {max_value}")

   
   # Count Medals Per Player
   players = {}
   for row in data:
      medal = row["Medal"]
      
      if medal != "NA":
         player = row["Name"]

         if player not in players:
            players[player] = 0
         players[player] += 1  
   for player in players:
      print(f"Medals of {player} is: {players[player]}")
      
   

   # Top most Player
   top_player = None
   top_player_value = 0
   for key in sorted(players):
      if players[key] > top_player_value:
         top_player_value = players[key]
         top_player = key       
   print(f"Top player of Olympics is:{top_player} !!!!")

   # Medals Won by each Country
   countries = {}
   for row in data:
      medal = row["Medal"]
      
      if medal != "NA":
         country = row["Team"]
         countries[country] = countries.get(country,0) + 1    
   for country in countries:
     print(f"Medals won by {country} is: {countries[country]}")  
    
         
         


      


      


