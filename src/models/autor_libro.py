from database.base import Base
from models.libro import Libro
from models.autor import Autor

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

class AutorLibro(Base):
    __tablename__ = "autor_libro"

    id_libro: Mapped[int] = mapped_column(ForeignKey("libro.id_libro"), primary_key=True)
    id_autor: Mapped[int] = mapped_column(ForeignKey("autor.id_autor"), primary_key=True)

    libro: Mapped[Libro] = relationship(back_populates="autoreslibros")
    autor: Mapped[Autor] = relationship(back_populates="autoreslibros")