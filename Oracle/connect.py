import cx_Oracle
import yaml

# Get database connection information from YML file
with open("oracle.yml", 'r') as stream:
    config = yaml.load(stream)

# Parse connection data	
host = config[':host'] 
port = config[':port']
sid = config[':sid']
user = config[':user']
password = config[':password']

# Show information
print('Connect to Oracle database')
print('Oracle server   :', host)
print('Oracle port     :', port)
print('Oracle SID      :', sid)

# Prepare DSN
dsnStr = cx_Oracle.makedsn(host, port, sid)
#print('Oracle DSN      :', dsnStr)

# Connect to the database
con = cx_Oracle.connect(user = user, password = password, dsn = dsnStr)

# Get Oracle version 
print('Oracle version  :', con.version)

# Close connection
con.close()
