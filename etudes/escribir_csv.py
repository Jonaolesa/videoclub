import csv

fichero = open("data/grupos_zoo.csv", "a", newline="")
escribidor_csv = csv.writer(fichero, delimiter=";", quotechar="'")
escribidor_csv.writerow([1, 3, 1, 23])
escribidor_csv.writerow([1, 4, 1, 18])

fichero.close()

#ahora con diccionarios

with open("data/grupos_zoo.csv", "a", newline="") as fichero:
    escribidor_csv = csv.DictWriter(fichero, fieldnames=["id_grupo", "tipo_entrada", "cantidad_entrada", "subtotal"], delimiter=":", quotechar="'")
    escribidor_csv.writerows([
        {"id_grupo":1, "tipo_entrada":3, "cantidad_entrada":1, "subtotal": 23},
        {"id_grupo":1, "tipo_entrada":4, "cantidad_entrada":1, "subtotal": 18},
    ])


