"""
This python script finds all files in ip_files directory and its sub directories.
ip_files directory must be located at same level as this script file and
prints in sorted order all valid ip addresses
"""
from pathlib import Path
import re

ip_candidates = []
text_content = ""

def find_ip_in_text(text):
    return re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", text)

def find_all_ip_in_dir(dir_name):
    entries = Path(dir_name)
    for entry in entries.iterdir():
       if entry.is_file():
           with open(entry) as f:
              textcontent = f.read()
              ip_candidates.extend(find_ip_in_text(textcontent))
       elif entry.is_dir():
           find_all_ip_in_dir(entry)

find_all_ip_in_dir('ip_files')

for ip in sorted(ip_candidates):
    print(ip)
