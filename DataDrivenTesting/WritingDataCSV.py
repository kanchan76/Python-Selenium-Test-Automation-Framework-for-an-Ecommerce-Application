import csv

fields = ['emailid','password']

rows = [['kanchansahu7696@gmail.com','avactis'],
       ['kanchansahu766@gmail.com','avactis'],
       ['kanchansahu7696@gmail.com','avacis'],
       ]

filename = 'ConfigData.csv'

with open(filename,'w') as csvfile:
    writer = csv.writer(csvfile)

    # writing headers (field names)
    writer.writerow(fields)

    # writing data rows
    writer.writerows(rows)