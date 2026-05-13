import sys

file_path = r'c:\Users\ENG  AHMED TAG\Documents\tageldien\gas_mixtures_enhanced.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = lines[:1081] + lines[1473:1669] + lines[1129:1473] + lines[1669:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_content)

print('File updated successfully.')
