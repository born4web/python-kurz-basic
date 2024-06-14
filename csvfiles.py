import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file, delimiter=';')
    for radek in reader:
        print(radek)


with open("data.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=';')
    for radek in reader:
        radek['vek'] = int(radek['vek'])
        radek['telefon'] = '+420' + radek['telefon'].strip()
        print(radek)

data = [#['jmeno', 'vek', 'telefon'],
        ['Alice', '30', '+420603603603'],
        ['Bob', '25', '+420724724724']
        ]


with open('data.csv', 'a') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)

fieldnames = ['jmeno', 'vek', 'telefon']
data_dict = [
    {'jmeno': 'Petr', 'vek': 52, 'telefon': '+420123456789'},
    {'jmeno': 'Honza', 'vek': 45, 'telefon': '+420987654321'},
    {'jmeno': 'Jana', 'vek': 32, 'telefon': '+420951852753'},
]

with open('data.csv', 'w') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dict)
