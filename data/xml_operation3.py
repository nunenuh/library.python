import lxml
from lxml import etree
from lxml import objectify

with open('sample.xml') as file:
    data = objectify.fromstring(file.read())

print(data.country[1].rank)

