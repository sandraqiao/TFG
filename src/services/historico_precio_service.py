from models.historico_precio import HistoricoPrecio
from repositories import historico_precio_repository, libro_repository, tienda_repository

from decimal import Decimal
import datetime as dt

def create(id_libro: int, id_tienda: int, precio: Decimal, pct_descuento: Decimal | None, fecha_consulta: dt.date, 
           disponible: bool, url_libro: str):

    _general_checks(id_libro=id_libro, id_tienda=id_tienda, precio=precio, pct_descuento=pct_descuento)

    historico_precio = _build_historico_precio(
        id_libro=id_libro,
        id_tienda=id_tienda,
        precio=precio,
        pct_descuento=pct_descuento,
        fecha_consulta=fecha_consulta,
        disponible=disponible,
        url_libro=url_libro
    )
    return historico_precio_repository.create(historico_precio)

def update(id_precio: int, id_libro: int, id_tienda: int, precio: Decimal, pct_descuento: Decimal | None, 
           fecha_consulta: dt.date, disponible: bool, url_libro: str):

    if historico_precio_repository.get_by_id(id_precio) is None:
        raise ValueError("Histórico inexistente.")

    _general_checks(id_libro=id_libro, id_tienda=id_tienda, precio=precio, pct_descuento=pct_descuento)

    historico_precio = _build_historico_precio(
            id_precio=id_precio,
            id_libro=id_libro,
            id_tienda=id_tienda,
            precio=precio,
            pct_descuento=pct_descuento,
            fecha_consulta=fecha_consulta,
            disponible=disponible,
            url_libro=url_libro
        )

    return historico_precio_repository.update(historico_precio)

def delete(id_precio:int):
    if historico_precio_repository.get_by_id(id_precio) is None:
            raise ValueError("Histórico inexistente.")

    historico_precio_repository.delete(id_precio)

# ===============================================================================================================

def _build_historico_precio(id_libro: int, id_tienda: int, precio: Decimal, pct_descuento: Decimal | None, 
                            fecha_consulta: dt.date, disponible: bool, url_libro: str, 
                            id_precio: int | None = None) -> HistoricoPrecio:
    return HistoricoPrecio(
        id_precio=id_precio,
        id_libro=id_libro,
        id_tienda=id_tienda,
        precio=precio,
        pct_descuento=pct_descuento,
        fecha_consulta=fecha_consulta,
        disponible=disponible,
        url_libro=url_libro
    )

def _general_checks(id_libro: int, id_tienda: int, precio: Decimal, pct_descuento: Decimal | None):

    if libro_repository.get_by_id(id_libro) is None:
        raise ValueError("Libro inexistente.")

    if tienda_repository.get_by_id(id_tienda) is None:
        raise ValueError("Tienda inexistente.")

    if precio is None or precio < 0:
        raise ValueError("Precio fuera de rango.")

    if pct_descuento is not None and (pct_descuento <= 0 or pct_descuento > 100):
        raise ValueError("Porcentaje de descuento fuera de rango.")

    