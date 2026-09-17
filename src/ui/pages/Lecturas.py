import streamlit as st
from services import lectura_service, libro_service, autor_libro_service
from utils.prints import *

@st.dialog("Confirma si quieres borrar la lectura", dismissible=False, icon="⚠️")
def confirm_delete(id_lectura: int) -> bool:
    st.write("Esta acción no se puede deshacer")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Si, borra"):
            lectura_service.delete(id_lectura)
            st.session_state["lectura_eliminada"] = True
            st.rerun()
    with col2:
        if st.button("No, me arrepiento"):
            st.rerun()

# ==========================================================================================================

st.set_page_config(
    page_title="Lecturas"
)

st.write("# 📓 Lecturas")


# STATES
if st.session_state.get("lectura_creada", False):
    st.toast("✔️ Lectura creada correctamente")
    del st.session_state["lectura_creada"]

if st.session_state.get("lectura_editada", False):
    st.toast("✔️ Lectura editada correctamente")
    del st.session_state["lectura_editada"]

if st.session_state.get("lectura_eliminada", False):
    st.toast("❌ Lectura eliminada correctamente")
    del st.session_state["lectura_eliminada"]


col01, col02, col03 = st.columns([0.8, 0.1, 0.1])
with col01:
    st.write(" ")
with col02:
    if st.button("", icon=":material/filter_alt:"):
        st.write("filter")
with col03:
    if st.button("", icon=":material/add:"):
        st.switch_page("./pages/add_lectura.py")

lecturas = lectura_service.get_all_lecturas()

if lecturas is None:
    st.write("## 🕸️ No hay lecturas registradas 🕸️")

else:

    for lectura in lecturas:

        # VARIABLES IMPORTANTES DE CADA LECTURA
        libro = libro_service.get_libro(lectura.id_libro)
        autores = autor_libro_service.get_autores_by_libro(libro.id_libro)

        # IMPRESIONES
        with st.expander(f"{codigo_color_estado(lectura.estado)} {titulo_autor(libro.titulo, autores)}"):

            col11, col12 = st.columns(2)
            with col11:
                st.write(f"Estado: {lectura.estado}")
            with col12:
                st.write(f"Formato: {lectura.formato}")

            col21, col22 = st.columns(2)
            with col21:
                st.write(f"Valoración: {estrellas(lectura.valoracion)}")
            with col22:
                st.write(f"{fechas(lectura.fecha_ini, lectura.fecha_fin)}")

            if lectura.comentario:
                st.write(f"{lectura.comentario}")

            col31, col32, col33 = st.columns([0.8, 0.1, 0.1])
            with col31:
                st.write("")
            with col32:
                if st.button("", icon=":material/edit:", key=f"edit_{lectura.id_lectura}"):
                    st.session_state["edit_lectura_id"] = lectura.id_lectura
                    st.switch_page("./pages/edit_lectura.py")
            with col33:
                if st.button("", icon=":material/delete:", key=f"delete_{lectura.id_lectura}"):
                    confirm_delete(lectura.id_lectura)


