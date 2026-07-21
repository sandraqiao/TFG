# Diseño físico

### Libro
Tabla que almacena la información bibliográfica de cada obra registrada por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_libro | INTEGER | PK, AUTOINCREMENT | Identificador único para un libro |
| id_saga | INTEGER | FK, NULL | Identificador único para una saga |
| titulo | VARCHAR(255) | NOT NULL | Nombre de la obra |
| isbn | VARCHAR(20) | UNIQUE, NULL | ISBN de una edición de referencia de la obra, cuando esté disponible |
| num_pag | INTEGER | NULL | Cantidad de páginas que tiene la obra |
| genero | TEXT | NOT NULL | Listado de géneros literarios asociados a la obra |
| idioma | VARCHAR(50) | NOT NULL | Idioma correspondiente a la edición de referencia (ISBN) |
| sinopsis | TEXT | NULL | Sinopsis de la obra |
| fecha_public | DATE | NULL | Fecha de publicación de la edición de referencia (ISBN) |
| url_portada | TEXT | NULL | URL de la imagen de la portada |
| editorial | VARCHAR(255) | NULL | Nombre de la editorial coincidente con el ISBN |
| en_wishlist | BOOLEAN | NOT NULL, DEFAULT FALSE | Booleano que indica si está el libro o no dentro de la lista de deseos |
| prioridad_wishlist | SMALLINT | NULL, CHECK (1-5) | Prioridad asignada al libro dentro de la lista de deseos |
**Restricciones adicionales**
- prioridad_wishlist solo se aplica si en_wishlist = true

### Saga
Tabla que almacena la información de las sagas de los libros registrados por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_saga | INTEGER | PK, AUTOINCREMENT | Identificador único para una saga |
| nom_saga | VARCHAR(255) | NOT NULL | Nombre de la saga |

### Autor
Tabla que almacena la información de los autores de los libros registrados por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_autor | INTEGER | PK, AUTOINCREMENT | Identificador único para un autor |
| nom_autor | VARCHAR(255) | NOT NULL | Nombre del autor |

### AutorLibro
Tabla intermedia que representa la relación N:M entre autores y libros.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_libro | INTEGER | PK, FK, NOT NULL | Identificador único para un libro |
| id_autor | INTEGER | PK, FK, NOT NULL | Identificador único para un autor |

### Lectura
Tabla que almacena la información personal de cada lectura realizada por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_lectura | INTEGER | PK, AUTOINCREMENT | Identificador único para una lectura |
| id_libro | INTEGER | FK, NOT NULL | Identificador único para un libro |
| estado | VARCHAR(255) | NOT NULL, CHECK (IN ('Leyendo', 'Leído', 'Abandonado')) | Estado de una lectura |
| valoracion | INTEGER | NULL, CHECK (0-10) | Valoración personal de una lectura |
| comentario | TEXT | NULL | Comentarios sobre la lectura |
| fecha_ini | DATE | NOT NULL | Fecha de inicio de lectura |
| fecha_fin | DATE | NULL | Fecha de finalización de la lectura |
| formato | VARCHAR(255) | NOT NULL, CHECK (IN ('Físico', 'eReader')) | Formato en el que se ha realizado la lectura |
**Restricciones adicionales**
- fecha_fin >= fecha_ini

### Tienda
Tabla que almacena la información objetiva de las tiendas sobre las que se hará scraping.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_tienda | INTEGER | PK, AUTOINCREMENT | Identificador único para una tienda |
| nom_tienda | VARCHAR(255) | NOT NULL | Nombre de la tienda |
| url_tienda | TEXT | NOT NULL | URL de la tienda |

### HistoricoPrecio
Tabla que almacena la información con los precios de los libros sobre los que se hacen scraping.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_precio | INTEGER | PK, AUTOINCREMENT | Identificador único para un precio |
| id_libro | INTEGER | FK, NOT NULL | Identificador único para un libro |
| id_tienda | INTEGER | FK, NOT NULL | Identificador único para una tienda |
| precio | NUMERIC(10,2) | NOT NULL | Precio en el momento que se ha hecho la consulta |
| pct_descuento | NUMERIC(3,2) | NULL, CHECK (0-100) | Descuentos aplicables en el momento en el que se ha hecho la consulta |
| fecha_consulta | DATE | NOT NULL | Fecha de la consulta |
| disponible | BOOLEAN | NOT NULL | Disponibilidad en el momento de la consulta |
| url_libro | TEXT | NOT NULL | URL correspondiente con la tienda y libro para poder realizar la compra |
**Restricciones adicionales**
- precio > 0
