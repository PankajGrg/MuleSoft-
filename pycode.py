import sqlite3 as sql

connection = sql.connect("moviedb.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('The Conjuring','Patrick Wilson','Vera Farmiga','James Wan',2013)")
pointer.execute("INSERT INTO MOVIES VALUES('Eternals','Richard Madden','Gemma Chan','Chloé Zhao',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Spider-Man: Homecoming','Tom Holland','Zendaya','Jon Watts',2017)")
pointer.execute("INSERT INTO MOVIES VALUES('Avengers: Endgame','Robert Downey Jr.','Elizabeth Olsen','Sarah Finn',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('Inception','Leonardo DiCaprio','Marion Cotillard','Christopher Nolan',2010)")


print("------------------------------- Movies  in the database-------------------------------")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("-----------------------------------------------------------------------------------------------")

# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("\n\n\n\n------------------------------------------- Actor ------------------------------------------")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Richard Madden'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("-----------------------------------------------------------------------------------------------")
  