import datetime as dt

from sqlalchemy import Integer, String, Boolean, Date, Text, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Libro(Base):
    __tablename__ = "libro"

    id_libro: Mapped[int] = mapped_column(Integer, primary_key=True)
    # id_saga: Mapped[int]
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
