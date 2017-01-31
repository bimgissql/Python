import redis

# Redis host server address
redishost = '192.168.55.181'

# Redis port number on host server
redisport = 6379

# Number of database on Redis server
redisdb = 0

# Redis connection pool
pool = redis.ConnectionPool(host=redishost, port=redisport, db=redisdb)

# Redis database
db = redis.Redis(connection_pool=pool)

# Show information
print('Delete contents of Redis database')
print('Redis server   :', redishost)
print('Redis port     :', redisport)
print('Redis database :', redisdb)

# Display summry info  
print('Number of keys :', db.dbsize())


