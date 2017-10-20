import redis
import yaml
import time

start_time = time.time()

ifcfilename = "HITOS_Architectural_2006-10-25.ifc"

# Get database connection information from YML file
with open("redis.yml", 'r') as stream:
    config = yaml.load(stream)

# Parse connection data	
redishost = config[':host']
redisport = config[':port']
redisdb = config[':db']

# Redis connection pool
pool = redis.ConnectionPool(host=redishost, port=redisport, db=redisdb)

# Redis database
db = redis.Redis(connection_pool=pool)

# Show information
print('Redis server    :', redishost)
print('Redis port      :', redisport)
print('Redis database  :', redisdb)

# open IFC file for read
ifcfile = open(ifcfilename,"r")
print('Processing file :',ifcfilename)

# set counter
i = 0
notfound = True
maxkey = 0

# iterate through whole IFC file line by line
for line in ifcfile:
    if line[0] == "#":
        i += 1
        ifcobject = line.split("=")
        ifcobjectkey = ifcobject[0][1:].strip()
        ifcobjectval = ifcobject[1].strip()
        if (ifcobjectval[0:10] == 'IFCPROJECT' and notfound):
            ifcprojectkey = ifcobjectkey
            print('IFCPROJECT key  :', ifcprojectkey)
            db.set('0',ifcprojectkey.encode('utf-8'))
            notfound = False
        db.set(ifcobjectkey,ifcobjectval.encode('utf-8'))
        if int(ifcobjectkey) > maxkey:
            maxkey = int(ifcobjectkey)
print('Objects in file :',i)
ifcfile.close()        

db.set('-1',str(maxkey).encode('utf-8'))

# Display summry info  
print('Number of keys  :', db.dbsize())
print('Running time    : %s seconds' % (time.time() - start_time))


