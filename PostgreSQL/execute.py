import psycopg2
import yaml

# Get database connection information from YML file
with open("database.yml", 'r') as stream:
    config = yaml.load(stream)

# Parse connection data	
pghost = config[':host']
pgport = config[':port']
pgdb = config[':dbname']
pguser = config[':user']
pgpassw = config[':password']

# PostgreSQL connection pool
conn = 'host=' + pghost + ' port=' + str(pgport) + ' dbname=' + pgdb + ' user=' + pguser + ' password=' + pgpassw

# Connect to PostgreSQL database
db = psycopg2.connect(conn)

# Show information
print('Connect to PostgreSQL database')
print('PostgreSQL server   :', pghost)
print('PostgreSQL port     :', str(pgport))
print('PostgreSQL database :', pgdb)

# List of tables to show
tables = {'ifc.project', 'ifc.site', 'ifc.building', 'ifc.buildingstorey', 'ifc.space'}

# Print contents of tables
for t in tables:


  # Create cursor
  cursor = db.cursor()

  # Execute query
  cursor.execute('SELECT * FROM ' + t + ';')
 
  # print records
  print("----------------------------")
  print(t + ' table:')
  print("----------------------------")
  for record in cursor:
    print(record)

  # close cursor
  cursor.close()

  
