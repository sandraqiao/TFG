from database.base import Base
from models.libro import Libro

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class Saga(Base):
    __tablename__ = "saga"

    id_saga: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_saga: Mapped[str] = mapped_column(String(255), nullable=False)
    
    libros: Mapped[list["Libro"]] = relationship()