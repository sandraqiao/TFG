from database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

if TYPE_CHECKING:
    from models.libro import Libro

class Libro(Base):
    __tablename__ = "saga"

    id_saga: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_saga: Mapped[str] = mapped_column(String(255), nullable=False)
    
    libros: Mapped[list["Libro"]] = relationship(back_populates="saga")