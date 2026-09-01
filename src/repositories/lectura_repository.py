from sqlalchemy.orm import Session
from database.database import engine
from models.lectura import Lectura

def create(lectura: Lectura):
    with Session(engine) as session:
        try:
            session.add(lectura)
            session.commit()
            return lectura
        except Exception:
            session.rollback()
            raise

def get_by_id(id_lectura: int):
    with Session(engine) as session:
        result = session.get(Lectura, id_lectura)
        return result

def get_by_libro(id_libro: int):
    with Session(engine) as session:
        result = session.query(Lectura).filter_by(id_libro=id_libro).all()
        return result

def get_by_estado(estado: str):
    with Session(engine) as session:
        result = session.query(Lectura).filter_by(estado=estado).all()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(Lectura).all()
        return result

def filter_lectura(filtros):
    with Session(engine) as session:
        result = session.query(Lectura).filter(*filtros).all()
    return result

def delete(id_lectura: int):
    with Session(engine) as session:
        try:
            session.query(Lectura).filter_by(id_lectura=id_lectura).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise

def update(lectura: Lectura):
    with Session(engine) as session:
        try:
            lectura_antigua = session.get(Lectura, lectura.id_lectura)
            lectura_antigua.id_libro = lectura.id_libro
            lectura_antigua.estado = lectura.estado
            lectura_antigua.valoracion = lectura.valoracion
            lectura_antigua.comentario = lectura.comentario
            lectura_antigua.fecha_ini = lectura.fecha_ini
            lectura_antigua.fecha_fin = lectura.fecha_fin
            lectura_antigua.formato = lectura.formato
            session.commit()
        except Exception:
            session.rollback()
            raise