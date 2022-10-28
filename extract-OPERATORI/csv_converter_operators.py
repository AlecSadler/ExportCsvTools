'''
    Instructions:
    open terminal and type python3 json-to-csv.py <<filename.json>>
'''

import json
import csv
import sys

csv.field_size_limit(sys.maxsize)

# open input and output files
try:
    with open(sys.argv[1]) as json_file:
        to_convert = json.load(json_file)

    buf_file = open('export-operatori.csv', 'w')

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
field_user = []
field_name = []
field_lastname = []
field_email = []
field_codstrut = []
field_piva = []
field_ragsoc = []
field_address = []
field_nomesch = []
field_localita = []
field_comune = []
field_tipologia = []
field_cell = []
field_phone = []
field_telatt = []
field_ambito = []
field_prov = []
field_site = []
field_twitter = []
field_facebook = []
field_youtube = []
field_insta = []
field_cf = []
field_nomeprof = []
field_nomeatt = []
field_expire = []
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
    field_created.append(a['DataCreazione'])
    field_ragsoc.append(a['RagioneSociale'])
    field_piva.append(a['PartitaIVA'])
    field_address.append(a['Address'])
    field_nomesch.append(a['NomeSuScheda'])
    field_localita.append(a['Localita'])
    field_comune.append(a['Comune'])
    field_tipologia.append(a['Tipologia'])
    field_cell.append(a['Cellulare'])
    field_phone.append(a['Telefono'])
    field_telatt.append(a['TelefonoAttivita'])
    field_ambito.append(a['Ambito'])
    field_prov.append(a['Provincia'])
    field_codstrut.append(a['CodiceStruttura'])
    field_site.append(a['SitoWeb'])
    field_twitter.append(a['Twitter'])
    field_facebook.append(a['Facebook'])
    field_youtube.append(a['YouTube'])
    field_insta.append(a['Instagram'])
    field_cf.append(a['CodiceFiscale'])
    field_nomeprof.append(a['NomeProfilo'])
    field_nomeatt.append(a['NomeAttivita'])
    field_expire.append(a['Scadenza'])
    field_eventi.append(a['Eventi'])
    field_offerte.append(a['Offerte'])
    field_idee.append(a['Idee'])
    field_ricette.append(a['Ricette'])
    field_attrazioni.append(a['Attrazioni'])
    field_itinerari.append(a['Itinerari'])
    field_bike.append(a['ItinerariBike'])

print('*\n*\n*')

# headers
csv_creator.writerow(['username', 'Nome', 'Cognome', 'Email', 'DataCreazione', 'SitoWeb', 'Twitter', 'Facebook', 'YouTube', 'Instagram', 'RagioneSociale', 'NomeScheda', 'NomeProfilo', 'NomeAttivita', 'Indirizzo', 'Localita', 'Comune', 'Provincia', 'Ambito', 'Cellulare', 'Telefono', 'TelefonoAttivita', 'Tipologia', 'PartitaIva', 'CodiceFiscale', 'CodiceStruttura', 'Scadenza', 'Eventi', 'Offerte', 'Idee', 'Ricette', 'Attrazioni', 'Itinerari', 'ItinerariBike'])

# writing records
for i in range(0, len(assets)):
    row = []

    row.append(field_user[i])
    row.append(field_name[i])
    row.append(field_lastname[i])
    row.append(field_email[i])
    row.append(field_created[i])
    row.append(field_site[i])
    row.append(field_twitter[i])
    row.append(field_facebook[i])
    row.append(field_youtube[i])
    row.append(field_insta[i])
    row.append(field_ragsoc[i])
    row.append(field_nomesch[i])
    row.append(field_nomeprof[i])
    row.append(field_nomeatt[i])
    row.append(field_address[i])
    row.append(field_localita[i])
    row.append(field_comune[i])
    row.append(field_prov[i])
    row.append(field_ambito[i])
    row.append(field_cell[i])
    row.append(field_phone[i])
    row.append(field_telatt[i])
    row.append(field_tipologia[i])
    row.append(field_piva[i])
    row.append(field_cf[i])
    row.append(field_codstrut[i])
    row.append(field_expire[i])
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
