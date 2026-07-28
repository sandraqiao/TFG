from database.base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Text, Date

import datetime as dt

class Lectura(Base):
    __tablename__ = "lectura"

    id_lectura: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_libro: Mapped[int] = mapped_column(ForeignKey("libro.id_libro"), nullable=False)
    estado: Mapped[str] = mapped_column(String(255), nullable=False)
    valoracion: Mapped[int|None] = mapped_column(Integer, nullable=True)
    comentario: Mapped[str|None] = mapped_column(Text, nullable=True)
    fecha_ini: Mapped[dt.date] = mapped_column(Date, nullable=False)
    fecha_fin: Mapped[dt.date|None] = mapped_column(Date, nullable=True)
    formato: Mapped[str] = mapped_column(String(255), nullable=False)