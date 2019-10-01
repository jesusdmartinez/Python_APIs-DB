'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:hoboHOBO123!@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([category])
result_proxy = connection.execute(query)
result = result_proxy.fetchone()

pprint(result)


film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.select([film])
result_proxy = connection.execute(query)
result = result_proxy.fetchone()

pprint(result)




# actor_list = []

# for result in result_proxy:
#     new_actor = Actor(result['actor_id'], result['first_name'], result['last_name'], result['last_update'])
#     actor_list.append(new_actor)
#
# for actor in actor_list:
#     print(actor)

