import streamlit as st

st.set_page_config(
    page_title="Mi biblioteca"
)

# ==========================================================================================================
# NAVEGACIÓN
# ==========================================================================================================

biblioteca = st.Page("./pages/Biblioteca.py", title="Biblioteca", icon="📖")
lecturas = st.Page("./pages/Lecturas.py", title="Lecturas", icon="🔖")

pg = st.navigation(
    [biblioteca, lecturas]
)

pg.run()