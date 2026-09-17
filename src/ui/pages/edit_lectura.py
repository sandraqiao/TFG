import streamlit as st
from ui.ui_selections import select_libro, select_estado, select_formato, select_valoracion, select_date, add_comentario
from services import lectura_service

st.set_page_config(
    page_title="Editar lectura"
)

st.write("# ✏️ Editar lectura")

edit_lectura_id = st.session_state["edit_lectura_id"]
lectura = lectura_service.get_by_id(edit_lectura_id)

id_libro = select_libro(lectura.id_libro)

col11, col12 = st.columns(2)
with col11:
    estado = select_estado(lectura.estado)
with col12:
    formato = select_formato(lectura.formato)

valoracion = select_valoracion(lectura.valoracion)

col21, col22 = st.columns(2)
with col21:
    fecha_ini = select_date("Inicio", lectura.fecha_ini)
with col22:
    fecha_fin = select_date("Finalización", lectura.fecha_fin)

comentario = add_comentario(lectura.comentario)

if st.button("Guardar", icon="💾"):
    lectura = lectura_service.update(
        id_lectura=edit_lectura_id,
        id_libro=id_libro,
        estado=estado,
        formato=formato,
        fecha_ini=fecha_ini,
        fecha_fin=fecha_fin,
        valoracion=valoracion,
        comentario=comentario)
    st.session_state["lectura_editada"] = True
    st.switch_page("./pages/lecturas.py")