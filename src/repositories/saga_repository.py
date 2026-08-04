from sqlalchemy.orm import Session
from database.database import engine
from models.saga import Saga

def create(saga: Saga):
    with Session(engine) as session:
        try:
            session.add(saga)
            session.commit()
            return saga
        except Exception:
            session.rollback()
            raise

def get_by_id(id_saga: int):
    with Session(engine) as session:
        result = session.get(Saga, id_saga)
        return result

def get_by_name(nom_saga: str):
    with Session(engine) as session:
        result = session.query(Saga).filter(Saga.nom_saga.contains(nom_saga)).all()
        return result

def get_by_exact_name(nom_saga: str):
    with Session(engine) as session:
        result = session.query(Saga).filter(Saga.nom_saga==nom_saga).one_or_none()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(Saga).all()
        return result

def delete(id_saga: int):
    with Session(engine) as session:
        try:
            session.query(Saga).filter_by(id_saga=id_saga).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise

def update(saga: Saga):
    with Session(engine) as session:
        try:
            saga_antigua = session.get(Saga, saga.id_saga)
            saga_antigua.nom_saga = saga.nom_saga
            session.commit()
        except Exception:
            session.rollback()
            raise