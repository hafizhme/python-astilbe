f = open('input', 'r')

one  = f.readline()
rest = f.read()
print('one\n' + one)
print('rest\n' + rest)

f.close()

f = open('output', 'w')
f.write('Hello\n')
f.write('again\n')

f.close()

satu = input()
dua = input()

print(satu)
print(dua)

print()

import json

f = open('input_json', 'r')
js = json.load(f)
f.close()
print(js['name'])
