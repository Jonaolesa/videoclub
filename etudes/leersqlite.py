import sqlite3

def rows_to_dictlist(filas, nombres):
    registros = []
    for fila in filas:
        registro = {}
        pos = 0
        for nombre in nombres:
            registro[nombre] = fila[pos]
            pos += 1

        """
        for pos, nombre in enumerate(nombres):
            registro[nombre] = fila[pos]
        """
        registros.append(registro)
    return registros

# Abrir conexion
con = sqlite3.connect("data/peliculas.sqlite")

# Crear cursor 
cur = con.cursor()

# Uso el cursos con sql en forma de cadena
cur.execute("select id, nombre, url_foto from directores where url_foto is not NULL")

columns_description = cur.description
nombres_columna = []
for columna in columns_description:
    nombres_columna.append(columna[0])

nombres_columna = list(map(lambda item: item[0], columns_description))

# Proceso la respuesta si la hubiera (un select)
rows = cur.fetchall()

# hacer una funcion que me transforme la lista de tuplas result, en una lista de diccionarios como la que devuelve el dict reader

resultado = rows_to_dictlist(rows, nombres_columna)

print(resultado)

# Cerrar la conexion siempre
con.close()