# Diseño físico

### Libro

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_libro | INTEGER | PK, AUTOINCREMENT | Identificador único para un libro |
| id_saga | INTEGER | FK, NULL | Identificador único para una saga |
| titulo | VARCHAR(255) | NOT NULL | Nombre de la obra |
| isbn | VARCHAR(20) | UNIQUE, NULL | Código único de la obra, este será solo de un valor y se usará una edición en concreto como ejemplo si procede |
| num_pag | INTEGER | NULL | Cantidad de páginas que tiene la obra |
| genero | TEXT | NOT NULL | Géneros literarios de la obra |
| idioma | VARCHAR(50) | NOT NULL | Idioma de la obra coincidente con el isbn |
| sinopsis | TEXT | NULL | Sinopsis de la obra |
| fecha_public | DATE | NULL | Primera fecha de publicación de la obra, la versión del isbn |
| url_portada | TEXT | NULL | URL de la imágen de la portada |
| editorial | VARCHAR(255) | NULL | Nombre de la editorial coincidente con el isbn |
| en_wishlist | BOOLEAN | NOT NULL, DEFAULT FALSE | Booleano que indica si está el libro o no dentro de la lista de deseos |
| prioridad_wishlist | SMALLINT | NULL, CHECK (1-5) | Prioridad asignada al libro dentro de la lista de deseos |

### Saga

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_saga | INTEGER | PK, AUTOINCREMENT | Identificador único para una saga |
| nom_saga | VARCHAR(255) | NOT NULL | Nombre de la saga |

### Autor

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

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_lectura | INTEGER | PK, AUTOINCREMENT | Identificador único para una lectura |
| id_libro | INTEGER | FK, NOT NULL | Identificador único para un libro |
| estado | VARCHAR(255) | NOT NULL, CHECK (leyendo, leído, abandonado) | Estado de una lectura |
| valoracion | INTEGER | NULL, CHECK (1-10) | Valoración personal de una lectura |
| notas | VARCHAR(255) | NULL | Comentarios sobre la lectura |
| fecha_ini | DATE | NOT NULL | Fecha de inicio de lectura |
| fecha_fin | DATE | NULL | Fecha final de lectura, solo si esta se ha llegado a completar (estado leído) |
| formato | VARCHAR(255) | NOT NULL, CHECK (físico, ereader) | Formato en el que se ha realizado la lectura |

### Tienda

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_tienda | INTEGER | PK, AUTOINCREMENT | Identificador único para una tienda |
| nom_tienda | VARCHAR(255) | NOT NULL | Nombre de la tienda |
| url_tienda | VARCHAR(255) | NOT NULL | URL de la tienda |

### HistoricoPrecio

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_precio | INTEGER | PK, AUTOINCREMENT | Identificador único para un precio |
| id_libro | INTEGER | FK, NOT NULL | Identificador único para un libro |
| id_tienda | INTEGER | FK, NOT NULL | Identificador único para una tienda |
| precio | DOUBLE | NOT NULL | Precio en el momento que se ha hecho la consulta |
| pct_descuento | INTEGER | NULL | Descuentos aplicables en el momento en el que se ha hecho la consulta |
| fecha_consulta | DATE | NOT NULL | Fecha de la consulta |
| disponible | BOOLEAN | NOT NULL | Disponibilidad de la consulta: 0 - no disponible, 1 - disponible |
| url_libro | VARCHAR(255) | NOT NULL | URL correspondiente con la tienda y libro para poder realizar la compra |