from database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, Boolean, Date, Text, SmallInteger

import datetime as dt

if TYPE_CHECKING:
    from models.autor_libro import AutorLibro
    from models.lectura import Lectura
    from models.historico_precio import HistoricoPrecio
    from models.saga import Libro

class Libro(Base):
    __tablename__ = "libro"

    __table_args__ = (
        CheckConstraint("num_pag IS NULL OR num_pag > 0", name="check_num_pag"),
        CheckConstraint("prioridad_wishlist IS NULL OR prioridad_wishlist BETWEEN 0 AND 5", name="check_prioridad_wishlist")
    )

    id_libro: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_saga: Mapped[int|None] = mapped_column(ForeignKey("saga.id_saga", ondelete="SET NULL"), nullable=True)
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

    autoreslibros: Mapped[list["AutorLibro"]] = relationship(back_populates="libro")
    precios: Mapped[list["HistoricoPrecio"]] = relationship(back_populates="libro")
    lecturas: Mapped[list["Lectura"]] = relationship(back_populates="libro")
    saga: Mapped["Libro"] = relationship(back_populates="libros")