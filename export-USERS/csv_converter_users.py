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

    buf_file = open('export-users.csv', 'w')

except OSError:
    print("Error parsing file!")
    sys.exit(1)

# init csv writer
DELIMITER = '$'
csv_creator = csv.writer(buf_file, delimiter = DELIMITER)
print(f'Used separator: {DELIMITER}')

# select which part of json to export
assets = to_convert['Users']

# fields selection
field_user = []
field_name = []
field_lastname = []
field_email = []
field_group = []
field_eventi = []
field_offerte = []
field_idee = []
field_ricette = []
field_attrazioni = []
field_itinerari = []
field_bike = []
field_created = []

for a in assets:
    field_user.append(a['Username'])
    field_name.append(a['Nome'])
    field_lastname.append(a['Cognome'])
    field_email.append(a['email'])
    field_group.append(a['Gruppo'])
    field_created.append(a['DataCreazione'])
    field_eventi.append(a['Eventi'])
    field_offerte.append(a['Offerte'])
    field_idee.append(a['Idee'])
    field_ricette.append(a['Ricette'])
    field_attrazioni.append(a['Attrazioni'])
    field_itinerari.append(a['Itinerari'])
    field_bike.append(a['ItinerariBike'])

print('*\n*\n*')

# headers
csv_creator.writerow(['Username', 'Gruppo', 'Nome', 'Cognome', 'Email', \
                      'DataCreazione', 'Eventi', 'Offerte', 'Idee', 'Ricette', \
                          'Attrazioni', 'Itinerari', 'ItinerariBike'])

# writing records
for i in range(0, len(assets)):
    row = []

    row.append(field_user[i])
    row.append(field_group[i])
    row.append(field_name[i])
    row.append(field_lastname[i])
    row.append(field_email[i])
    row.append(field_created[i])
    row.append(field_eventi[i])
    row.append(field_offerte[i])
    row.append(field_idee[i])
    row.append(field_ricette[i])
    row.append(field_attrazioni[i])
    row.append(field_itinerari[i])
    row.append(field_bike[i])

    csv_creator.writerow(row)

print(f'Exported {i + 1} records')
buf_file.close()
