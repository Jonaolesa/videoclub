import sqlite3

con = sqlite3.connect("data/peliculas.sqlite")

cur = con.cursor()

nombre = input("Nombre:")
foto = input("Url_foto:")
web = input("Url web:")

query = "INSERT INTO directores(nombre, url_foto, url_web) values (?, ?, ?)"

print(query)
cur.execute(query, (nombre, foto, web))
con.commit()

con.close()