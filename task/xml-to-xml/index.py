import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('AUTO550DUAL_AU-AU.xml')
root = tree.getroot()

product = ET.Element('product', attrib={
    'language': 'au',
    'mpn': 'AA001550',
    'manufacturer_id': '262'
})

basic_info = ET.SubElement(product, 'basic_information', attrib={'md5_hash': ''})

ET.SubElement(basic_info, 'title').text = root.findtext('ProductName')
ET.SubElement(basic_info, 'description').text = root.findtext('IntroDescription')


mpns = ET.SubElement(basic_info, 'mpns')
for mpn in root.findall('ProductMPN'):
    ET.SubElement(mpns, 'mpn').text = mpn.text


eans = ET.SubElement(basic_info, 'eans')
ET.SubElement(eans, 'ean').text = root.findtext('ProductEAN')


cats = ET.SubElement(basic_info, 'categories')
ET.SubElement(cats, 'category').text = root.findtext('CategoryName')


features = ET.SubElement(product, 'features', attrib={'md5_hash': ''})
for idx, feat in enumerate(root.findall('Feature'), start=1):
    feature = ET.SubElement(features, 'feature', attrib={
        'order': str(idx),
        'asset_order': str(idx),
        'type': 'Feature',
        'section_title': feat.findtext('FeatureName'),
        'brand_style': '_feature_'
    })
    ET.SubElement(feature, 'title').text = feat.findtext('FeatureName')
    ET.SubElement(feature, 'description').text = feat.findtext('FeatureDescription')
    ET.SubElement(feature, 'image', attrib={
        'type': 'Embeded',
        'url': feat.findtext('FeatureImgUrl'),
        'title': '',
        'description': '',
        'brand_style': 'featureimage'
    })


ET.SubElement(features, 'feature', attrib={
    'order': str(idx + 1),
    'asset_order': str(idx + 1),
    'type': 'Feature',
    'section_title': 'Overview',
    'brand_style': '_overview_'
})
overview = features[-1]
ET.SubElement(overview, 'title').text = root.findtext('Overview')
ET.SubElement(overview, 'description').text = root.findtext('Overview')


specs = ET.SubElement(product, 'specifications', attrib={'md5_hash': ''})
spec_idx = 1
for topic in root.findall('Specs/SpecTopic'):
    for item in topic.findall('item'):
        ET.SubElement(specs, 'specification', attrib={
            'order': str(spec_idx),
            'asset_order': str(spec_idx),
            'type': 'Key Specification',
            'section_title': topic.attrib.get('name'),
            'title': item.findtext('itemDescription'),
            'specification_description': item.findtext('itemDescription'),
            'specification_value': item.findtext('itemDescription'),
            'brand_style': f"AA001550_au_spec_{spec_idx}"
        })
        spec_idx += 1

for idx, item in enumerate(root.findall('InTheBox/ITBTopic/item'), start=1):
    ET.SubElement(features, 'feature', attrib={
        'order': str(len(features) + idx),
        'asset_order': str(len(features) + idx),
        'type': 'Feature',
        'section_title': 'Package Contents',
        'brand_style': '_in_box_feature_'
    })
    pkg = features[-1]
    ET.SubElement(pkg, 'title').text = 'Package Contents'
    ET.SubElement(pkg, 'description').text = item.findtext('itemDescription')


images = ET.SubElement(product, 'images', attrib={'md5_hash': ''})
for idx, asset in enumerate(root.findall('ProductGallery/Asset'), start=1):
    ET.SubElement(images, 'image', attrib={
        'order': str(idx),
        'title': '',
        'type': 'OTHER',
        'url': asset.text.strip(),
        'description': 'Product Image',
        'brand_style': f"AA001550_au_image_{idx}"
    })

#output file formate
def prettify(elem):
    return minidom.parseString(ET.tostring(elem)).toprettyxml(indent="  ")

with open("newfile_converted.xml", "w", encoding="utf-8") as f:
    f.write(prettify(product))


print("you xml file was successfully converted as new xml file with a name of newfile_converted.xml")


