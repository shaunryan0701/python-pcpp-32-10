import xml.etree.ElementTree as ET

root = ET.Element('shop')
category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})
products = [{
        'Good Morning Sunshine': ('cereals', 'OpenEDG Testing Service', 9.90, 'USD'),
        'Spaghetti Veganietto': ('pasta', 'Programmers Eat Pasta' , 16.48, 'EUR'),
        'Fantastic Almond Milk': ('beverages', 'Drinks4Coders Inc.' , 19.75, 'GBP')
        }]

for product in products:
    for key, value in product.items():
        prod = ET.SubElement(category, 'product', {'name': key})
        type = ET.SubElement(prod, 'type')
        type.text = value[0]
        producer = ET.SubElement(prod, 'producer')
        producer.text = value[1]
        price = ET.SubElement(prod, 'price')
        price.text = str(float(value[2]))
        currency = ET.SubElement(prod, 'currency')
        currency.text = value[3]

ET.dump(root)