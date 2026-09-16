from datetime import date
from utils import constants

def titulo_autor(titulo: str,  autores: list) -> str:

    titulo_autor = titulo + " - "

    for i, autor in enumerate(autores):
        if i > 0:
            titulo_autor += ", "
        titulo_autor += autor.nom_autor

    return titulo_autor

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
        for i in range(constants.VALORACION_MAX):
            if i < valoracion:
                estrellas += "★"
            else:
                estrellas += "☆"
            estrellas += " "
    else:
        estrellas = "☆ ☆ ☆ ☆ ☆"
        valoracion = 0

    estrellas += f"({valoracion}/{constants.VALORACION_MAX})"
    return estrellas

def fechas(ini: date, fin: date | None) -> str:

    fechas = ""

    if fin:
        fechas += f"{ini.strftime('%d/%m/%Y')} - {fin.strftime('%d/%m/%Y')}"
    else:
        fechas += f"{ini.strftime('%d/%m/%Y')} - [sin especificar]"

    return fechas