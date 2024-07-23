CREATE TABLE IF NOT EXISTS "directores" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"url_foto"	TEXT,
	"url_web"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "peliculas" (
	"id"	INTEGER,
	"titulo"	TEXT NOT NULL,
	"id_director"	INTEGER NOT NULL,
	"anyo"	INTEGER NOT NULL,
	"url_caratula"	TEXT,
	"id_genero"	INTEGER,
	"es_animacion"	INTEGER,
	FOREIGN KEY("id_director") REFERENCES "directores"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)
