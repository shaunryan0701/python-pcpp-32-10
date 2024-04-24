import xml.etree.ElementTree as ET

tree = ET.parse('xml/books.xml')

root = tree.getroot()

for book in root.findall('book'):
    print(book.get('title'))