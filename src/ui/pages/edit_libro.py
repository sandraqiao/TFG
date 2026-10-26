import streamlit as st
from ui.ui_selections import select_saga, select_idioma, select_genero, add_texto, select_date, select_prioridad_wishlist, select_orden_saga, select_autor
from services import libro_service, saga_service, autor_libro_service, autor_service

@st.dialog("Seguro que quieres eliminar el libro?", dismissible=False, icon="⚠️")
def confirm_delete(id_libro: int) -> bool:
    st.write("Esta acción no se puede deshacer")
    st.caption("Toda la información relacionada con este libro se eliminará junto a él")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Si, bórralo"):
            libro_service.delete(id_libro)
            st.session_state["libro_eliminado"] = True
            st.switch_page("./pages/biblioteca.py")
    with col2:
        if st.button("No, me arrepiento"):
            st.rerun()

def add_saga_popover():
    nom_saga = st.text_input("Nombre de la saga")
    if st.button("Guardar", icon="💾"):
        saga_service.create(nom_saga)

# ==========================================================================================================

st.set_page_config(
    page_title="Editar libro"
)

st.write("# ✏️ Editar libro")

libro = libro_service.get_libro(st.session_state["info_libro_id"])
id_autores_originales = autor_libro_service.get_id_autores_by_libro(libro.id_libro)
if st.session_state.get("autores_libro_editando") != libro.id_libro:
    autores = autor_service.get_all_autores()
    st.session_state["autores"] = [autor for autor in autores if autor.id_autor in id_autores_originales]
    st.session_state["autores_libro_editando"] = libro.id_libro

if libro.url_portada:
    col01, col02 = st.columns([2.5, 7.5])
    with col01:
        st.image(libro.url_portada)
    with col02:
        titulo = st.text_input("Título", libro.titulo)
        id_autores = select_autor(autor_libro_service.get_id_autores_by_libro(libro.id_libro))

        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            id_saga = select_saga(libro.id_saga)
        with col2:
            orden_saga = select_orden_saga(id_saga, libro.orden_saga)
else: 
    titulo = st.text_input("Título", libro.titulo)
    id_autores = select_autor(autor_libro_service.get_id_autores_by_libro(libro.id_libro))
    id_saga = select_saga(libro.id_saga)

isbn = st.text_input("ISBN", libro.isbn)

col1, col2, col3, col4, col5 = st.columns([0.15, 0.15, 0.4, 0.15, 0.15])
with col1:
    num_pag = st.text_input("Nº páginas", libro.num_pag if libro.num_pag else None)
with col2:
    idioma = select_idioma(libro.idioma)
with col3:
    editorial = st.text_input("Editorial", libro.editorial)
with col4:
    st.write("Wishlistear")
    with st.container(horizontal=True, horizontal_alignment="center"):
        en_wishlist = st.toggle("", value=libro.en_wishlist)
with col5:
    prioridad_wishlist = select_prioridad_wishlist(en_wishlist=en_wishlist, edit_prioridad=libro.prioridad_wishlist)

url_portada = st.text_input("Portada", libro.url_portada)

fecha_public = select_date("Fecha de publicación", libro.fecha_public)

generos = ",".join(select_genero(libro.genero))

sinopsis = add_texto("Sinopsis", libro.sinopsis)


with st.container(horizontal=True, horizontal_alignment="right"):
    if st.button("Guardar", icon="💾"):
        libro_service.update(
            id_libro=libro.id_libro,
            id_saga=id_saga,
            titulo=titulo,
            isbn=isbn,
            orden_saga=orden_saga,
            num_pag=int(num_pag) if num_pag else None,
            genero=generos,
            idioma=idioma,
            sinopsis=sinopsis,
            fecha_public=fecha_public,
            url_portada=url_portada,
            editorial=editorial,
            en_wishlist=en_wishlist,
            prioridad_wishlist=prioridad_wishlist
        )

        for id in (set(id_autores_originales)-set(id_autores)): 
            autor_libro_service.delete(libro.id_libro, id)
        for id in (set(id_autores)-set(id_autores_originales)):
            autor_libro_service.create(libro.id_libro, id)

        st.session_state["editando_libro"] = False
        st.session_state["libro_editado"] = True
        st.switch_page("./pages/biblioteca.py")

    if st.button("Eliminar", icon=":material/delete:"):
        confirm_delete(libro.id_libro)