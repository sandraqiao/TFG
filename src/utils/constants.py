# Atributos Libro

GENERO: list[str] = [
    "Acción",
    "Aventura",
    "Autobiografía",
    "Biografía",
    "Ciencia ficción",
    "Contemporánea",
    "Distopía",
    "Divulgación",
    "Drama",
    "Ensayo",
    "Fantasía",
    "Filosofía",
    "Historia",
    "Histórica",
    "Humor",
    "Infantil",
    "Juvenil",
    "Memorias",
    "Misterio",
    "New Adult",
    "Novela negra",
    "Poesía",
    "Policíaca",
    "Psicología",
    "Realismo mágico",
    "Romance",
    "Suspense",
    "Teatro",
    "Terror",
    "Thriller",
]

IDIOMA: list[str] = [
    "ESP",
    "ENG"
]

PRIORIDAD_WISHLIST = list(range(1,6)) # 1-5


# Atributos Lectura

ESTADO: list[str] = [
    "Leyendo",
    "Leído",
    "Abandonado"
]

VALORACION = list(range(11)) # 0-10

FORMATO: list[str] = [
    "Físico",
    "Ebook",
    "AudioLibro"
]