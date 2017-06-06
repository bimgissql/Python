
import pymongo
from pymongo import MongoClient

import yaml

# Get database connection information from YML file
with open("mongodb.yml", 'r') as stream:
    config = yaml.load(stream)

# Parse connection data	
mdbhost = config[':host'] 
mdbport = config[':port']
mdbuser = config[':user']
mdbpassw = config[':password']

# Show information
print('Connect to MongoDB database')
print('MongoDB server   :', mdbhost)
print('MongoDB port     :', str(mdbport))

# connect to database
conn = MongoClient(mdbhost, mdbport)

db = conn.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']

