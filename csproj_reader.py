from pathlib import Path

import csv    

import xml.etree.ElementTree as ET
import re
import os

def extract_from_directory(target_path):
    ret = []
    for csproj_path in Path(target_path).rglob("*.csproj"):
        ret.extend(extract_from_csproj(csproj_path))
    return ret
    
def extract_from_csproj(csproj_path):
    directory = os.path.dirname(csproj_path.absolute())

    root = ET.parse(csproj_path).getroot()
    namespace = re.match('\{.*\}', root.tag).group(0)
    
    ret = []
    for item in root.iter(namespace + 'Compile'):
        ret.append([directory + '\\' + item.attrib['Include']])

    return ret

def write_to_csv(file_list, path):
    file_list.sort(key=lambda v : v[0])
    with open(path, 'w', newline='') as fp:
        w = csv.writer(fp)
        w.writerows(file_list)
            