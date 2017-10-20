import redis
import yaml
import time

start_time = time.time()

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

# Display summry info  
print('Number of keys  :', db.dbsize())

ifcprojectkey = ''
ifcprojectkey = db.get('0').decode('utf-8')
print('IFCPROJECT key  :', str(ifcprojectkey))

ifcmaxkey = ''
ifcmaxkey = db.get('-1').decode('utf-8')
print('Max key         :', str(ifcmaxkey))

for i in range(1,int(ifcmaxkey)):
    ifcobjectkey = str(i)
    ifcobjectval = db.get(ifcobjectkey)
#    if ifcobjectval != '':
#        ifcclass = ifcobjectval[0:ifcobjectval.find('(')]
#        print(ifcclass)

print('Running time    : %s seconds' % (time.time() - start_time))



