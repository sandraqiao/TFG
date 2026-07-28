from database.base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class Autor(Base):
    __tablename__ = "autor"

    id_autor: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_autor: Mapped[str] = mapped_column(String(255), nullable=False)