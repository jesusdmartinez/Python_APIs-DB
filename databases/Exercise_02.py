'''
Using sqlalchemy which the necessary code to:

- Select all the actors with the first name of your choice-- x

- Select all the actors and the films they have been in-- x

- Select all the actors that have appeared in a category of you choice comedy-- x

- Select all the comedic films and that and sort them by rental rate-- x

- Using one of the statements above, add a GROUP BY

- Using on of the statements above, add a ORDER BY

'''
import sqlalchemy
from pprint import pprint
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:hoboHOBO123!@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

#FILTER TO COMEDIES, AND SORT BY RENTAL RATE
join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id).join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
query = sqlalchemy.select([actor.columns.first_name, film.columns.rental_rate]).where(category.columns.name == "comedy").order_by(film.columns.rental_rate.desc()).group_by(actor.columns.first_name).select_from(join_statement)

result_proxy = connection.execute(query)
result = result_proxy.fetchall()

pprint(result)




# #PICK ED QUERY
# join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# query = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, film.columns.title]).where(category.columns. == "Ed").select_from(join_statement)
#
# result_proxy = connection.execute(query)
# result = result_proxy.fetchall()
#
# pprint(result)


# query = sqlalchemy.select([actor]).where(actor.columns.first_name == "Jesus")

# join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# # query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name]).select_from(join_statement)



