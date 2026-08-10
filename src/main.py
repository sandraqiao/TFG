# ==========================================================================================================
# CONEXIÓN CON STREAMLIT
# ==========================================================================================================

# import streamlit as st

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
import models
from database.base import Base
from database.database import engine

Base.metadata.create_all(engine)

# QUERY PARA BORRADO: DROP SCHEMA public CASCADE; CREATE SCHEMA public;

# ==========================================================================================================
# 
# ==========================================================================================================