import xmltodict

with open('sample.xml') as file:
    res = xmltodict.parse(file.read())

print(res['data']['country'][0]['rank'])
