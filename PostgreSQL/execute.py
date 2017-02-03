import psycopg2

# PostgreSQL host server address
pghost = '192.168.55.172'

# PostgreSQL port number on host server
pgport = 5432

# PostgreSQL user
pguser = 'postgres'

# PostgreSQL password
pgpassw = 'password'

# Number of database on PostgreSQL server
pgdb = 'bimdb'

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

  