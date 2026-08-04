from sqlalchemy.orm import Session
from database.database import engine
from models.libro import Libro

def create(libro: Libro):
    with Session(engine) as session:
        try:
            session.add(libro)
            session.commit()
            return libro
        except Exception:
            session.rollback()
            raise

def get_by_id(id_libro: int):
    with Session(engine) as session:
        result = session.get(Libro, id_libro)
        return result

def get_by_name(titulo: str):
    with Session(engine) as session:
        result = session.query(Libro).filter(Libro.titulo.contains(titulo)).all()
        return result

def get_by_exact_name(titulo: str):
    with Session(engine) as session:
        result = session.query(Libro).filter(Libro.titulo==titulo).all()
        return result

def get_by_isbn(isbn: int):
    with Session(engine) as session:
        result = session.query(Libro).filter(Libro.isbn == isbn).one_or_none()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(Libro).all()
        return result

def delete(id_libro: int):
    with Session(engine) as session:
        try:
            session.query(Libro).filter_by(id_libro=id_libro).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise

def update(libro: Libro):
    with Session(engine) as session:
        try:
            libro_antiguo = session.get(Libro, libro.id_libro)
            libro_antiguo.id_saga = libro.id_saga
            libro_antiguo.titulo = libro.titulo
            libro_antiguo.isbn = libro.isbn
            libro_antiguo.num_pag = libro.num_pag
            libro_antiguo.genero = libro.genero
            libro_antiguo.idioma = libro.idioma
            libro_antiguo.sinopsis = libro.sinopsis
            libro_antiguo.fecha_public = libro.fecha_public
            libro_antiguo.url_portada = libro.url_portada
            libro_antiguo.editorial = libro.editorial
            libro_antiguo.en_wishlist = libro.en_wishlist
            libro_antiguo.prioridad_wishlist = libro.prioridad_wishlist
            session.commit()
        except Exception:
            session.rollback()
            raise