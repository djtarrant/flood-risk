# flood-risk
Flood Risk map of UK postcodes

# data import
Rename db.example.py to db.py
Adjust the db credentials
Flood risk data CSV acquired from getthedata.co.uk
Check included_cols correspond to the CSV data
Run import.py to import data to the db

# running in docker
build the docker image:
docker build -t flaskapp:latest .

run the docker image on 127.0.0.1:5000 (mapped from 0.0.0.0):
docker run -it -p 5000:5000 flaskapp

