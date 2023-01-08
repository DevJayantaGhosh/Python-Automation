#!/usr/bin/env python3
import os

script_dir= os.path.dirname(__file__)
filePathForTs=os.path.join(script_dir,'./deploy/cli.ts')
filePathForJSON=os.path.join(script_dir,'./deploy/scr/pack.json')
print(filePathForTs)
print(filePathForJSON)
sprintNo="60"
spin="0"
versioModify='"version":"3.0.'+sprintNo+'.'+spin+'"'

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num-1] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

replace_line(filePathForJSON, 4, '"designation":"Software Engineer",\n')
replace_line(filePathForJSON, 6, '"Author":"JGhosh",\n')
replace_line(filePathForJSON, 7, versioModify+',\n')
replace_line(filePathForTs, 2, 'aplication:"My Package Manager"\n')

