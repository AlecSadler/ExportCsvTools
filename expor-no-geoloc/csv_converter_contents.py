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

    buf_file = open('export-nogeo.csv', 'w')

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
field_type = []
field_id = []
field_link = []

for a in assets:
    field_title.append(a['Title_dprop'])
    field_creator.append(a['userCreated'])
    field_path.append(a['path'])
    field_type.append(a['type'])
    field_id.append(a['id'])
    field_link.append('visittuscany.com' + a['link'])

print('*\n*\n*')

# headers
csv_creator.writerow(['Titolo', 'Autore', 'Path', 'Link', 'id', 'Tipo'])

# writing records
for i in range(0, len(assets)):
    row = []

    row.append(field_title[i])
    row.append(field_creator[i])
    row.append(field_path[i])
    row.append(field_link[i])
    row.append(field_id[i])
    row.append(field_type[i])

    csv_creator.writerow(row)

print(f'Exported {i + 1} records')
buf_file.close()
