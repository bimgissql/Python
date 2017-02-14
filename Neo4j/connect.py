# install Neo4j driver using pip install neo4j-driver==1.1.0b3

from neo4j.v1 import GraphDatabase, basic_auth
import yaml

# Get database connection information from YML file
with open("graphdb.yml", 'r') as stream:
    config = yaml.load(stream)

# Parse connection data	
gdbhost = config[':host'] 
gdbport = config[':port']
gdbuser = config[':user']
gdbpassw = config[':password']

# Show information
print('Connect to Neo4j database')
print('Neo4j server   :', pghost)
print('Neo4j port     :', str(pgport))

# connection
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("test", "test"))

# session
session = driver.session()

# Insert query
session.run("CREATE (a:Person {name:'X', title:'Mr.'})")

# Execute query
result = session.run("MATCH (a:Person) WHERE a.name = 'X' RETURN a.title AS title, a.name AS name")

for record in result:
  print("%s %s" % (record["title"], record["name"]))

# close Neo4j session
session.close()


