# The nested dictionary, pokemon, shows the number of various Pokemon that each person has caught while playing Pokemon Go. 
# Find the total number of rattatas, dittos, and pidgeys caught and assign to the variables r, d, and p respectively. 
# Do not hardcode. Note: Be aware that not every trainer has caught a ditto.

pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}
# print(type(pokemon))
# print(pokemon.keys())
# print(type(pokemon['Trainer1']))
# print(pokemon['Trainer1'].keys())
r = 0
for trainer in pokemon:
    for pok_type in trainer:
        for pok in pok_type:
            if pok == 'rattatas':
                print(pok_type[pok])

                
                