import json
from xml.dom import minidom

PATH = "output/"

def write_to_xml(data, fileName):
  dom = minidom.parseString(data)
  pretty_xml = dom.toprettyxml()

  with open(f"{PATH}{fileName}.xml", "w", encoding="utf-8") as f: 
    f.write(pretty_xml) 

  print(f"XML file '{fileName}' has been created.")

def write_to_json(data, fileName):
  with open(f"{PATH}{fileName}.json", "w", encoding="utf-8") as f: 
    json.dump(json.loads(data), f, indent=4, ensure_ascii=False)
  
  print(f"JSON file '{fileName}' has been created.")