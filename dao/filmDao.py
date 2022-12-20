from dao.utility.db import MySql

class Film:

    @classmethod
    def getAllFilm(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film")
        data = MySql.getResults()
        MySql.closeConnection()

        return data

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
