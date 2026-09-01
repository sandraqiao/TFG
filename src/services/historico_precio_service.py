from models.historico_precio import HistoricoPrecio
from repositories import historico_precio_repository, libro_repository, tienda_repository

from decimal import Decimal
import datetime as dt

def create(id_libro: int, 
           id_tienda: int, 
           precio: Decimal, 
           fecha_consulta: dt.date, 
           disponible: bool, 
           url_libro: str,
           pct_descuento: Decimal | None = None):

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

def update(id_precio: int,
           id_libro: int, 
           id_tienda: int, 
           precio: Decimal, 
           fecha_consulta: dt.date, 
           disponible: bool, 
           url_libro: str,
           pct_descuento: Decimal | None = None):

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

def get_all_historico_precio():
    return historico_precio_repository.get_all()

def filter_historico(libros: list[int] | None = None, tiendas: list[int] | None = None, 
                     fecha_ini: dt.date | None = None, fecha_fin: dt.date | None = None,
                       precio_min: Decimal | None = None, precio_max: Decimal | None = None):

    filtros = []

    if libros: 
        filtros.append(HistoricoPrecio.id_libro.in_(libros))
    if tiendas: 
        filtros.append(HistoricoPrecio.id_tienda.in_(tiendas))
    if fecha_ini is not None and fecha_fin is not None: 
        filtros.append(HistoricoPrecio.fecha_consulta.between(fecha_ini, fecha_fin))
    if precio_min is not None and precio_max is not None: 
        filtros.append(HistoricoPrecio.precio.between(precio_min, precio_max))

    return historico_precio_repository.filter_historico_precio(filtros)

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

    if precio is None or precio <= 0:
        raise ValueError("Precio fuera de rango.")

    if pct_descuento is not None and (pct_descuento < 0 or pct_descuento > 100):
        raise ValueError("Porcentaje de descuento fuera de rango.")