import sqlite3

# Abrir conexion
con = sqlite3.connect("data/peliculas.sqlite")

# Crear cursor 
cur = con.cursor()

# Uso el cursos con sql en forma de cadena
cur.execute("select id, nombre, url_foto, url_web from directores")

columns_description = cur.description

# Proceso la respuesta si la hubiera (un select)
result = cur.fetchall()


# hacer una funcion que me transforme la lista de tuplas result, en una lista de diccionarios como la que devuelve el dict reader


print(result)

# Cerrar la conexion siempre
con.close()