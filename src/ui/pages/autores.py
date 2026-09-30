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
if st.session_state.get("autor_eliminado", False):
    st.toast("✔️ Autor eliminado correctamente")
    del st.session_state["autor_eliminado"]


# GET SAGAS A MOSTRAR
autores = sorted(autor_service.get_all_autores(), key=lambda autor: autor.nom_autor)

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
                st.write(saga.nom_saga)
            with col02:
                if st.button("", icon=":material/delete:", key=f"delete_{saga.id_saga}"):
                    confirm_delete(saga.id_saga)

        if libros:
            portadas = st.columns(len(libros), gap="xsmall")
            for column, libro in zip(portadas, libros):
                with column:
                    if libro.url_portada:
                        st.image(libro.url_portada, width=150)
                    else: 
                        st.write(libro.titulo)
                        st.caption("[Sin portada]")