# Diseño físico

## Libro

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