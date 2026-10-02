from models.libro import Libro
from repositories import libro_repository, saga_repository
from utils.constants import PRIORIDAD_WISHLIST_MIN, PRIORIDAD_WISHLIST_MAX
from sqlalchemy import or_

import datetime as dt

def create(titulo: str, 
           genero: str, 
           idioma: str,
           en_wishlist: bool, 
           id_saga: int | None = None,  
           isbn: str | None = None, 
           num_pag: int | None = None,  
           sinopsis: str | None = None, 
           fecha_public: dt.date | None = None, 
           url_portada: str | None = None, 
           editorial: str | None = None,
           prioridad_wishlist: int | None = None):

    isbn=_clean_optional(isbn)
    url_portada=_clean_optional(url_portada)
    editorial=_clean_optional(editorial)

    if isbn is not None and libro_repository.get_by_isbn(isbn):
        raise ValueError("ISBN ya existente.")

    _obligatory(titulo=titulo, genero=genero, idioma=idioma)
    _general_checks(id_saga=id_saga, num_pag=num_pag, en_wishlist=en_wishlist, prioridad_wishlist=prioridad_wishlist)
    
    libro = _build_libro(
                id_saga=id_saga,
                titulo=titulo,
                isbn=isbn,
                num_pag=num_pag,
                genero=genero,
                idioma=idioma,
                sinopsis=sinopsis,
                fecha_public=fecha_public,
                url_portada=url_portada,
                editorial=editorial,
                en_wishlist=en_wishlist,
                prioridad_wishlist=prioridad_wishlist
    )
    return libro_repository.create(libro)

def update(id_libro: int,
           titulo: str, 
           genero: str, 
           idioma: str,
           en_wishlist: bool, 
           id_saga: int | None = None,  
           isbn: str | None = None, 
           num_pag: int | None = None,  
           sinopsis: str | None = None, 
           fecha_public: dt.date | None = None, 
           url_portada: str | None = None, 
           editorial: str | None = None,
           prioridad_wishlist: int | None = None):

    isbn=_clean_optional(isbn)
    url_portada=_clean_optional(url_portada)
    editorial=_clean_optional(editorial)

    libro = libro_repository.get_by_id(id_libro)

    if libro is None:
        raise ValueError("Libro inexistente.")

    if isbn is not None:
        libro_isbn = libro_repository.get_by_isbn(isbn)
        if libro_isbn is not None and libro.id_libro != libro_isbn.id_libro:
            raise ValueError("Ya existe un libro con ese ISBN.")

    _obligatory(titulo=titulo, genero=genero, idioma=idioma)
    _general_checks(id_saga=id_saga, num_pag=num_pag, en_wishlist=en_wishlist, prioridad_wishlist=prioridad_wishlist)


    libro = _build_libro(
        id_libro=id_libro,
        id_saga=id_saga,
        titulo=titulo,
        isbn=isbn,
        num_pag=num_pag,
        genero=genero,
        idioma=idioma,
        sinopsis=sinopsis,
        fecha_public=fecha_public,
        url_portada=url_portada,
        editorial=editorial,
        en_wishlist=en_wishlist,
        prioridad_wishlist=prioridad_wishlist
    )
    return libro_repository.update(libro)

def delete(id_libro: int):
    if libro_repository.get_by_id(id_libro) is None:
        raise ValueError("Libro inexistente.")

    libro_repository.delete(id_libro)

def get_libro(id_libro: int):
    libro = libro_repository.get_by_id(id_libro)
    if libro is None:
        raise ValueError("Libro inexistente.")
    return libro

def get_all_libros():
    return libro_repository.get_all()

def search_by_saga(id_saga: int):
    if saga_repository.get_by_id(id_saga) is None:
        raise ValueError("Saga inexistente.")
    return libro_repository.get_by_saga(id_saga)

def search_by_title(titulo: str):
    return libro_repository.get_by_name(titulo)

def search_by_isbn(isbn: str):
    return libro_repository.get_by_isbn(isbn)

def filter_libro(generos: list[str] | None = None, idiomas: list[str] | None = None, editoriales: list[str] | None = None, en_wishlist: bool | None = None):

    filtros = []

    if generos: 
        filtros.append(or_(*[Libro.genero.contains(genero) for genero in generos]))
    if idiomas: 
        filtros.append(Libro.idioma.in_(idiomas))
    if editoriales: 
        filtros.append(Libro.editorial.in_(editoriales))
    if en_wishlist is not None: 
        filtros.append(Libro.en_wishlist==en_wishlist)

    return libro_repository.filter_libro(filtros)

# ===============================================================================================================

def _build_libro(id_saga: int | None, titulo: str, isbn: str | None, num_pag: int | None, genero: str, 
                 idioma: str, sinopsis: str | None, fecha_public: dt.date | None, url_portada: str | None, 
                 editorial: str | None, en_wishlist: bool, prioridad_wishlist: int | None, id_libro: int | None = None
                 ) -> Libro:
    return Libro(
        id_libro=id_libro,
        id_saga=id_saga,
        titulo=titulo,
        isbn=isbn,
        num_pag=num_pag,
        genero=genero,
        idioma=idioma,
        sinopsis=sinopsis,
        fecha_public=fecha_public,
        url_portada=url_portada,
        editorial=editorial,
        en_wishlist=en_wishlist,
        prioridad_wishlist=prioridad_wishlist
        )

def _general_checks(id_saga: int | None, num_pag: int | None, en_wishlist: bool, prioridad_wishlist: int | None):

    if id_saga is not None and saga_repository.get_by_id(id_saga) is None:
            raise ValueError("Saga inexistente.")

    if num_pag is not None and num_pag <= 0:
        raise ValueError("El libro tiene que tener un mínimo de 1 páginas.")

    if en_wishlist is False and prioridad_wishlist is not None:
        raise ValueError("Un libro que no esté en Wishlist no se puede priorizar.")
    if en_wishlist is True and prioridad_wishlist is not None:
        if prioridad_wishlist not in range(PRIORIDAD_WISHLIST_MIN, PRIORIDAD_WISHLIST_MAX+1):
            raise ValueError("Prioridad fuera de rango")

def _obligatory(titulo: str, genero: str, idioma: str):

    if not titulo.strip():
        raise ValueError("Título obligatorio")

    if not genero.strip():
        raise ValueError("Género obligatorio")

    if not idioma.strip(): 
        raise ValueError("Idioma obligatorio")

def _clean_optional(value: str | None) -> str | None:
    if value is not None:
        return value.strip() or None
    else:
        return None