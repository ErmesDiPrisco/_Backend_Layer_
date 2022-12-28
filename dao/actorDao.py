from dao.utility.db import MySql
from dto.actordto import Actordto

class ActorDao:
    @classmethod
    def findAllActors(cls):
        MySql.openConnection()
        MySql.query(
          "SELECT * \
            FROM Actor")
        data = MySql.getResults()
        actors=list()
        for actor in data:
          actors.append(Actordto(actor[0], actor[1], actor[2], actor[3]))

        MySql.closeConnection()
        return actors

    @classmethod
    def findFirstNameAndLastnameByFilmTitle(cls, titolo_film):
        MySql.openConnection()
        MySql.query(
          f"SELECT a.actor_id, a.first_name, a.last_name, a.last_update\
            FROM Actor a, Film f, Film_Actor fa \
            WHERE a.actor_id = fa.actor_id AND fa.film_id = f.film_id \
            AND f.title = '{titolo_film}'"
            )
        data = MySql.getResults()
        actors=list()
        for actor in data:
          actors.append(Actordto(actor[0], actor[1], actor[2], actor[3]))
        MySql.closeConnection()
        return actors
      
    @classmethod
    def findActorByName(cls, name):
        MySql.openConnection()
        MySql.query(
          f"SELECT * FROM Actor WHERE first_name = '{name}'"
          )
        data = MySql.getResults()
        actors=list()
        for actor in data:
          actors.append(Actordto(actor[0], actor[1], actor[2], actor[3]))
        MySql.closeConnection()
        return actors
      
    @classmethod
    def findActorBySurname(cls, surname):
        MySql.openConnection()
        MySql.query(
          f"SELECT * FROM Actor WHERE last_name = '{surname}'"
          )
        data = MySql.getResults()
        actors=list()
        for actor in data:
          actors.append(Actordto(actor[0], actor[1], actor[2], actor[3]))
        MySql.closeConnection()
        return actors 

    @classmethod
    def findActorById(cls, id_attore):
        MySql.openConnection()
        MySql.query(
          f"SELECT *\
            FROM ACTOR\
            WHERE actor_id = {id_attore}"
        )
        data = MySql.getResults()
        actors=list()
        for actor in data:
          actors.append(Actordto(actor[0], actor[1], actor[2], actor[3]))
        MySql.closeConnection()
        return actors

    @classmethod
    def findActorByIdentityNumber(cls, id):
        MySql.openConnection()
        MySql.query(
          f"SELECT *\
            FROM ACTOR\
            WHERE actor_id = {id}"
        )
        data = MySql.getResults()
        actors=list()
        for actor in data:
          actors.append(Actordto(actor[0], actor[1], actor[2], actor[3]))
        MySql.closeConnection()
        return actors

    @classmethod
    def findFirstNameAndLastnameBy15NumFilm(cls):
        MySql.openConnection()
        MySql.query(
          f"SELECT actor.first_name, actor.last_name, COUNT(film_actor.actor_id) AS Num \
            FROM actor \
            INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id\
            GROUP BY film_actor.actor_id\
            HAVING COUNT(film_actor.actor_id) > 15"
        )
        data = MySql.getResults()
        MySql.closeConnection()      
        return data
