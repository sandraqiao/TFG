from sqlalchemy.orm import Session
from database.database import engine
from models.historico_precio import HistoricoPrecio

def create(precio: HistoricoPrecio):
    with Session(engine) as session:
        try:
            session.add(precio)
            session.commit()
            session.refresh(precio)
            return precio
        except Exception:
            session.rollback()
            raise

def get_by_id(id_precio: int):
    with Session(engine) as session:
        result = session.get(HistoricoPrecio, id_precio)
        return result

def get_by_libro(id_libro: int):
    with Session(engine) as session:
        result = session.query(HistoricoPrecio).filter_by(id_libro=id_libro).all()
        return result

def get_by_nom_tienda(nom_tienda: str):
    with Session(engine) as session:
        result = session.query(HistoricoPrecio).filter_by(nom_tienda=nom_tienda).all()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(HistoricoPrecio).all()
        return result

def filter_historico_precio(filtros):
    with Session(engine) as session:
        result = session.query(HistoricoPrecio).filter(*filtros).all()
    return result

def delete(id_precio: int):
    with Session(engine) as session:
        try:
            session.query(HistoricoPrecio).filter_by(id_precio=id_precio).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise