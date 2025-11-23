import sqlite3

from routers.movie_routers import movies

conn = sqlite3.connect("movie.sqlite3")
cur = conn.cursor()

cur.execute("SELECT * FROM movies WHERE year > 2000")
rows = cur.fetchall()

for row in rows:
    print(row[1])





conn.commit()


movies = session.query(Movie).filter(Moview.year > 2000).all()
for m in movies:
    print(movie.title)
