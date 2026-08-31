from models.autor import Autor
from repositories import autor_repository

def create(nom_autor: str):
    if autor_repository.get_by_exact_name(nom_autor):
        raise ValueError("Ya existe un autor con ese nombre.")

    return autor_repository.create(_build_autor(nom_autor))

def update(id_autor: int, nom_autor: str):
    autor = autor_repository.get_by_id(id_autor)

    if autor is None:
        raise ValueError("Autor inexistente.")

    autor_existe = autor_repository.get_by_exact_name(nom_autor)
    if autor_existe is not None and autor.id_autor != autor_existe.id_autor:
        raise ValueError("Ya existe un autor con ese nombre.")

    return autor_repository.update(_build_autor(id_autor=id_autor, nom_autor=nom_autor))

def delete(id_autor: int):
    if autor_repository.get_by_id(id_autor) is None:
        raise ValueError("Autor inexistente.")

    autor_repository.delete(id_autor)

def get_all_autores():
    return autor_repository.get_all()

# ===============================================================================================================

def _build_autor(nom_autor: str, id_autor: int | None = None) -> Autor:
    return Autor(id_autor=id_autor, nom_autor=nom_autor)