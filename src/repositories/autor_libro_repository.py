from sqlalchemy.orm import Session
from database.database import engine
from models.autor_libro import AutorLibro

def create(autor_libro: AutorLibro):
    with Session(engine) as session:
        try:
            session.add(autor_libro)
            session.commit()
            return autor_libro
        except Exception:
            session.rollback()
            raise

def get_by_autor_libro(id_libro: int, id_autor: int):
    with Session(engine) as session:
        result = session.query(AutorLibro).filter_by(id_autor=id_autor, id_libro=id_libro).one_or_none()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(AutorLibro).all()
        return result

def delete(id_libro: int, id_autor: int):
    with Session(engine) as session:
        try:
            session.query(AutorLibro).filter_by(id_autor=id_autor, id_libro=id_libro).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise