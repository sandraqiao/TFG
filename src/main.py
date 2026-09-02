# ==========================================================================================================
# ACTIVACIÓN ENTORNO VIRUTAL
# ==========================================================================================================
# .\.venv\Scripts\Activate.ps1

# ==========================================================================================================
# CONEXIÓN CON STREAMLIT
# ==========================================================================================================

# import streamlit as st
# st.title("Mi biblioteca")

# st.set_page_config(
#     page_title="My Streamlit App",
#     page_icon=":rocket:",
#     layout="wide"
# )

# st.title("Welcome to My Streamlit App")

# st.write("This is a simple Streamlit application that demonstrates how to create a web app using Python.")

# ==========================================================================================================
# CREACIÓN DE TABLAS QUE NO EXISTAN
# ==========================================================================================================
# import models
# from database.base import Base
# from database.database import engine

# Base.metadata.create_all(engine)

# QUERY PARA BORRADO: DROP SCHEMA public CASCADE; CREATE SCHEMA public;

# ==========================================================================================================
# FILTROS
# ==========================================================================================================

# import models
# import services

# resultados = services.historico_precio_service.filter_historico(
#     libros=[1, 4],
#     # tiendas=[1]
#     # fecha_min='2019-12-01',
#     # fecha_max='2019-12-04',
#     precio_min=10,
#     precio_max=20
# )

# ==========================================================================================================
# 
# ==========================================================================================================
from scraper.casa_del_libro import get_url

get_url("https://www.casadellibro.com/libro-nacidos-de-la-bruma-trilogia-original-mistborn-1/9788413149813/16532594")