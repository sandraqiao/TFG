from database.base import Base
from models.libro import Libro
from models.tienda import Tienda

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric, Date, Boolean, Text

from decimal import Decimal
import datetime as dt

class HistoricoPrecio(Base):
    __tablename__ = "historico_precio"

    id_precio: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_libro: Mapped[int] = mapped_column(ForeignKey("libro.id_libro"), nullable=False)
    id_tienda: Mapped[int] = mapped_column(ForeignKey("tienda.id_tienda"), nullable=False)
    precio: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    pct_descuento: Mapped[Decimal|None] = mapped_column(Numeric(5,2), nullable=True)
    fecha_consulta: Mapped[dt.date] = mapped_column(Date, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False)
    url_libro: Mapped[str] = mapped_column(Text, nullable=False)

    libro: Mapped[Libro] = relationship(back_populates="precios")
    tienda: Mapped[Tienda] = relationship(back_populates="precios")