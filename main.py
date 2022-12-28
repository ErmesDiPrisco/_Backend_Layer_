from dao.actorDao import ActorDao

result=ActorDao.findFirstNameAndLastnameBy15NumFilm()
for r in result:
    print(r)