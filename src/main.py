# CONEXIÓN CON STREAMLIT

# import streamlit as st

# st.set_page_config(
#     page_title="My Streamlit App",
#     page_icon=":rocket:",
#     layout="wide"
# )

# st.title("Welcome to My Streamlit App")

# st.write("This is a simple Streamlit application that demonstrates how to create a web app using Python.")

# ==========================================================================================================

#  PRUEBAS DE LOS MODELOS

# from models.libro import Libro
# from models.saga import Saga
# from models.autor import Autor
# from models.lectura import Lectura
# from models.tienda import Tienda
# from models.historico_precio import HistoricoPrecio
# from models.autor_libro import AutorLibro

# print("Todo fofa")

# ==========================================================================================================

# COMPROBACIÓN QUE METADATA TIENE TODOS LOS MODELOS
# import models
# from database.base import Base
# from database.database import engine

# Base.metadata.create_all(engine)

# ==========================================================================================================

# CREAR UN LIBRO DE PRUEBA
from sqlalchemy.orm import Session
from database.database import engine
from models.libro import Libro

prueba = Libro(titulo="prueba", genero="probando", idioma="esp", en_wishlist=False)

with Session(engine) as session:
    session.begin()
    try:
        session.add(prueba)
    except:
        session.rollback()
        raise
    else:
        session.commit()