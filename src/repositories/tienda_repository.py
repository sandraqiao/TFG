from sqlalchemy.orm import Session
from database.database import engine
from models.tienda import Tienda

def create(tienda: Tienda):
    with Session(engine) as session:
        try:
            session.add(tienda)
            session.commit()
            return tienda
        except Exception:
            session.rollback()
            raise

def get_by_id(id_tienda: int):
    with Session(engine) as session:
        result = session.get(Tienda, id_tienda)
        return result

def get_by_name(nom_tienda: str):
    with Session(engine) as session:
        result = session.query(Tienda).filter(Tienda.nom_tienda.contains(nom_tienda)).all()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(Tienda).all()
        return result

def delete(id_tienda: int):
    with Session(engine) as session:
        try:
            session.query(Tienda).filter_by(id_tienda=id_tienda).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise

def update(tienda: Tienda):
    with Session(engine) as session:
        try:
            tienda_antigua = session.get(Tienda, tienda.id_tienda)
            tienda_antigua.nom_tienda = tienda.nom_tienda
            tienda_antigua.url_tienda = tienda.url_tienda
            session.commit()
        except Exception:
            session.rollback()
            raise