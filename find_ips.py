"""
This python script finds all files in directory ip_files located at same level as this script file and 
prints in sorted order all valid ip addresses
"""
from pathlib import Path
import re

ip_candidates = []

entries = Path('ip_files/')
for entry in entries.iterdir():
    if entry.is_file():
        with open(entry) as f:
            textcontent = f.read()
            ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", textcontent)

for ip in sorted(ip_candidates):
    print(ip)
