from db import myconnection, mycursor
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
        postcode = content[0]
        floodRisk = content[1]
        if content[2] == '\\N':
            riskDate = ''
        else:
            riskDate = content[2]
        latitude = content[3]
        longitude = content[4]

        #if riskLevel != 'None': #gets any at risk of flooding
            #print(content)
        print(content)

        #mycursor.execute("INSERT INTO location (postcode, latitude, longitude, floodRisk, riskDate) VALUES ('"+postcode+"', '"+latitude+"', '"+longitude+"', '"+floodRisk+"', '"+riskDate+"') ")
        #print("INSERT INTO location (postcode, latitude, longitude, floodRisk, riskDate) VALUES ('"+postcode+"', '"+latitude+"', '"+longitude+"', '"+floodRisk+"', '"+riskDate+"') ")

        sql = "INSERT INTO location (postcode, latitude, longitude, floodRisk, riskDate) VALUES (%s, %s, %s, %s, %s)"
        val = (postcode, latitude, longitude, floodRisk, riskDate)
        mycursor.execute(sql, val)
        myconnection.commit()
        print("Inserted "+postcode)
        
    


#attribution required
#Contains Environment Agency data licensed under the Open Government Licence v3.0 (http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).