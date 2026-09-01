from sqlalchemy.orm import Session
from database.database import engine
from models.historico_precio import HistoricoPrecio

def create(precio: HistoricoPrecio):
    with Session(engine) as session:
        try:
            session.add(precio)
            session.commit()
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

def get_by_tienda(id_tienda: int):
    with Session(engine) as session:
        result = session.query(HistoricoPrecio).filter_by(id_tienda=id_tienda).all()
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

def update(precio: HistoricoPrecio):
    with Session(engine) as session:
        try:
            precio_antiguo = session.get(HistoricoPrecio, precio.id_precio)
            precio_antiguo.id_libro = precio.id_libro
            precio_antiguo.id_tienda = precio.id_tienda
            precio_antiguo.precio = precio.precio
            precio_antiguo.pct_descuento = precio.pct_descuento
            precio_antiguo.fecha_consulta = precio.fecha_consulta
            precio_antiguo.disponible = precio.disponible
            precio_antiguo.url_libro = precio.url_libro
            session.commit()
        except Exception:
            session.rollback()
            raise