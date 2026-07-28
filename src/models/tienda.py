from database.base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text

class Tienda(Base):
    __tablename__ = "tienda"

    id_tienda: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_tienda: Mapped[str] = mapped_column(String(255), nullable=False)
    url_tienda: Mapped[str] = mapped_column(Text, nullable=False)