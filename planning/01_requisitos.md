# Requisitos funcionales

### Gestión de la biblioteca
- **RF-01**: El sistema permitirá registrar nuevos libros.
- **RF-02**: El sistema permitirá editar la información de un libro.
- **RF-03**: El sistema permitirá eliminar libros.
- **RF-04**: El sistema permitirá consultar la información bibliográfica de los libros registrados.

### Organización
- **RF-05**: El sistema permitirá registrar y consultar lecturas asociadas a los libros, indicando su estado (Leyendo, Leído o Abandonado).
- **RF-06**: El sistema permitirá indicar el formato de una lectura (Físico, Ebook o AudioLibro).
- **RF-07**: El sistema permitirá registrar y consultar las fechas de inicio y finalización, la valoración personal y los comentarios de cada lectura.
- **RF-08**: El sistema permitirá gestionar autores y sagas, así como consultar los libros relacionados con ellos.

### Búsqueda y filtrado
- **RF-09**: El sistema permitirá ordenar los libros de la biblioteca por título o saga.
- **RF-10**: El sistema permitirá filtrar los libros por género, idioma, editorial y pertenencia a la lista de deseos.
- **RF-11**: El sistema permitirá filtrar las lecturas por estado, valoración y formato.

### Wishlist
- **RF-12**: El sistema permitirá incluir y excluir libros de la lista de deseos.
- **RF-13**: El sistema permitirá establecer una prioridad del 1 al 5 para los libros incluidos en la lista de deseos.

### Información bibliográfica
- **RF-14**: El sistema permitirá obtener automáticamente parte de la información bibliográfica de un libro a partir de su ISBN mediante web scraping de Casa del Libro.

### Precios
- **RF-15**: El sistema permitirá iniciar manualmente la consulta del precio y la disponibilidad de los libros de la lista de deseos mediante web scraping de Casa del Libro.
- **RF-16**: El sistema almacenará un histórico de los precios y la disponibilidad obtenidos, junto con la fecha de consulta y la URL del libro.
- **RF-17**: El sistema permitirá consultar el histórico de precios de los libros incluidos en la lista de deseos.

### Estadísticas
- **RF-18**: El sistema mostrará estadísticas sobre la biblioteca y las lecturas, incluyendo el número de libros, lecturas, libros en la lista de deseos, sagas, estados de lectura, formatos, valoraciones, valoración media, evolución anual de las lecturas y géneros registrados.

# Requisitos no funcionales

- **RNF-01**: La aplicación deberá disponer de una interfaz intuitiva y fácil de usar.
- **RNF-02**: La información almacenada deberá persistir entre sesiones.
- **RNF-03**: La aplicación deberá acceder a una base de datos relacional para almacenar la información.
- **RNF-04**: La aplicación deberá separar la interfaz de usuario, la lógica de negocio y el acceso a datos para facilitar el mantenimiento y la reutilización del código.
- **RNF-05**: La aplicación deberá validar los datos introducidos y mantener la integridad de la información almacenada.
- **RNF-06**: El sistema de web scraping deberá contemplar la posibilidad de que la tienda no proporcione los datos esperados o deniegue el acceso.