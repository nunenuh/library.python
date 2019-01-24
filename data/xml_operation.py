import xml.etree.ElementTree as ET
# import os

tree = ET.parse('sample.xml')
root = tree.getroot()
print(f'root.tag \t: {root.tag}')
print(f'root.attrib \t: {root.attrib}')


for child in root:
    if child.getchildren():
        for sub_child in child:
            if sub_child.text:
                print(sub_child.tag, sub_child.text)
            else:
                print(sub_child.tag, sub_child.attrib)
        print()
