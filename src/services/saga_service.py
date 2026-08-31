from models.saga import Saga
from repositories import saga_repository

def create(nom_saga: str):
    if saga_repository.get_by_exact_name(nom_saga):
        raise ValueError("Ya existe una saga con ese nombre.")
    
    return saga_repository.create(_build_saga(nom_saga=nom_saga))

def update(id_saga: int, nom_saga: str):
    saga = saga_repository.get_by_id(id_saga)

    if saga is None:
        raise ValueError("Saga inexistente.")

    saga_existe = saga_repository.get_by_exact_name(nom_saga)
    if saga_existe is not None and saga.id_saga != saga_existe.id_saga:
        raise ValueError("Ya existe una saga con ese nombre.")

    return saga_repository.update(_build_saga(id_saga=id_saga, nom_saga=nom_saga))

def delete(id_saga: int):
    if saga_repository.get_by_id(id_saga) is None:
        raise ValueError("Saga inexistente.")
    
    saga_repository.delete(id_saga)

def get_all_sagas():
    return saga_repository.get_all()

def search_by_name(nom_saga: str):
    return saga_repository.get_by_name(nom_saga)

# ===============================================================================================================

def _build_saga(nom_saga: str, id_saga: int | None = None) -> Saga:
    return Saga(id_saga=id_saga, nom_saga=nom_saga)