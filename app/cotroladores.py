from app.vistas import VistaTituloPagina, VistaCatalogo
from app.modelos import DAO_CSV_Pelicula
from simple_screen import DIMENSIONS, locate, Input, cls, Screen_manager

class VideoClub:
    def __init__(self):
        self.tituloPagina = VistaTituloPagina("CATALOGO VC")
        self.titulo2 = VistaTituloPagina("===========", 2)

        self.vista_catalogo = VistaCatalogo([], 0, 2, 0, 3)
        self.daoPelis = DAO_CSV_Pelicula("tests/data/peliculas.csv")

    def run(self):
        continuar = "S"
        with Screen_manager:
            while continuar.upper() == "S":
                cls()
                peliculas = self.daoPelis.todos()
                self.vista_catalogo.peliculas = peliculas

                self.tituloPagina.paint()
                self.titulo2.paint()
                self.vista_catalogo.paint()

                locate(0, DIMENSIONS.h - 1, "Repetir (S/n)")
                continuar = Input()
