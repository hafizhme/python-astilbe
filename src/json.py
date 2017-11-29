import json

f = open('input_json', 'r')

js = json.load(f)

f.close()

print(js['name'])
