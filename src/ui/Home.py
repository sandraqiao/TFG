import streamlit as st

st.set_page_config(
    page_title="Mi biblioteca"
)

biblioteca = st.Page("./pages/biblioteca.py", title="Biblioteca", icon="📖")
lecturas = st.Page("./pages/lecturas.py", title="Lecturas", icon="🔖")
add_lectura = st.Page("./pages/add_lectura.py", title="Nueva Lectura", icon="➕", visibility="hidden")

pg = st.navigation(
    [biblioteca, lecturas, add_lectura]
)

pg.run()