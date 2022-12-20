# File che utilizzeremo in futuro :D

from dao.actorDao import ActorDao
from dao.filmDao import Film

qry1=Film()
categoria=input('Inserisci la categoria: ')
qry1=qry1.getCategories(categoria)
print(qry1)

