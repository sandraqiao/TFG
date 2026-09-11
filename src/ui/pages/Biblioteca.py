import streamlit as st
from services import libro_service

st.set_page_config(
    page_title="Biblioteca"
)

st.write("# Biblioteca")

# ==========================================================================================================

# libros = libro_service.get_all_libros()

# if libros:
#     for libro in libros:
#         st.write(f"## {libro.titulo}")
#         # st.write(libro.)
#         # st.write("★☆⭐🌟")
# else: 
#     st.write("🕸️No hay libros en tu biblioteca🕸️")