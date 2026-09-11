import streamlit as st
import datetime as dt
from services import lectura_service, libro_service

st.set_page_config(
    page_title="Lecturas"
)

st.write("# Lecturas")

# ==========================================================================================================

lecturas = lectura_service.get_all_lecturas()

if lecturas:
    for lectura in lecturas:
        libro = libro_service.get_libro(lectura.id_libro)


        # VALORACIÓN DE LECTURA
        estrellas = ""
        if lectura.valoracion:
            for i in range(10):
                if i < lectura.valoracion:
                    estrellas += "★"
                else:
                    estrellas += "☆"
                estrellas += " "
        else:
            estrellas = "☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆"


        # FECHAS DE LECTURA
        fechas = ""
        if lectura.fecha_fin:
            fechas += f"{lectura.fecha_ini.strftime('%d/%m/%Y')} - {lectura.fecha_fin.strftime('%d/%m/%Y')}"
        else:
            fechas += f"{lectura.fecha_ini.strftime('%d/%m/%Y')} - [sin especificar]"


        # IMMPRESION EN PANTALLA
        st.write(f"## {libro.titulo}")
        st.markdown(
            f"""
            <div style="line-height: 1.2;">
                <div style="font-size: 26px;">{estrellas}</div>
                <div>{fechas}</div>
            </div>
            """,
            unsafe_allow_html=True
        )