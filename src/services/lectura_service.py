from models.lectura import Lectura
from repositories import lectura_repository, libro_repository
from utils import constants

import datetime as dt

def create(id_libro: int, 
           estado: str,
           formato: str,
           fecha_ini: dt.date, 
           fecha_fin: dt.date | None = None, 
           valoracion: int | None = None, 
           comentario: str | None = None):

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

def update(id_lectura: int,
           id_libro: int, 
           estado: str,
           formato: str,
           fecha_ini: dt.date, 
           fecha_fin: dt.date | None = None, 
           valoracion: int | None = None, 
           comentario: str | None = None):

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

def get_all_lecturas():
    return lectura_repository.get_all()

def search_by_libro(id_libro: int):
    if libro_repository.get_by_id(id_libro) is None:
        raise ValueError("Libro inexistente.")
    if lectura_repository.get_by_libro(id_libro) is None:
        raise ValueError("Este libro no tiene lecturas.")
    return lectura_repository.get_by_libro(id_libro)

def filter_lectura(estados: list[str] | None = None, valoraciones: list[int] | None = None, formatos: list[str] | None = None):

    filtros = []

    if estados: 
        filtros.append(Lectura.estado.in_(estados))
    if valoraciones: 
        filtros.append(Lectura.valoracion.in_(valoraciones))
    if formatos: 
        filtros.append(Lectura.formato.in_(formatos))

    return lectura_repository.filter_lectura(filtros)

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
    
    if valoracion is not None:
        if estado not in (constants.ESTADO[1], constants.ESTADO[2]):
            raise ValueError("Una lectura solo puede tener valoración si está finalizada o abandonada.")
        if (valoracion < constants.VALORACION_MIN or constants.VALORACION_MAX < valoracion):
            raise ValueError("Valoración fuera de rango.")

    if fecha_fin is not None and fecha_fin < fecha_ini:
        raise ValueError("Fechas inválidas.")

    if formato not in constants.FORMATO:
        raise ValueError("Formato inválido.")