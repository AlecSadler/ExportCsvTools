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

    buf_file = open('export-makegroups.csv', 'w')

except OSError:
    print("Error parsing file!")
    sys.exit(1)

# init csv writer
DELIMITER = '$'
csv_creator = csv.writer(buf_file, delimiter = DELIMITER)
print(f'Used separator: {DELIMITER}')

# select which part of json to export
assets = to_convert['data']['Users']

# fields selection
field_ragsoc = []
field_address = []
field_nomeaz = []
field_regionale = []
field_nomesch = []
field_localitadel = []
field_localita = []
field_comune = []
field_tipologia = []
field_cell = []
field_phone = []
field_ref = []
field_ambito = []
field_slug = []
field_email = []
field_prov = []
field_site = []
field_twitter = []
field_facebook = []
field_youtube = []
field_insta = []
field_expire = []
field_created = []

for a in assets:
    field_ragsoc.append(a['RagioneSociale'])
    field_address.append(a['Address'])
    field_nomeaz.append(a['NomeAzienda'])
    field_regionale.append(a['Regionale'])
    field_nomesch.append(a['NomeSuScheda'])
    field_localitadel.append(a['LocalitaDelega'])
    field_localita.append(a['Localita'])
    field_comune.append(a['Comune'])
    field_tipologia.append(a['Tipologia'])
    field_cell.append(a['Cellulare'])
    field_phone.append(a['Telefono'])
    field_ref.append(a['Referente'])
    field_ambito.append(a['Ambito'])
    field_slug.append(a['slug'])
    field_email.append(a['email'])
    field_prov.append(a['Provincia'])
    field_site.append(a['SitoWeb'])
    field_twitter.append(a['Twitter'])
    field_facebook.append(a['Facebook'])
    field_youtube.append(a['YouTube'])
    field_insta.append(a['Instagram'])
    field_expire.append(a['Scadenza'])
    field_created.append(a['DataCreazione'])


print('*\n*\n*')

# headers
csv_creator.writerow(['RagioneSociale', 'NomeAzienda', 'NomeSuScheda', 'SitoWeb', 'Twitter', 'Facebook', 'YouTube', 'Instagram', 'Slug', 'Indirizzo', 'LocalitaDelega', 'Localita', 'Comune', 'Provincia', 'Ambito', 'Regionale', 'Cellulare', 'Telefono', 'Email', 'Referente', 'Tipologia', 'Scadenza', 'DataCreazione'])

# writing records
for i in range(0, len(assets)):
    row = []

    row.append(field_ragsoc[i])
    row.append(field_nomeaz[i])
    row.append(field_nomesch[i])
    row.append(field_site[i])
    row.append(field_twitter[i])
    row.append(field_facebook[i])
    row.append(field_youtube[i])
    row.append(field_insta[i])
    row.append(field_slug[i])
    row.append(field_address[i])
    row.append(field_localitadel[i])
    row.append(field_localita[i])
    row.append(field_comune[i])
    row.append(field_prov[i])
    row.append(field_ambito[i])
    row.append(field_regionale[i])
    row.append(field_cell[i])
    row.append(field_phone[i])
    row.append(field_email[i])
    row.append(field_ref[i])
    row.append(field_tipologia[i])
    row.append(field_expire[i])
    row.append(field_created[i])

    csv_creator.writerow(row)

print(f'Exported {i + 1} records')
buf_file.close()
