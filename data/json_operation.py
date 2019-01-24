import json

with open('sample.json', 'r') as file:
    result = json.load(file)

print(result)
