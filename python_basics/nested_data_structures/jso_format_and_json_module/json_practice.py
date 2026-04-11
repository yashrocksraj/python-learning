import json
# How to use .loads function in json module
text = '{"count": 3, "items": [10, 20, 30]}'

info1 = json.loads(text)
info2 = json.loads(text)

print(text[2])
print(info1["count"])
# print(text["count"]) # error will be printed


json_text = """  [
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 25}
]  """

people = json.loads(json_text)
print(people[1]["name"])
print(people[0]["name"])

# How to use .dumps function in json module
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
