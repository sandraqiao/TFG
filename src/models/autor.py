from database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

if TYPE_CHECKING:
    from models.autor_libro import AutorLibro

class Autor(Base):
    __tablename__ = "autor"

    id_autor: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_autor: Mapped[str] = mapped_column(String(255), nullable=False)

    autoreslibros: Mapped[list[AutorLibro]] = relationship(back_populates="autor")