import os
import re
import json

class Cell:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.content = []
        self.kid = set()
        self.parent = set()
        
    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "kid": list(self.kid),    # Convert set to list for JSON serialization
            "parent": list(self.parent)  # Convert set to list
        }


cellLib = {}

def readMarkdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_name = file_path.split("/")[-1].replace(".md", "")
        if file_name not in cellLib:
            cellLib[file_name] = Cell(file_name, file_path.replace('../', './')) 

        cellLib[file_name].content = f.read()

        links = re.findall(r'\]\((.*?\.md)\)', cellLib[file_name].content)
        define_section = re.search(r'##\s*Define(.*?)(## \w+|$)', cellLib[file_name].content, re.DOTALL)
        define_section = define_section.group(1).strip() if define_section else None

        
        for link in links:
            name_tmp = link.split("/")[-1].replace(".md", "")
            if name_tmp not in cellLib:
                cellLib[name_tmp] = Cell(name_tmp, link.replace('./', './notes/'))

            if define_section and link in define_section:
                cellLib[file_name].parent.add(name_tmp)
                cellLib[name_tmp].kid.add(file_name)
            else:
                cellLib[file_name].kid.add(name_tmp)
                cellLib[name_tmp].parent.add(file_name)

def readLib(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                readMarkdown(file_path)

    serializable_cellLib = {key: cell.to_dict() for key, cell in cellLib.items()}
    json_string = json.dumps(serializable_cellLib)
    with open("cellLib.json", "w") as file:
        file.write(json_string)

