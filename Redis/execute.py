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
print('Execute Redis command')
print('Redis server   :', redishost)
print('Redis port     :', redisport)
print('Redis database :', redisdb)

# Execute Redis command and display its output
print(db.execute_command('GET','#1'))


