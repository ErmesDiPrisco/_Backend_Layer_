from dao.filmDao import Film

result=Film.getAllFilm()
for r in result:
    print(r)