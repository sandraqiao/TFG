from database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, Boolean, Date, Text, SmallInteger

import datetime as dt

if TYPE_CHECKING:
    from models.autor_libro import AutorLibro
    from models.lectura import Lectura
    from models.historico_precio import HistoricoPrecio
    from models.saga import Libro

class Libro(Base):
    __tablename__ = "libro"

    id_libro: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_saga: Mapped[int|None] = mapped_column(ForeignKey("saga.id_saga"), nullable=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)
    isbn: Mapped[str|None] = mapped_column(String(20), nullable=True, unique=True)
    num_pag: Mapped[int|None] = mapped_column(Integer, nullable=True)
    genero: Mapped[str] = mapped_column(Text, nullable=False)
    idioma: Mapped[str] = mapped_column(String(50), nullable=False)
    sinopsis: Mapped[str|None] = mapped_column(Text, nullable=True)
    fecha_public: Mapped[dt.date|None] = mapped_column(Date, nullable=True)
    url_portada: Mapped[str|None] = mapped_column(Text, nullable=True)
    editorial: Mapped[str|None] = mapped_column(String(255), nullable=True)
    en_wishlist: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    prioridad_wishlist: Mapped[int|None] = mapped_column(SmallInteger, nullable=True)

    autoreslibros: Mapped[list[AutorLibro]] = relationship(back_populates="libro")
    precios: Mapped[list[HistoricoPrecio]] = relationship(back_populates="libro")
    lecturas: Mapped[list[Lectura]] = relationship(back_populates="libro")
    saga: Mapped[Libro] = relationship(back_populates="libros")