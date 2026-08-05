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

PRIORIDAD_WISHLIST_MIN = 1
PRIORIDAD_WISHLIST_MAX = 5
PRIORIDAD_WISHLIST = list(range(PRIORIDAD_WISHLIST_MIN, PRIORIDAD_WISHLIST_MAX+1))


# Atributos Lectura

ESTADO: list[str] = [
    "Leyendo",
    "Leído",
    "Abandonado"
]

VALORACION_MIN = 0
VALORACION_MAX = 10
VALORACION = list(range(VALORACION_MIN, VALORACION_MAX+1))

FORMATO: list[str] = [
    "Físico",
    "Ebook",
    "AudioLibro"
]