import csv


data = [#['jmeno', 'vek', 'telefon'],
        ['Alice', '30', '+420603603603'],
        ['Bob', '25', '+420724724724']
        ]


with open('data3.csv', 'w', newline='\r\n') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)
