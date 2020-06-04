from db import myconnection, mycursor, conn
from flask import Flask, url_for, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

#read
@app.route('/floodRisk/<string:postcode>', methods = ['GET'])
def get_floodRisk(postcode):
    sql = "SELECT postcode, latitude, longitude, floodRisk, riskDate FROM location WHERE replace(postcode, ' ', '') = %s LIMIT %s"
    val = (postcode.replace(" ", ""), 1)
    print(val)
    mycursor.execute(sql, val)   
    try:
        rows = mycursor.fetchall()
        results = len(rows) 
        if results > 0:
            row = rows[0]
            postcode, latitude, longitude, floodRisk, riskDate = row[0], row[1], row[2], row[3], row[4]
            message = "Total number of rows is: "+str(mycursor.rowcount)
            returnVars = jsonify(postcode=postcode, message=message, latitude=latitude, longitude=longitude, floodRisk=floodRisk, riskDate=riskDate)
            status = 200
        else:
            message = "Total number of rows is: "+str(mycursor.rowcount)
            returnVars = jsonify(postcode=postcode, message=message)
            status = 404
    except conn.Error as error:
        message = "Failed to get record from MySQL table: {}".format(error)
        returnVars = jsonify(postcode=postcode, message=message)
        status = 404
    return returnVars, status

#read
@app.route('/searchPostcode/<string:postcodeText>', methods = ['GET'])
def get_postcode(postcodeText):
    sql = "SELECT postcode FROM location WHERE replace(postcode, ' ', '') LIKE %s LIMIT %s"
    val = ('%'+postcodeText.replace(" ", "")+'%', 100)
    print(val)
    mycursor.execute(sql, val)   
    try:
        rows = mycursor.fetchall()
        if len(rows) > 0:
            recordDictionary = {}
            num=0
            for row in rows:
                recordDictionary[num] =  row[0] 
                print(row[0], num)
                num=num+1
            records = json.dumps(recordDictionary)
            records = records.replace("\\", "")
            message = "Total number of rows is: "+str(mycursor.rowcount)
            returnVars = jsonify(postcodeSearch=postcodeText, message=message, records=recordDictionary)
            status = 200
        else:
            message = "Total number of rows is: "+str(mycursor.rowcount)
            returnVars = jsonify(postcodeSearch=postcodeText, message=message)
            status = 404
    except conn.Error as error:
        message = "Failed to get records from MySQL table: {}".format(error)
        returnVars = jsonify(postcodeSearch=postcodeText, message=message)
        status = 404
    return returnVars, status

# run app
if __name__ == '__main__':
    app.run(debug=True)
