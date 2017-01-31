import redis

# Redis host server address
redishost = '192.168.55.181'

# Redis port number on host server
redisport = 6379

# Number of database on Redis server
redisdb = 0

# Name of IFC file to be imported
ifcfilename = "ifc.ifc"

# Redis connection pool
pool = redis.ConnectionPool(host=redishost, port=redisport, db=redisdb)

# Redis database
db = redis.Redis(connection_pool=pool)

# Open IFC file
ifcfile = open(ifcfilename)

# Show information
print('Import contents of IFC file to Redis database')
print('Redis server   :', redishost)
print('Redis port     :', redisport)
print('Redis database :', redisdb)
print('IFC file       :', ifcfilename)

# Set line counter to zero
linecount = 0

# Put every line from IFC data section to Redis database
ln = ifcfile.readline()
while ln != "":
  if ln[0] == "#":
    ifcline = ln.strip().split('=')
    key = ifcline[0].strip()
    val = ifcline[1].strip(';')
    db.set(key,val)
    linecount += 1
  ln = ifcfile.readline()

# Display summry info  
print(linecount, 'lines processed')



