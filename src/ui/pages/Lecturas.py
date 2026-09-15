import streamlit as st
from datetime import date
from services import lectura_service, libro_service, autor_service, autor_libro_service
from utils.prints import *

st.set_page_config(
    page_title="Lecturas"
)

st.write("# 🔖 Lecturas")

col01, col02, col03 = st.columns([0.8, 0.1, 0.1])
with col01:
    st.write(" ")
with col02:
    st.write(" ")
    # if st.button("", icon=":material/filter_alt:")
with col03:
    if st.button("", icon=":material/add:"):
        st.switch_page("./pages/Add_lectura.py")


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
