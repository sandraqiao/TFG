import streamlit as st

st.set_page_config(
    page_title="Mi biblioteca"
)

biblioteca = st.Page("./pages/biblioteca.py", title="Biblioteca", icon="📖")
add_libro = st.Page("./pages/add_libro.py", title="Nuevo libro", visibility="hidden")
edit_libro = st.Page("./pages/edit_libro.py", title="Editar libro", visibility="hidden")
lecturas = st.Page("./pages/lecturas.py", title="Lecturas", icon="🔖")
add_lectura = st.Page("./pages/add_lectura.py", title="Nueva lectura", visibility="hidden")
edit_lectura = st.Page("./pages/edit_lectura.py", title="Editar lectura", visibility="hidden")
sagas = st.Page("./pages/sagas.py", title="Sagas", icon="📚")
autores = st.Page("./pages/autores.py", title="Autores", icon="👤")

pg = st.navigation(
    [biblioteca, add_libro, edit_libro, lecturas, add_lectura, edit_lectura, sagas, autores]
)

pg.run()