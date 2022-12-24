from tag_regex import tag_regex
from create_xml_tree import create_xml_tree

with open('test.xml', 'r') as f:
    xml_data = f.read()

print("----------- Q1 -----------")
tag = tag_regex(xml_data)
print(tag)

print("----------- Q2 -----------")
tree = create_xml_tree()
print(tree)

print("----------- Q3 -----------")
found_tags = tree.find('heading', type="Reminder")
print(found_tags[0])
