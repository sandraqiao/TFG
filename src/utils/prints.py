from services import libro_service, autor_libro_service, autor_service
from datetime import date

def titulo_autor(titulo: str,  autores: list) -> str:

    titulo_autor = titulo + " - "

    for i, autor in enumerate(autores):
        if i > 0:
            titulo_autor += ", "
        titulo_autor += autor.nom_autor

    return titulo_autor

# def titulo_y_autor(id_libro: int) -> str:

#     libro = libro_service.get_libro(id_libro)
#     autoreslibro = autor_libro_service.search_by_libro(libro.id_libro)

#     titulo_y_autor = libro.titulo
    
#     for autorlibro in autoreslibro:
#         titulo_y_autor += " - "
#         titulo_y_autor += autor_service.get_by_id(autorlibro.id_autor).nom_autor

    return titulo_y_autor

def codigo_color_estado(estado: str) -> str:

    if estado == "Leído":
        return "🟢"
    elif estado == "Leyendo":
        return "🟡"
    else:
        return "🔴"

def estrellas(valoracion: int) -> str:
    estrellas = ""

    if valoracion:
        for i in range(10):
            if i < valoracion:
                estrellas += "★"
            else:
                estrellas += "☆"
            estrellas += " "
    else:
        estrellas = "☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆"
        valoracion = 0

    estrellas += f"({valoracion}/10)"
    return estrellas

def fechas(ini: date, fin: date | None) -> str:

    fechas = ""

    if fin:
        fechas += f"{ini.strftime('%d/%m/%Y')} - {fin.strftime('%d/%m/%Y')}"
    else:
        fechas += f"{ini.strftime('%d/%m/%Y')} - [sin especificar]"

    return fechas