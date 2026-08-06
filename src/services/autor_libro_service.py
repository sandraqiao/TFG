from models.autor_libro import AutorLibro
from repositories import autor_libro_repository, autor_repository, libro_repository

def create(id_libro: int, id_autor: int):

    _general_checks(id_libro=id_libro, id_autor=id_autor)

    if autor_libro_repository.get_by_autor_libro(id_libro=id_libro, id_autor=id_autor) is not None:
        raise ValueError("Relación autor-libro existente.")

    return autor_libro_repository.create(_build_autor_libro(id_libro=id_libro, id_autor=id_autor))

def delete(id_libro: int, id_autor: int):

    _general_checks(id_libro=id_libro, id_autor=id_autor)

    if autor_libro_repository.get_by_autor_libro(id_libro=id_libro, id_autor=id_autor) is None:
        raise ValueError("Relación autor-libro inexistente.")

    autor_libro_repository.delete(id_libro=id_libro, id_autor=id_autor)

# ===============================================================================================================

def _build_autor_libro(id_libro: int, id_autor: int) -> AutorLibro:
    return AutorLibro(id_libro=id_libro, id_autor=id_autor)

def _general_checks(id_libro: int, id_autor: int):
    if libro_repository.get_by_id(id_libro) is None:
        raise ValueError("Libro inexistente.")
    
    if autor_repository.get_by_id(id_autor) is None:
        raise ValueError("Autor inexistente.")