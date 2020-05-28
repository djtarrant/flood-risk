from db import mycursor
import csv

#mycursor.execute("SHOW TABLES")

#vars
fname = 'open_flood_risk_by_postcode.csv'
floodRiskData = []

# get a sample of data
with open(fname, 'r') as f:
    for lnum, line in enumerate(f):
        if lnum > 10:
            break
        print(line[:-1])

#get the number of rows
with open(fname, 'r') as f:
    print( sum(1 for line in f) )

#with open(fname, 'r') as f:
    #reader = csv.DictReader(f)
    #for row in reader:
        #floodRiskData.append(row)

#for dataLine in floodRiskData:
    #print(dataLine)


