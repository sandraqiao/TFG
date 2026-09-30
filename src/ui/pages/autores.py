import streamlit as st
from services import autor_service, libro_service, autor_libro_service

@st.dialog("Seguro que quieres borrar al autor?", dismissible=False, icon="⚠️")
def confirm_delete(id_autor: int) -> bool:
    st.write("Esta acción no se puede deshacer")
    st.write("Los libros escritos por este autor pasarán a no tener informado el campo autor")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Si, bórralo"):
            autor_service.delete(id_autor)
            st.session_state["autor_eliminado"] = True
            st.rerun()
    with col2:
        if st.button("No, me arrepiento"):
            st.rerun()

# ==========================================================================================================

st.set_page_config(
    page_title="Autores"
)

st.write("# 👤 Autores")

# STATES EDICIONES
if st.session_state.get("autor_creado", False):
    st.toast("✔️ Autor creado correctamente")
    del st.session_state["autor_creado"]
if st.session_state.get("autor_eliminado", False):
    st.toast("✔️ Autor eliminado correctamente")
    del st.session_state["autor_eliminado"]

# NEW AUTOR
new_autor = st.text_input("Añadir nuevo autor", placeholder="Nombre")
with st.container(horizontal=True, horizontal_alignment="right"):
    if st.button("Guardar", icon="💾") and new_autor:
        autor_service.create(new_autor)
        st.session_state["autor_creado"] = True
        st.rerun()

# GET AUTORES A MOSTRAR
autores = sorted(autor_service.get_all_autores(), key=lambda autor: autor.nom_autor)

st.divider()
if not autores:
    st.write("## 🕸️ No hay autores registrados 🕸️")

else:
    for autor in autores:

        # VARIABLES
        autor_libros = autor_libro_service.search_by_autor(autor.id_autor)

        # IMPRESIONES
        with st.container(border=True):

            col01, col02 = st.columns([0.9, 0.1])
            with col01:
                st.write(autor.nom_autor)
            with col02:
                if st.button("", icon=":material/delete:", key=f"delete_{autor.id_autor}"):
                    confirm_delete(autor.id_autor)

            if autor_libros:
                portadas = st.columns(len(autor_libros), gap="xsmall")
                for column, autor_libro in zip(portadas, autor_libros):
                    libro = libro_service.get_libro(autor_libro.id_libro)
                    with column:
                        if libro.url_portada:
                            st.image(libro.url_portada, width=150)
                        else:
                            st.write(libro.titulo)
                            st.caption("[Sin portada]")