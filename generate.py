import dicttoxml
import json
from xml.dom.minidom import parseString
import yaml

from podcast_categories_list import categories

BASE_NAME = "podcast_categories_list"

def write_format(file_extention, content):
    with open(BASE_NAME + file_extention, 'w') as f:
        f.write(content)

write_format(".json", json.dumps(categories, indent=4))
write_format(".yaml", yaml.dump(categories))

data = dicttoxml.dicttoxml(categories)
data = parseString(data)
data = data.toprettyxml()
write_format(".xml", data)


