from sqlalchemy.orm import Session
from database.database import engine
from models.autor import Autor

def create(autor: Autor):
    with Session(engine) as session:
        try:
            session.add(autor)
            session.commit()
            return autor
        except Exception:
            session.rollback()
            raise

def get_by_id(id_autor: int):
    with Session(engine) as session:
        result = session.get(Autor, id_autor)
        return result

def get_by_name(nom_autor: str):
    with Session(engine) as session:
        result = session.query(Autor).filter(Autor.nom_autor.contains(nom_autor)).all()
        return result

def get_all():
    with Session(engine) as session:
        result = session.query(Autor).all()
        return result

def delete(id_autor: int):
    with Session(engine) as session:
        try:
            session.query(Autor).filter_by(id_autor=id_autor).delete()
            session.commit()
        except Exception:
            session.rollback()
            raise

def update(autor: Autor):
    with Session(engine) as session:
        try:
            autor_antiguo = session.get(Autor, autor.id_autor)
            autor_antiguo.nom_autor = autor.nom_autor
            session.commit()
        except Exception:
            session.rollback()
            raise