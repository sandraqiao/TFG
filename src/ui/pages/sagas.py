import streamlit as st
from services import saga_service, libro_service

@st.dialog("Seguro que quieres borrar la saga?", dismissible=False, icon="⚠️")
def confirm_delete(id_saga: int) -> bool:
    st.write("Esta acción no se puede deshacer")
    st.write("Los libros pertenecientes a esta saga pasarán a no tener informado el campo saga")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Si, bórralo"):
            saga_service.delete(id_saga)
            st.session_state["saga_eliminada"] = True
            st.rerun()
    with col2:
        if st.button("No, me arrepiento"):
            st.rerun()

# ==========================================================================================================

st.set_page_config(
    page_title="Sagas"
)

st.write("# 📚 Sagas")

# STATES EDICIONES
if st.session_state.get("saga_creada", False):
    st.toast("✔️ Saga creada correctamente")
    del st.session_state["saga_creada"]
if st.session_state.get("saga_eliminada", False):
    st.toast("✔️ Saga eliminada correctamente")
    del st.session_state["saga_eliminada"]

# NEW SAGA
new_saga = st.text_input("Añadir nueva saga", placeholder="Nombre de la saga")
with st.container(horizontal=True, horizontal_alignment="right"):
    if st.button("Guardar", icon="💾") and new_saga:
        saga_service.create(new_saga)
        st.session_state["saga_creada"] = True
        st.rerun()

# GET SAGAS A MOSTRAR
sagas = sorted(saga_service.get_all_sagas(), key=lambda saga: saga.nom_saga)

st.divider()
if not sagas:
    st.write("## 🕸️ No hay sagas registradas 🕸️")

else:
    st.write("")
    for saga in sagas:

        # VARIABLES
        libros = libro_service.search_by_saga(saga.id_saga)

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