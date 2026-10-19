# Diseño físico

### Libro
Tabla que almacena la información bibliográfica de cada obra registrada por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_libro | INTEGER | PK | Identificador único para un libro |
| id_saga | INTEGER | FK, NULL | Identificador de la saga a la que pertenece el libro, cuando corresponda |
| titulo | VARCHAR(255) | NOT NULL | Nombre de la obra |
| isbn | VARCHAR(20) | UNIQUE, NULL | ISBN de la edición de referencia de la obra, cuando esté disponible |
| num_pag | INTEGER | NULL, CHECK (> 0) | Cantidad de páginas de la obra |
| genero | TEXT | NOT NULL | Géneros literarios asociados a la obra |
| idioma | VARCHAR(50) | NOT NULL | Idioma de la edición de referencia |
| sinopsis | TEXT | NULL | Sinopsis de la obra |
| fecha_public | DATE | NULL | Fecha de publicación de la edición de referencia |
| url_portada | TEXT | NULL | URL de la imagen de la portada |
| editorial | VARCHAR(255) | NULL | Nombre de la editorial de la edición de referencia |
| en_wishlist | BOOLEAN | NOT NULL, DEFAULT FALSE | Indica si el libro está incluido en la lista de deseos |
| prioridad_wishlist | SMALLINT | NULL, CHECK (1-5) | Prioridad asignada al libro dentro de la lista de deseos |

**Restricciones adicionales**
- num_pag debe ser mayor que 0 cuando se indique.
- Si en_wishlist es false, prioridad_wishlist debe ser NULL.
- Si en_wishlist es true, prioridad_wishlist puede ser NULL o un valor entre 1 y 5.

### Saga
Tabla que almacena la información de las sagas de los libros registrados por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_saga | INTEGER | PK | Identificador único para una saga |
| nom_saga | VARCHAR(255) | NOT NULL | Nombre de la saga |

### Autor
Tabla que almacena la información de los autores de los libros registrados por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_autor | INTEGER | PK | Identificador único para un autor |
| nom_autor | VARCHAR(255) | NOT NULL | Nombre del autor |

### AutorLibro
Tabla intermedia que representa la relación N:M entre autores y libros.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_libro | INTEGER | PK, FK, NOT NULL | Identificador del libro |
| id_autor | INTEGER | PK, FK, NOT NULL | Identificador del autor |

### Lectura
Tabla que almacena la información personal de cada lectura registrada por el usuario.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_lectura | INTEGER | PK | Identificador único para una lectura |
| id_libro | INTEGER | FK, NOT NULL | Identificador del libro asociado a la lectura |
| estado | VARCHAR(255) | NOT NULL, CHECK (IN ('Leyendo', 'Leído', 'Abandonado')) | Estado de la lectura |
| valoracion | INTEGER | NULL, CHECK (1-5) | Valoración personal de la lectura |
| comentario | TEXT | NULL | Comentarios personales sobre la lectura |
| fecha_ini | DATE | NOT NULL | Fecha de inicio de la lectura |
| fecha_fin | DATE | NULL | Fecha de finalización de la lectura |
| formato | VARCHAR(255) | NOT NULL, CHECK (IN ('Físico', 'Ebook', 'AudioLibro')) | Formato en el que se realiza la lectura |

**Restricciones adicionales**
- fecha_fin debe ser mayor o igual que fecha_ini cuando se indique.
- La valoración puede ser NULL o un valor entre 1 y 5.
- Si se indica una valoración, el estado debe ser 'Leído' o 'Abandonado'.

### Tienda
Tabla que almacena la información de las tiendas sobre las que se registran históricos de precios.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_tienda | INTEGER | PK | Identificador único para una tienda |
| nom_tienda | VARCHAR(255) | NOT NULL | Nombre de la tienda |
| url_tienda | TEXT | NOT NULL | URL de la tienda |

### HistoricoPrecio
Tabla que almacena los precios y la disponibilidad de los libros consultados mediante web scraping.

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_precio | INTEGER | PK | Identificador único para un registro de precio |
| id_libro | INTEGER | FK, NOT NULL | Identificador del libro |
| id_tienda | INTEGER | FK, NOT NULL | Identificador de la tienda |
| precio | NUMERIC(10,2) | NOT NULL, CHECK (> 0) | Precio en el momento de la consulta |
| pct_descuento | NUMERIC(5,2) | NULL, CHECK (0-100) | Porcentaje de descuento en el momento de la consulta |
| fecha_consulta | DATE | NOT NULL | Fecha de la consulta |
| disponible | BOOLEAN | NOT NULL | Indica si el libro estaba disponible en el momento de la consulta |
| url_libro | TEXT | NOT NULL | URL del libro en la tienda |

**Restricciones adicionales**
- precio debe ser mayor que 0.
- pct_descuento puede ser NULL o un valor entre 0 y 100.

## Efecto de delete en relaciones
Tabla que resume el comportamiento de borrado en las relaciones.

| Relación | Acción |
|----------|--------|
| Saga -> Libro | SET NULL |
| Libro -> Lectura | CASCADE |
| Libro -> HistoricoPrecio | CASCADE |
| Tienda -> HistoricoPrecio | CASCADE |
| Autor -> AutorLibro | CASCADE |
| Libro -> AutorLibro | CASCADE |