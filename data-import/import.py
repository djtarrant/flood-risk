from db import mycursor
import csv

#mycursor.execute("SHOW TABLES")

#vars
fname = 'open_flood_risk_by_postcode.csv'
included_cols = [0, 2, 4, 8, 9]

# get a sample of data
#with open(fname, 'r') as f:
    #for lnum, line in enumerate(f):
        #if lnum > 100:
            #break
        #print(line[:-1])

#get the number of rows
#with open(fname, 'r') as f:
    #print( sum(1 for line in f) )

#parse csv
with open(fname, 'r') as fp:
    reader = csv.reader(fp, delimiter=",")
    for row in reader:
        content = list(row[i] for i in included_cols)
        if content[1] != 'None': #gets any at risk of flooding
            print(content)
    


#attribution required
#Contains Environment Agency data licensed under the Open Government Licence v3.0 (http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).