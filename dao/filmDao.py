from dao.utility.db import MySql
from dto.filmdto import Filmdto

class Film:

    @classmethod
    def getAllFilm(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film")
        data = MySql.getResults()
        films=list()
        for film in data:
            films.append(Filmdto(film[0], film[1], film[2], film[3], film[4], film[5], film[6], film[7], film[8], film[9], film[10], film[11], film[12]))

        MySql.closeConnection()

        return films

    @classmethod
    def getAllPgFilms(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film WHERE rating like 'PG%'")
        
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllTitleStartR(cls):
        MySql.openConnection()
        MySql.query("SELECT title FROM film WHERE title LIKE 'R%'")

        data = MySql.getResults()
        MySql.closeConnection()

        return data
    
    @classmethod
    def  getCategories(cls, categoria):
        MySql.openConnection()
        MySql.query(f'Select title, name from film_category fc inner join film f on f.film_id=fc.film_id inner join category c on c.category_id=fc.category_id where name="{categoria}"')

        data=MySql.getResults()
        MySql.closeConnection()
        
        return data
