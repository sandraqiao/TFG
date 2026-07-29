from database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text

if TYPE_CHECKING:
    from models.historico_precio import HistoricoPrecio

class Tienda(Base):
    __tablename__ = "tienda"

    id_tienda: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_tienda: Mapped[str] = mapped_column(String(255), nullable=False)
    url_tienda: Mapped[str] = mapped_column(Text, nullable=False)

    precios: Mapped[list[HistoricoPrecio]] = relationship(back_populates="tienda")