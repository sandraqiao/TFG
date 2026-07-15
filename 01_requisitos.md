# Requisitos funcionales

### Gestión de la biblioteca
**RF-01**: El sistema permitirá registrar nuevos libros.
**RF-02**: El sistema permitirá editar la información de un libro.
**RF-03**: El sistema permitirá eliminar libros.
**RF-04**: El sistema permitirá consultarla información de un libro.

### Organización
**RF-05**: El sistema permitirá clasificar los libros según su estado de lectura (pendiente, leyendo, leído).
**RF-06**: El sistema permitirá indicar el formato en el que el usuario posee un libro (físico, ebook, ambos).
**RF-07**: El sistema permitirá añadir notas y una valoración personal a un libro.

### Búsqueda
**RF-08**: El sistema permitirá buscar libros por isbn, saga, título o autor.
**RF-09**: El sistema permitirá filtrar los libros según distintos criterios (estado de lectura, género, saga, formato, etc.).

### Wishlist
**RF-10**: El sistema permitirá añadir y eliminar libros de la lista de deseos.
**RF-11**: El sistema permitirá establecer un orden de prioridad a los libros dentro de la lista de deseos.

### Precios
**RF-12**: El sistema permitirá obtener automáticamente el precio de un libro de distintas tiendas mediante web scraping.
**RF-13**: El sistema almacenará un histórico de los precios obtenidos de los libros con sus fechas.
**RF-14**: El sistema permitirá consultar la evolución del precio de un libro.

### Estadísticas
**RF-15**: El sistema mostrará estadísticas sobre la biblioteca del usuario (libros leídos, páginas leídas, géneros, reto de lectura, media de días de lectura por libro, etc.).

# Requisitos no funcionales

**RNF-01**: La aplicación deberá disponer de una interfaz intuitiva y fácil de usar.
**RNF-02**: La información almacenada deberá persistir entre sesiones.
**RNF-03**: La aplicación deberá acceder a una base de datos relacional.
**RNF-04**: Las consultas habituales deberán responder en un tiempo razonable (menos de 2s con una biblioteca de tamaño normal).
**RNF-05**: La aplicación deberá registrar correctamente los errores producidos durante el scraping.
**RNF-06**: La aplicación deberá permitir añadir nuevas tiendas para el scraping sin modificar el resto de la aplicación (escalabilidad).