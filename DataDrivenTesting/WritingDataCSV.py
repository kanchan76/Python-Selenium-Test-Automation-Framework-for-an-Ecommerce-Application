import csv

fields = ['credential','emailid','password']

rows = [[True,'kanchansahu7696@gmail.com','avactis'],
        [False,'kanchansahu766@gmail.com','avactis'],
        [False,'kanchansahu7696@gmail.com','avacis'],
        ]

filename = 'ConfigData.csv'

with open(filename,'w') as csvfile:
    writer = csv.writer(csvfile)

    # writing headers (field names)
    writer.writerow(fields)

    # writing data rows
    writer.writerows(rows)