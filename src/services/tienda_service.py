from models.tienda import Tienda
from repositories import tienda_repository

def create(nom_tienda: str, url_tienda: str):
    if tienda_repository.get_by_exact_name(nom_tienda):
        raise ValueError("Ya existe una tienda con ese nombre.")

    return tienda_repository.create(_build_tienda(nom_tienda=nom_tienda, url_tienda=url_tienda))

def update(id_tienda: int, nom_tienda: str, url_tienda: str):
    tienda = tienda_repository.get_by_id(id_tienda)

    if tienda is None:
        raise ValueError("Tienda inexistente.")

    tienda_existente = tienda_repository.get_by_exact_name(nom_tienda)
    if tienda_existente is not None and tienda.id_tienda != tienda_existente.id_tienda:
        raise ValueError("Ya existe una tienda con ese nombre.")

    return tienda_repository.update(_build_tienda(id_tienda=id_tienda, nom_tienda=nom_tienda, url_tienda=url_tienda))

def delete(id_tienda: int):
    if tienda_repository.get_by_id(id_tienda) is None:
        raise ValueError("Tienda inexistente.")

    tienda_repository.delete(id_tienda)

def get_all_tiendas():
    return tienda_repository.get_all()

def search_by_name(nom_tienda: str):
    return tienda_repository.get_by_name(nom_tienda)

# ===============================================================================================================

def _build_tienda(nom_tienda: str, url_tienda: str | None, id_tienda: int | None = None) -> Tienda:
    return Tienda(id_tienda=id_tienda, nom_tienda=nom_tienda, url_tienda=url_tienda)