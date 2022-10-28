'''
    Instructions:
    open terminal and type python3 json-to-csv.py <<namefile.json>>
'''

import json
import csv
import sys

csv.field_size_limit(sys.maxsize)

# open input and output files
try:
    with open(sys.argv[1]) as json_file:
        to_convert = json.load(json_file)

    buf_file = open('export-contents.csv', 'w')

except OSError:
    print("Error parsing file!")
    sys.exit(1)

# init csv writer
DELIMITER = '$'
csv_creator = csv.writer(buf_file, delimiter = DELIMITER)
print(f'Used separator: {DELIMITER}')

# select which part of json to export
assets = to_convert['response']['docs']

# fields selection
field_title = []
field_creator = []
field_path = []
field_tema = []
field_type = []

for a in assets:
    field_title.append(a['Title_dprop'])
    field_creator.append(a['userCreated'])
    field_path.append(a['path'])
    try:
    	field_tema.append(a['tema_it_lower'])
    except:
    	field_tema.append('N/A')

    field_type.append(a['type'])

print('*\n*\n*')

# headers
csv_creator.writerow(['Titolo', 'Autore', 'Path', 'Tema', 'Tipo'])

# writing records
for i in range(0, len(assets)):
    row = []

    row.append(field_title[i])
    row.append(field_creator[i])
    row.append(field_path[i])
    row.append(field_tema[i])
    row.append(field_type[i])

    csv_creator.writerow(row)

print(f'Exported {i + 1} records')
buf_file.close()
