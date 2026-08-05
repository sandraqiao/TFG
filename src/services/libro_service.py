from models.libro import Libro
from repositories import libro_repository, saga_repository
import datetime as dt

def create(id_saga: int | None, titulo: str, isbn: str | None, num_pag: int | None, genero: str, 
                 idioma: str, sinopsis: str | None, fecha_public: dt.date | None, url_portada: str | None, 
                 editorial: str | None, en_wishlist: bool, prioridad_wishlist: int | None):

    if isbn is not None and libro_repository.get_by_isbn(isbn):
        raise ValueError("ISBN ya existente.")

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

def update(id_libro: int, id_saga: int | None, titulo: str, isbn: str | None, num_pag: int | None, genero: str, 
            idioma: str, sinopsis: str | None, fecha_public: dt.date | None, url_portada: str | None, 
            editorial: str | None, en_wishlist: bool, prioridad_wishlist: int | None):

    libro = libro_repository.get_by_id(id_libro)

    if libro is None:
        raise ValueError("Libro inexistente.")

    if isbn is not None:
        libro_isbn = libro_repository.get_by_isbn(isbn)
        if libro_isbn is not None and libro.id_libro != libro_isbn.id_libro:
            raise ValueError("Ya existe un libro con ese ISBN.")

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
    if en_wishlist is True and prioridad_wishlist is None:
        prioridad_wishlist = 0