# ==========================================================================================================
# ACTIVACIÓN ENTORNO VIRUTAL
# ==========================================================================================================
# .\.venv\Scripts\Activate.ps1

# ==========================================================================================================
# CREACIÓN DE TABLAS QUE NO EXISTAN
# ==========================================================================================================
# import models
# from database.base import Base
# from database.database import engine

# Base.metadata.create_all(engine)

# QUERY PARA BORRADO: DROP SCHEMA public CASCADE; CREATE SCHEMA public;

# ==========================================================================================================
# FILTROS
# ==========================================================================================================

# import models
# import services

# resultados = services.historico_precio_service.filter_historico(
#     libros=[1, 4],
#     # tiendas=[1]
#     # fecha_min='2019-12-01',
#     # fecha_max='2019-12-04',
#     precio_min=10,
#     precio_max=20
# )

# ==========================================================================================================
# STREAMLIT
# ==========================================================================================================
# streamlit run .\src\ui\Home.py

# $env:PYTHONPATH = ".\src"

# ==========================================================================================================

# from services import autor_service, autor_libro_service, libro_service, lectura_service
# from datetime import date


# def titulo_y_autor(libro):

#     titulo_autor = libro.titulo

#     print(titulo_autor)

#     autoreslibro = autor_libro_service.search_by_libro(libro.id_libro)
    
#     for autorlibro in autoreslibro:
#         titulo_autor += " - "
#         titulo_autor += autor_service.get_by_id(autorlibro.id_autor).nom_autor

#     return titulo_autor


# lecturas = lectura_service.get_all_lecturas()

# for lectura in lecturas:
#     libro = libro_service.get_libro(lectura.id_libro)
#     titulo_y_autor(libro)
    # autoreslibro = autor_libro_service.search_by_libro(libro.id_libro)
#     titulo = libro.titulo 
#     if autoreslibro is None:
#         titulo =+ "[Sin datos]"
#     for autorlibro in autoreslibro:
#         titulo += " - "
#         titulo += autor_service.get_by_id(autorlibro.id_autor).nom_autor
#     print(titulo)

# ==========================================================================================================

# from services import lectura_service, saga_service, autor_service, libro_service, autor_libro_service
# from datetime import date

# saga_service.create("The Shepherd King")
# saga_service.create("This Woven Kingdom")
# saga_service.create("Mindf*ck")

# autor_service.create("Rachel Gillig")
# autor_service.create("Tahereh Mafi")
# autor_service.create("S.T. Abby")

# libro_service.create("One Dark Window", "Aventura, Fantasía, Juvenil, Romance", "ENG", False, 1, "9780356519494", 432, fecha_public=date(2022, 3, 27), editorial="Macdonald Orbis")
# libro_service.create("Two twisted crowns", "Aventura, Fantasía, Juvenil, Romance", "ENG", False, 1, "9780356519500", 464, fecha_public=date(2023, 10, 19), editorial="Macdonald Orbis")

# libro_service.create("This Woven Kingdom", "Aventura, Fantasía, Juvenil, Romance", "ENG", False, 2, "9780755500093", 496, fecha_public=date(2022, 8, 4), editorial="Electric Monkey")
# libro_service.create("These Infinite Threads", "Aventura, Fantasía, Juvenil, Romance", "ENG", False, 2, "9780008529529", 404, fecha_public=date(2023, 8, 3), editorial="Electric Monkey")
# libro_service.create("All This Twisted Glory", "Aventura, Fantasía, Juvenil, Romance", "ENG", False, 2, "9780008625757", 416, fecha_public=date(2024, 8, 1), editorial="Electric Monkey")
# libro_service.create("Every Spiral of Fate", "Aventura, Fantasía, Juvenil, Romance", "ENG", True, 2, "9780008629243", fecha_public=date(2026, 8, 13), editorial="Electric Monkey", prioridad_wishlist=5)

# libro_service.create("Mindf*ck", "Acción, Novela negra, Policíaca, Romance, Thriller", "ENG", True, 3, "")

# lectura_service.create(1, "Leído",  "Físico", date(2024, 10, 30), date(2024, 11, 5), 7)
# lectura_service.create(1, "Leído",  "Físico", date(2025, 11, 25), date(2025, 12, 1), 8)
# lectura_service.create(2, "Leído",  "Físico", date(2024, 11, 6), date(2024, 11, 19), 6)
# lectura_service.create(3, "Leído",  "Físico", date(2024, 8, 5), date(2024, 8, 11), 8)
# lectura_service.create(4, "Leído",  "Físico", date(2024, 8, 12), date(2024, 8, 17), 7)
# lectura_service.create(5, "Leído",  "Físico", date(2024, 8, 24), date(2024, 9, 2), 7)
# lectura_service.create(7, "Leído",  "Ebook", date(2024, 10, 2), date(2024, 10, 11), 8)
# lectura_service.create(7, "Leyendo",  "Ebook", date(2026, 8, 30))

# lectura_service.update(1, 1, "Leído",  "Físico", date(2024, 10, 30), date(2024, 11, 5), 7, "Buffff. Que fuerte. Wenísimo final y mu heavy. Pos ma gustau. No es el mejor libro de la historia pero lo he disfrutado.")