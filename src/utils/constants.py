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


# Atributos Lectura

ESTADO: list[str] = [
    "Leyendo",
    "Leído",
    "Abandonado"
]

VALORACION_MIN = 1
VALORACION_MAX = 5

FORMATO: list[str] = [
    "Físico",
    "Ebook",
    "AudioLibro"
]

# Atributos sort-eables libros
SORT_BIBLIOTECA: list[str] = [
    "Título",
    "Saga"
]

# Atributos filtrables

FILTROS_LECTURAS: list[str] = [
    "Estados",
    "Valoraciones", 
    "Formatos"
]

FILTROS_LIBROS: list[str] = [
    "Generos",
    "Idiomas",
    "Editoriales",
    "Wishlisteado"
]