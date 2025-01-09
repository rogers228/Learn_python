import json

#建立
data = {'request':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
print(data)

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

print('ok')

#讀取
with open('data.txt') as json_file:
    data = json.load(json_file)['request'][0]
print(data['name'])
print(data['website'])
print(data['from'])