from app.modelos import Director, DAO_CSV_Director, Pelicula, DAO_CSV_Pelicula, DAO_SQLite_Director

def test_create_director():
    director = Director("Robert Redford")

    assert director.nombre == "Robert Redford"
    assert director.id == -1


def test_dao_directores_traer_todos():
    dao = DAO_CSV_Director("tests/data/directores.csv")
    directores = dao.todos()

    assert len(directores) == 8
    assert directores[7] == Director("Charlie Chaplin", 8) 

def test_create_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", 9)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director is None
  
def test_create_pelicula_and_informar_director_completo():
    director = Director("Peter Jackson", 9)
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", director)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director == director

def test_asigna_director_a_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", -1)

    director = Director("Peter Jackson", 9)

    pelicula.director = director

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"

    assert pelicula.id == -1
    assert pelicula.director == director
    assert pelicula._id_director == 9

def test_dao_peliculas_traer_todos():
    dao = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    peliculas = dao.todos()

    assert len(peliculas) == 5

    assert peliculas[1] == Pelicula("Los siete samuráis", "Una banda de forajidos atemorizan a los habitantes de un pequeño pueblo, saqueándolos periódicamente sin piedad. Para repeler estos ataques, los aldeanos deciden contratar a mercenarios. Finalmente, consiguen los servicios de 7 guerreros, 7 samurais dispuestos a defenderlos a cambio, tan solo, de cobijo y comida.", 2, 17 )

def test_dao_directores_sql_traer_todos():
    dao = DAO_SQLite_Director("data/films.sqlite")

    directores = dao.todos()

    assert len(directores) == 76
    assert directores[7] == Director("Charlie Chgapli", 8)