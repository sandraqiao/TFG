from database.base import Base
from typing import TYPE_CHECKING
from utils import constants

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, Text, Date

import datetime as dt

if TYPE_CHECKING:
    from models.libro import Libro

ESTADOS = ", ".join(f"'{e}'" for e in constants.ESTADO)
FORMATOS = ", ".join(f"'{f}'" for f in constants.FORMATO)


class Lectura(Base):
    __tablename__ = "lectura"

    __table_args__ = (
        CheckConstraint("fecha_fin >= fecha_ini", name="check_fechas_ini_fin"),
        CheckConstraint(f"estado IN ({ESTADOS})", name="check_estados"),
        CheckConstraint(f"formato IN ({FORMATOS})", name="check_formatos"),
        CheckConstraint(f"valoracion IS NULL OR (estado IN('{constants.ESTADO[1]}', '{constants.ESTADO[2]}') AND valoracion BETWEEN {constants.VALORACION_MIN} AND {constants.VALORACION_MAX})", name="check_valoracion")
    )

    id_lectura: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_libro: Mapped[int] = mapped_column(ForeignKey("libro.id_libro", ondelete="CASCADE"), nullable=False)
    estado: Mapped[str] = mapped_column(String(255), nullable=False)
    valoracion: Mapped[int|None] = mapped_column(Integer, nullable=True)
    comentario: Mapped[str|None] = mapped_column(Text, nullable=True)
    fecha_ini: Mapped[dt.date] = mapped_column(Date, nullable=False)
    fecha_fin: Mapped[dt.date|None] = mapped_column(Date, nullable=True)
    formato: Mapped[str] = mapped_column(String(255), nullable=False)

    libro: Mapped["Libro"] = relationship(back_populates="lecturas")