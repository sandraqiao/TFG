import streamlit as st
from services import lectura_service, libro_service, autor_service, autor_libro_service

st.set_page_config(
    page_title="Lecturas"
)

st.write("# Lecturas")

# ==========================================================================================================

lecturas = lectura_service.get_all_lecturas()

if lecturas is None:
    st.write("## 🕸️ No hay lecturas registradas 🕸️")

else:

    for lectura in lecturas:

        libro = libro_service.get_libro(lectura.id_libro)
        autoreslibro = autor_libro_service.search_by_libro(libro.id_libro)

        # TÍTULO Y AUTOR
        titulo = libro.titulo 
        if autoreslibro is None:
            titulo =+ "[Sin datos]"
        for autorlibro in autoreslibro:
            titulo += " - "
            titulo += autor_service.get_by_id(autorlibro.id_autor).nom_autor

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

        # IMPRESION
        with st.expander(f"{titulo}"):
            st.write(f"Valoración: {estrellas} ({lectura.valoracion}/10)")
            st.write(f"Fechas: {fechas}")

    # for lectura in lecturas:
    #     libro = libro_service.get_libro(lectura.id_libro)


    #     # VALORACIÓN DE LECTURA
    #     estrellas = ""
    #     if lectura.valoracion:
    #         for i in range(10):
    #             if i < lectura.valoracion:
    #                 estrellas += "★"
    #             else:
    #                 estrellas += "☆"
    #             estrellas += " "
    #     else:
    #         estrellas = "☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆"


    #     # FECHAS DE LECTURA
    #     fechas = ""
    #     if lectura.fecha_fin:
    #         fechas += f"{lectura.fecha_ini.strftime('%d/%m/%Y')} - {lectura.fecha_fin.strftime('%d/%m/%Y')}"
    #     else:
    #         fechas += f"{lectura.fecha_ini.strftime('%d/%m/%Y')} - [sin especificar]"


    #     # IMMPRESION EN PANTALLA
    #     st.write(f"## {libro.titulo}")
    #     st.markdown(
    #         f"""
    #         <div style="line-height: 1.2;">
    #             <div style="font-size: 26px;">{estrellas}</div>
    #             <div>{fechas}</div>
    #         </div>
    #         """,
    #         unsafe_allow_html=True
    #     )