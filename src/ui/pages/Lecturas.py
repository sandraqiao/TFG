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

def filtro_popover():
    estados = filtrado(constants.FILTROS_LECTURAS[0])
    st.divider()
    valoraciones = filtrado(constants.FILTROS_LECTURAS[1])
    st.divider()
    formatos = filtrado(constants.FILTROS_LECTURAS[2])

    with st.container(horizontal=True, horizontal_alignment="right"):
        if st.button("Aplicar"):
            st.session_state["filtros_lecturas"] = {
                "estados": estados,
                "valoraciones": valoraciones,
                "formatos": formatos
            }
            st.rerun()

def filtrado(to_filter: str):
    if to_filter == constants.FILTROS_LECTURAS[0]:
        options = constants.ESTADO
    elif to_filter == constants.FILTROS_LECTURAS[1]:
        options = list(range(constants.VALORACION_MIN, constants.VALORACION_MAX+1))
    elif to_filter== constants.FILTROS_LECTURAS[2]:
        options = constants.FORMATO

    st.write(to_filter)

    result = []
    for i, option in enumerate(options):
        actual = st.checkbox(f"{option}")
        if actual:
            result.append(f"{options[i]}")
    return result


# ==========================================================================================================

st.set_page_config(
    page_title="Lecturas"
)

st.write("# 📓 Lecturas")

# STATES EDICIONES
if st.session_state.get("lectura_creada", False):
    st.toast("✔️ Lectura creada correctamente")
    del st.session_state["lectura_creada"]

if st.session_state.get("lectura_editada", False):
    st.toast("✔️ Lectura editada correctamente")
    del st.session_state["lectura_editada"]

if st.session_state.get("lectura_eliminada", False):
    st.toast("❌ Lectura eliminada correctamente")
    del st.session_state["lectura_eliminada"]


# FILTER Y ADD LECTURAS
with st.container(horizontal=True, horizontal_alignment="right"):
    with st.popover("", icon=":material/filter_alt:"):
        filtro_popover()
    if st.button("", icon=":material/add:"):
        st.switch_page("./pages/add_lectura.py")

# GET LECTURAS A MOSTRAR
filtros = st.session_state.get("filtros_lecturas", None)
if filtros:
    lecturas = lectura_service.filter_lectura(estados=filtros["estados"], valoraciones=filtros["valoraciones"], formatos=filtros["formatos"])
else:
    lecturas = lectura_service.get_all_lecturas()


# LISTADO DE LECTURAS
if lecturas is None:
    st.write("## 🕸️ No hay lecturas registradas 🕸️")
else:

    for lectura in lecturas:

        # VARIABLES
        libro = libro_service.get_libro(lectura.id_libro)
        autores = autor_libro_service.get_autores_by_libro(libro.id_libro)

        # IMPRESIONES
        with st.expander(f"{codigo_color_estado(lectura.estado)} {titulo_autor(libro.titulo, autores)}"):

            col11, col12 = st.columns(2)
            col21, col22 = st.columns(2)

            with col11:
                st.write(f"Estado: {lectura.estado}")
            with col12:
                st.write(f"Formato: {lectura.formato}")
            with col21:
                st.write(f"Valoración: {estrellas(lectura.valoracion)}")
            with col22:
                st.write(f"{fechas(lectura.fecha_ini, lectura.fecha_fin)}")

            if lectura.comentario:
                st.write(f"{lectura.comentario}")

            with st.container(horizontal=True, horizontal_alignment="right"):

                if st.button("", icon=":material/edit:", key=f"edit_{lectura.id_lectura}"):
                    st.session_state["edit_lectura_id"] = lectura.id_lectura
                    st.switch_page("./pages/edit_lectura.py")

                if st.button("", icon=":material/delete:", key=f"delete_{lectura.id_lectura}"):
                    confirm_delete(lectura.id_lectura)
