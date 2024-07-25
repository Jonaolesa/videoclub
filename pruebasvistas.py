from app.vistas import VistaTituloPagina, VistaCatalogo
from app.modelos import Pelicula, Director
from simple_screen import Screen_manager, Input, cls, Print, DIMENSIONS, locate

tit1 = VistaTituloPagina("Video Club Mari Pepis")
tit2 = VistaTituloPagina("Catálogo de películas", 2)
p1 = Pelicula("Titulo1", "Un resumen cualquiera", Director("Robert Redford", 1))
p2 = Pelicula("Titulo2", "Sinopsis distinta", Director("Isabel Coixet", 2))
p3 = Pelicula("Titulo3", "Sinopsis 3", Director("director 4", 4))
p4 = Pelicula("Titulo4", "Sinopsis cuaggro", Director("El nuevo", 44))

vista_catalogo = VistaCatalogo([p1, p2, p3, p4], 3, 3, 89, 3)

with Screen_manager:
    cls()
    tit1.paint()
    tit2.paint()
    vista_catalogo.paint()

    locate(0, DIMENSIONS.h - 1)
    Input("Pulse enter para acabar")
    

