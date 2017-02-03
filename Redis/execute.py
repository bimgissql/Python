import redis
import yaml

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
print('Execute Redis command')
print('Redis server   :', redishost)
print('Redis port     :', redisport)
print('Redis database :', redisdb)

# Execute Redis command and display its output
print(db.execute_command('GET','#1'))



