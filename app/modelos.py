from abc import ABC, abstractmethod
import csv
import sqlite3

class Model(ABC):
    @classmethod
    @abstractmethod
    def create_from_dict(cls, diccionario):
        pass

class Director(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["nombre"], int(diccionario["id"]))

    def __init__(self, nombre: str, id: int = -1):
        self.nombre = nombre
        self.id = id

    def __repr__(self) -> str:
        return f"Director ({self.id}): {self.nombre}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.nombre == other.nombre
        return False
    
    def __hash__(self):
        return hash((self.id, self.nombre))


class Pelicula(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["titulo"], 
                   diccionario["sinopsis"], 
                   int(diccionario["director_id"]), 
                   int(diccionario["id"]))
    
    def __init__(self, titulo: str, sinopsis: str, director: object, id = -1):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id = id
        self.director = director
                
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value
            self._id_director = value.id
        elif isinstance(value, int):
            self._director = None
            self._id_director = value
        else:
            raise TypeError(f"{value} debe ser un entero o instancia de Director")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.titulo == other.titulo and self.sinopsis == other.sinopsis and self.director == other.director and self.id == other.id
        return False
    
    def __hash__(self):
        return hash((self.id, self.titulo, self.sinopsis, self.director))
    
    def __repr__(self):
        return f"Pelicula ({self.id}): {self.titulo}, {self.director}"


class DAO(ABC):
    """
    @abstractmethod
    def guardar(self, instancia):
        pass
    
    @abstractmethod
    def actualizar(self, instancia):
        pass
    
    @abstractmethod
    def borrar(self, id: int):
        pass
    
    @abstractmethod
    def consultar(self, id: int):
        pass
    """

    @abstractmethod
    def todos(self):
        pass

class DAO_CSV(DAO):
    model = None

    def __init__(self, path):
        self.path = path

    def todos(self):
        with open(self.path, "r", newline="", encoding="utf-8") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(self.model.create_from_dict(registro))
        return lista     

class DAO_CSV_Director(DAO_CSV):
    model = Director

class DAO_CSV_Pelicula(DAO_CSV):
    model = Pelicula

class DAO_SQLite(DAO):
    model = None
    tabla = None
    
    def __init__(self, path):
        self.path = path
    
    def todos(self):
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        nombres = list(map(lambda item: item[0], cur.description))
        cur.execute(f"Select * from {self.tabla}")

        lista = self.__rows_to_dictlist(cur.fetchall(), nombres)
        resultado = []
        for registro in lista:
            resultado.append(self.model.create_from_dict(registro))
        conn.close()
        return resultado

    def  __rows_to_dictlist(self, filas, nombres):
        registros = []
        for fila in filas:
            registro = {}
            pos = 0
            for nombre in nombres:
                registro[nombre] = fila[pos]
                pos += 1

            registros.append(registro)
        return registros

        
class DAO_SQLite_Director(DAO_SQLite):
    model = Director
    tabla = "directores"