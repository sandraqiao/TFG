from models.lectura import Lectura
from repositories import lectura_repository, libro_repository
from utils import constants

import datetime as dt

def create(id_libro: int, estado: str, valoracion: int | None, comentario: str | None,
                   fecha_ini: dt.date, fecha_fin: dt.date | None, formato: str):

    _general_checks(id_libro=id_libro, estado=estado, valoracion=valoracion, fecha_ini=fecha_ini, 
                    fecha_fin=fecha_fin, formato=formato)

    lectura = _build_lectura(
        id_libro=id_libro,
        estado=estado,
        valoracion=valoracion,
        comentario=comentario,
        fecha_ini=fecha_ini,
        fecha_fin=fecha_fin,
        formato=formato
    )
    return lectura_repository.create(lectura)

def update(id_lectura: int, id_libro: int, estado: str, valoracion: int | None, 
           comentario: str | None, fecha_ini: dt.date, fecha_fin: dt.date | None, formato: str):

    if lectura_repository.get_by_id(id_lectura) is None:
        raise ValueError("Lectura inexistente.")

    _general_checks(id_libro=id_libro, estado=estado, valoracion=valoracion, fecha_ini=fecha_ini, 
                fecha_fin=fecha_fin, formato=formato)

    lectura = _build_lectura(
        id_lectura=id_lectura,
        id_libro=id_libro,
        estado=estado,
        valoracion=valoracion,
        comentario=comentario,
        fecha_ini=fecha_ini,
        fecha_fin=fecha_fin,
        formato=formato
    )
    return lectura_repository.update(lectura)

def delete(id_lectura: int):
    if lectura_repository.get_by_id(id_lectura) is None:
        raise ValueError("Lectura inexistente.")

    lectura_repository.delete(id_lectura)

# ===============================================================================================================

def _build_lectura(id_libro: int, estado: str, valoracion: int | None, comentario: str | None,
                   fecha_ini: dt.date, fecha_fin: dt.date | None, formato: str, 
                   id_lectura: int | None = None) -> Lectura:
    return Lectura(
        id_lectura=id_lectura,
        id_libro=id_libro,
        estado=estado,
        valoracion=valoracion,
        comentario=comentario,
        fecha_ini=fecha_ini,
        fecha_fin=fecha_fin,
        formato=formato
    )

def _general_checks(id_libro: int, estado: str, valoracion: int | None, fecha_ini: dt.date, 
                fecha_fin: dt.date | None, formato: str):
     
    if libro_repository.get_by_id(id_libro) is None:
        raise ValueError("Libro inexistente.")
     
    if estado not in constants.ESTADO:
        raise ValueError("Estado inválido.")
    
    if valoracion is not None and (valoracion < constants.VALORACION_MIN or constants.VALORACION_MAX < valoracion):
        raise ValueError("Valoración fuera de rango.")

    if fecha_fin is not None and fecha_fin < fecha_ini:
        raise ValueError("Fechas inválidas.")

    if formato not in constants.FORMATO:
        raise ValueError("Formato inválido.")