# Descripcion del proyecto
El proyecto consiste en el desarrollo de una aplicación web para la gestión de una biblioteca personal. La aplicación permite almacenar y organizar información bibliográfica, gestionar autores y sagas, registrar el seguimiento de las lecturas, administrar una lista de deseos y consultar estadísticas personales.

Además, incorpora un sistema de consulta de precios mediante técnicas de web scraping sobre Casa del Libro, orientado a registrar la evolución de los precios y la disponibilidad de los libros incluidos en la lista de deseos. También permite obtener automáticamente parte de la información bibliográfica de un libro a partir de su ISBN.

# Objetivos
Desarrollar una aplicación web que permita gestionar una biblioteca personal, realizar un seguimiento de las lecturas y consultar estadísticas relacionadas con los libros registrados, incorporando funcionalidades de extracción automática de información bibliográfica y seguimiento de precios mediante web scraping.

# Alcance
La aplicación contempla las siguientes funcionalidades principales:
- Gestión del catálogo personal de libros, incluyendo su información bibliográfica, autores, sagas, géneros, idioma y editorial.
- Registro y seguimiento de las lecturas, con información sobre su estado, fechas, formato, valoración y comentarios personales.
- Gestión de una lista de deseos de libros, con posibilidad de establecer prioridades.
- Consulta de estadísticas relacionadas con la biblioteca y las lecturas, incluyendo el número de libros y lecturas, los estados de lectura, los formatos, las valoraciones, la evolución anual de las lecturas y los géneros registrados.
- Registro y consulta del historial de precios y disponibilidad de los libros incluidos en la lista de deseos mediante web scraping de Casa del Libro.
- Autorrellenado de parte de la información bibliográfica mediante la búsqueda de un libro por ISBN.
- Gestión de autores y sagas, permitiendo consultar los libros relacionados con cada uno.

# Tecnologías

# Planificación

# Lluvia de ideas

**Biblioteca**
    Se planteó mostrar en primera plana el libro que se está leyendo actualmente, seguido de los libros leídos y del resto del catálogo. En la versión implementada, la biblioteca muestra los libros registrados y permite ordenarlos por título o saga, así como filtrarlos por género, idioma, editorial y pertenencia a la lista de deseos. El seguimiento del estado de lectura se realiza desde el apartado de lecturas.

**Detalle del libro**
    Se planteó una pantalla independiente para consultar todos los detalles de un libro, incluyendo sus atributos, valoración, notas e historial de precios. En la versión implementada, la información bibliográfica se gestiona mediante los formularios de alta y edición del libro, mientras que las valoraciones, comentarios y fechas se registran en el apartado de lecturas. El historial de precios se consulta desde el apartado correspondiente.

**Análisis**
    Se planteó incorporar estadísticas personales, como la cantidad de libros leídos, las páginas leídas, el tiempo medio por libro, las categorías y un posible reto de lectura. En la versión implementada, se muestran estadísticas sobre el catálogo, la lista de deseos, las sagas, los estados de lectura, los formatos, las valoraciones, la evolución anual de las lecturas y los géneros. No se han implementado el cálculo del tiempo medio por libro ni el reto de lectura.

**Wishlist**
    Se planteó disponer de un listado de libros deseados con la posibilidad de añadir nuevos títulos y establecer prioridades, siguiendo una idea similar a la lista de deseos de Steam. En la versión implementada, los libros pueden incluirse en la lista de deseos y asignárseles una prioridad del 1 al 5.

**Precios**
    Se planteó registrar el historial de precios de los libros de la lista de deseos, ordenarlos por precio y disponer de una sección de ofertas o bajadas de precio destacadas. En la versión implementada, se pueden consultar los históricos de precios y la disponibilidad de los libros de la lista de deseos obtenidos mediante web scraping de Casa del Libro. La consulta se inicia manualmente y no se han implementado la ordenación automática por precio ni una sección específica de ofertas.