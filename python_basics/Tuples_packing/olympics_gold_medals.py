# Define a function to get number of gold medals won by each country and assign it to the list.


gold = {
    "USA": 31,
    "Great Britain": 19,
    "China": 19,
    "Germany": 13,
    "Russia": 12,
    "Japan": 10,
    "France": 8,
    "Italy": 8,
}
def get_num_medals(gold):
    num_medals = []
    for country,medals in gold.items():
        num_medals.append(medals)
    return num_medals  
num_medals = get_num_medals(gold)
    