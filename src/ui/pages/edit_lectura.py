import streamlit as st
from ui.ui_selections import select_libro, select_estado, select_formato, select_valoracion, select_date, add_comentario
from services import lectura_service

st.set_page_config(
    page_title="Editar lectura"
)

st.write("# ✏️ Editar lectura")

# hay que añadir un estado que contenga lectura

id_libro = select_libro()

col11, col12 = st.columns(2)
with col11:
    estado = select_estado()
with col12:
    formato = select_formato()

valoracion = select_valoracion()

col21, col22 = st.columns(2)
with col21:
    fecha_ini = select_date("Inicio")
with col22:
    fecha_fin = select_date("Finalización")

comentario = add_comentario()

if st.button("Guardar", icon="💾"):
    lectura = lectura_service.create(
        id_libro=id_libro,
        estado=estado,
        formato=formato,
        fecha_ini=fecha_ini,
        fecha_fin=fecha_fin,
        valoracion=valoracion,
        comentario=comentario)
    st.session_state["lectura_creada"] = True
    st.switch_page("./pages/lecturas.py")