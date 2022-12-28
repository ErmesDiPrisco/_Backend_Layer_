from dao.actorDao import ActorDao

titolofilm=input('')
result=ActorDao.findFirstNameAndLastnameByFilmTitle(titolofilm)
for r in result:
    print(r)