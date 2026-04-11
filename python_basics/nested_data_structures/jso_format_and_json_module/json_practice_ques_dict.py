# Below, we have a grocery store's inventory of all items in stock and their sale prices. 
# Answer the following questions about the inventory, and help a buyer get all items on their grocery list.
#  1.What is the price of an avocado? Can you print it using one line of code (no hardcoding)?
#  2.How many milk cartons are in stock? Print using one line of code.
#  3.Add a new item Celery to the inventory, which costs $1.25, and there are 15 bunches in stock.
#  4.Print each item in the inventory in the following format:
#      Apples
#           Price: 1.5
#           Stock: 10
#      Bananas
#          Price: 1.0
#          Stock: 12
#        ```
#  5. A buyer comes to the grocery story with a `groceryList`. Complete the function definition we started in the cell below. 
#     It should check the inventory dictionary and the grocery list, and print for the buyer which items from their grocery list are available 
#     and which are not, and the total cost of available items. Update the inventory to reflect the sale of these items. 
#     For example, if 
#         - the `inventory` was 
#                         ```{"Cherries": {"Price": 2.00, "Stock": 5}, "Strawberries": {"Price": 3.50, "Stock": 10}}```
#         - the `groceryList` was `["Cherries", "Strawberries", "Apples"]`
#         - the output will be:
#                      availableItems = ['Cherries', 'Strawberries'] unavailableItems = ['Apples'] totalCost = 5.5 ```

import json
inventory = {"Apples": {"Price": 1.50, "Stock": 10},
             "Bananas": {"Price": 1.00, "Stock": 12},
             "Eggs": {"Price": 3.00, "Stock": 7},
             "Milk": {"Price": 3.50, "Stock": 20},
             "Oranges": {"Price": 0.75, "Stock": 35},
             "Avocados": {"Price": 2.50, "Stock": 5}
            }
print(inventory['Avocados']['Price']) #Ans 1
print(inventory['Milk']['Stock']) # Ans 2
inventory['Celery'] = {"Price":1.25,"Stock":15} # Ans 3
print(inventory)
inventory_string = json.dumps(inventory , indent = 4) # Ans 4
print(inventory_string)
 # Ans 5
def process_shopping_list(inventory, groceryList=["Apples", "Eggs", "Milk", "Avocados", "Broccoli", "Celery", "Cherries"]):
    total_cost = 0
    availableItems = []
    unavailableItems = []
    for item in groceryList:
        if item in inventory.keys():
            availableItems.append(item)
            total_cost = total_cost + inventory[item]["Price"]
        else:
            unavailableItems.append(item)
    return ("availableItems :",availableItems,"unavailableItems :",unavailableItems,"total_cost :", total_cost)
        
print(process_shopping_list(inventory))        

