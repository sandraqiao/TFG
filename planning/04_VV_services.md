# Verificación y validación de services

## Pruebas sobre las funcionalidades generales de services
| Orden | Acción | Datos | Resultado esperado |
| ----- | ------ | ----- | ------------------ |
| 1 | Create saga | Nombre: Crónicas de Narnia | Se crea correctamente |
| 2 | Create saga | Nombre: Crónicas de Narnia | ValueError por nombre repetido |
| 3 | Create saga | Nombre: Saga de prueba | Se crea correctamente |
| 4 | Update saga | ID de Saga de prueba. Nuevo nombre: El Archivo de las Tormentas | Se modifica correctamente |
| 5 | Update saga | ID de El Archivo de las Tormentas. Nuevo nombre: Crónicas de Narnia | ValueError por nombre repetido |
| 6 | Update saga | ID inexistente. Nuevo nombre: Saga inexistente | ValueError por saga inexistente |
| 7 | Delete saga | ID de El Archivo de las Tormentas | Se elimina correctamente |
| 8 | Delete saga | ID inexistente | ValueError por saga inexistente |
| 9 | Create autor | Nombre: J.R.R. Tolkien | Se crea correctamente |
| 10 | Create autor | Nombre: J.R.R. Tolkien | ValueError por nombre repetido |
| 11 | Create autor | Nombre: J.K. Rowling | Se crea correctamente |
| 12 | Update autor | ID de J.K. Rowling. Nuevo nombre: George R.R. Martin | Se modifica correctamente |
| 13 | Update autor | ID de George R.R. Martin. Nuevo nombre: J.R.R. Tolkien | ValueError por nombre repetido |
| 14 | Update autor | ID inexistente. Nuevo nombre: Autor inexistente | ValueError por autor inexistente |
| 15 | Delete autor | ID de George R.R. Martin | Se elimina correctamente |
| 16 | Delete autor | ID inexistente | ValueError por autor inexistente |
| 17 | Create libro | Título: El Hobbit. ISBN: 9780261102217. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: None | Se crea correctamente |
| 18 | Create libro | Título: El Hobbit 2. ISBN: 9780261102217. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 1938-01-01. URL portada: https://ejemplo.com/hobbit2.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: None | ValueError por ISBN repetido |
| 19 | Create libro | Título: Libro de prueba. ISBN: 9780000000001. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: inexistente. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: false. Prioridad: None | ValueError por saga inexistente |
| 20 | Create libro | Título: Libro de prueba. ISBN: 9780000000002. Páginas: 0. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: false. Prioridad: None | ValueError por número de páginas inválido |
| 21 | Create libro | Título: Libro de prueba. ISBN: 9780000000003. Páginas: -10. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: false. Prioridad: None | ValueError por número de páginas inválido |
| 22 | Create libro | Título: Libro de prueba. ISBN: 9780000000004. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: false. Prioridad: 3 | ValueError por prioridad sin Wishlist |
| 23 | Create libro | Título: Libro de Wishlist. ISBN: 9780000000005. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: true. Prioridad: None | Se crea correctamente sin prioridad |
| 24 | Create libro | Título: Libro prioritario. ISBN: 9780000000006. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: true. Prioridad: 5 | Se crea correctamente |
| 25 | Create libro | Título: Libro de prueba. ISBN: 9780000000007. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: true. Prioridad: 0 | ValueError por prioridad fuera de rango |
| 26 | Create libro | Título: Libro de prueba. ISBN: 9780000000008. Páginas: 300. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: true. Prioridad: 6 | ValueError por prioridad fuera de rango |
| 27 | Update libro | ID de El Hobbit. Nuevo título: El Hobbit - Edición especial. ISBN: 9780261102217. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: None | Se modifica correctamente |
| 28 | Update libro | ID de El Hobbit. Nuevo título: El Hobbit - Edición especial. ISBN: 9780000000006. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: None | ValueError por ISBN repetido |
| 29 | Update libro | ID inexistente. Título: Libro actualizado. ISBN: 9780000000010. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Sinopsis de prueba. Fecha publicación: 2020-01-01. URL portada: https://ejemplo.com/libro.jpg. Editorial: Editorial de prueba. Wishlist: false. Prioridad: None | ValueError por libro inexistente |
| 30 | Update libro | ID de El Hobbit. Título: El Hobbit. ISBN: 9780261102217. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: inexistente. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: None | ValueError por saga inexistente |
| 31 | Update libro | ID de El Hobbit. Título: El Hobbit. ISBN: 9780261102217. Páginas: 0. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: None | ValueError por número de páginas inválido |
| 32 | Update libro | ID de El Hobbit. Título: El Hobbit. ISBN: 9780261102217. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: false. Prioridad: 3 | ValueError por prioridad sin Wishlist |
| 33 | Update libro | ID de El Hobbit. Título: El Hobbit. ISBN: 9780261102217. Páginas: 310. Género: Fantasía. Idioma: Español. Saga: Crónicas de Narnia. Sinopsis: Un hobbit emprende una aventura. Fecha publicación: 1937-09-21. URL portada: https://ejemplo.com/hobbit.jpg. Editorial: Minotauro. Wishlist: true. Prioridad: None | Se modifica correctamente sin prioridad |
| 34 | Delete libro | ID de un libro existente: El Hobbit | Se elimina correctamente |
| 35 | Delete libro | ID inexistente | ValueError por libro inexistente |
| 36 | Create tienda | Nombre: Amazon. URL: https://www.amazon.es | Se crea correctamente |
| 37 | Create tienda | Nombre: Amazon. URL: https://www.amazon.com | ValueError por nombre repetido |
| 38 | Create tienda | Nombre: Fnac. URL: https://www.fnac.es | Se crea correctamente |
| 39 | Update tienda | ID de Fnac. Nuevo nombre: Casa del Libro. URL: https://www.fnac.es | Se modifica correctamente |
| 40 | Update tienda | ID de Casa del Libro. Nuevo nombre: Amazon. URL: https://www.fnac.es | ValueError por nombre repetido |
| 41 | Update tienda | ID inexistente. Nombre: Tienda inexistente. URL: https://ejemplo.com/tienda | ValueError por tienda inexistente |
| 42 | Delete tienda | ID de Casa del Libro | Se elimina correctamente |
| 43 | Delete tienda | ID inexistente | ValueError por tienda inexistente |
| 44 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leyendo. Valoración: None. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | Se crea correctamente |
| 45 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leyendo. Valoración: 8. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | ValueError por valoración en lectura no finalizada |
| 46 | Create lectura | Libro inexistente. Estado: Leyendo. Valoración: None. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | ValueError por libro inexistente |
| 47 | Create lectura | Libro existente: Libro de Wishlist. Estado: Inventado. Valoración: None. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | ValueError por estado inválido |
| 48 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leído. Valoración: -1. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: 2026-08-10. Formato: Físico | ValueError por valoración fuera de rango |
| 49 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leído. Valoración: 11. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: 2026-08-10. Formato: Físico | ValueError por valoración fuera de rango |
| 50 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leído. Valoración: 8. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: 2026-08-10. Formato: Físico | Se crea correctamente |
| 51 | Create lectura | Libro existente: Libro de Wishlist. Estado: Abandonado. Valoración: 5. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: 2026-08-05. Formato: Físico | Se crea correctamente |
| 52 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leyendo. Valoración: None. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Papel | ValueError por formato inválido |
| 53 | Create lectura | Libro existente: Libro de Wishlist. Estado: Leyendo. Valoración: None. Comentario: None. Fecha inicio: 2026-08-10. Fecha fin: 2026-08-01. Formato: Físico | ValueError por fechas inválidas |
| 54 | Update lectura | ID de lectura existente. Libro: Libro de Wishlist. Estado: Leído. Valoración: 8. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: 2026-08-10. Formato: Físico | Se modifica correctamente |
| 55 | Update lectura | ID de lectura existente. Libro: Libro de Wishlist. Estado: Leyendo. Valoración: 8. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | ValueError por valoración en lectura no finalizada |
| 56 | Update lectura | ID inexistente. Libro: Libro de Wishlist. Estado: Leyendo. Valoración: None. Comentario: None. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | ValueError por lectura inexistente |
| 57 | Delete lectura | ID de una lectura existente | Se elimina correctamente |
| 58 | Delete lectura | ID inexistente | ValueError por lectura inexistente |
| 59 | Create autor-libro | ID de libro existente: Libro de Wishlist. ID de autor existente: J.R.R. Tolkien | Se crea correctamente |
| 60 | Create autor-libro | ID de libro existente: Libro de Wishlist. ID de autor existente: J.R.R. Tolkien. Misma combinación que la prueba anterior | ValueError por relación existente |
| 61 | Create autor-libro | ID de libro inexistente. ID de autor existente: J.R.R. Tolkien | ValueError por libro inexistente |
| 62 | Create autor-libro | ID de libro existente: Libro de Wishlist. ID de autor inexistente | ValueError por autor inexistente |
| 63 | Delete autor-libro | ID de libro existente: Libro de Wishlist. ID de autor existente: J.R.R. Tolkien | Se elimina correctamente |
| 64 | Delete autor-libro | ID de libro existente: Libro de Wishlist. ID de autor existente: J.R.R. Tolkien. Relación inexistente | ValueError por relación inexistente |
| 65 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: 15.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | Se crea correctamente |
| 66 | Create histórico precio | ID de libro inexistente. ID de tienda existente: Amazon. Precio: 15.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por libro inexistente |
| 67 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda inexistente. Precio: 15.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por tienda inexistente |
| 68 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: -5. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por precio fuera de rango |
| 69 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: 0. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por precio fuera de rango |
| 70 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: 15.99. Descuento: -1. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por porcentaje de descuento fuera de rango |
| 71 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: 15.99. Descuento: 101. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por porcentaje de descuento fuera de rango |
| 72 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: 15.99. Descuento: 0. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | Se crea correctamente |
| 73 | Create histórico precio | ID de libro existente: Libro de Wishlist. ID de tienda existente: Amazon. Precio: 15.99. Descuento: None. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | Se crea correctamente |
| 74 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: 12.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | Se modifica correctamente |
| 75 | Update histórico precio | ID de histórico inexistente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: 12.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por histórico inexistente |
| 76 | Update histórico precio | ID de histórico existente. ID de libro inexistente. ID de tienda: Amazon. Precio: 12.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por libro inexistente |
| 77 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda inexistente. Precio: 12.99. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por tienda inexistente |
| 78 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: -1. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por precio fuera de rango |
| 79 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: 0. Descuento: 10. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por precio fuera de rango |
| 80 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: 12.99. Descuento: -1. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por porcentaje de descuento fuera de rango |
| 81 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: 12.99. Descuento: 101. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | ValueError por porcentaje de descuento fuera de rango |
| 82 | Update histórico precio | ID de histórico existente. ID de libro: Libro de Wishlist. ID de tienda: Amazon. Precio: 12.99. Descuento: 0. Fecha consulta: 2026-08-07. Disponible: true. URL libro: https://ejemplo.com/libro | Se modifica correctamente |
| 83 | Delete histórico precio | ID de un histórico existente | Se elimina correctamente |
| 84 | Delete histórico precio | ID de un histórico inexistente | ValueError por histórico inexistente |

## Pruebas de borrado en cascada

| Orden | Acción | Datos | Resultado esperado |
| ----- | ------ | ----- | ------------------ |
| 85 | Delete saga | Borrar una saga que tenga libros asociados | Los libros mantienen su id_saga con valor NULL | 
| 86 | Delete libro | Borrar un libro que tenga lecturas asociadas | Se eliminan sus lecturas | 
| 87 | Delete libro | Borrar un libro que tenga históricos de precio asociados | Se eliminan sus históricos de precio | 
| 88 | Delete libro | Borrar un libro que tenga relaciones autor-libro | Se eliminan sus relaciones autor-libro | 
| 89 | Delete tienda | Borrar una tienda con históricos de precio asociados | Se eliminan sus históricos de precio | 
| 90 | Delete autor | Borrar un autor con relaciones autor-libro | Se eliminan sus relaciones autor-libro |


## Pruebas sobre las funcionalidades get_all, search y filter de services

### Datos previos

### Sagas
| ID | Nombre |
| -- | ------ |
| 1 | El señor de los anillos |
| 2 | Harry Potter |
| 3 | Nacidos de la Bruma |

### Autores
| ID | Nombre |
| -- | ------ |
| 1 | J.R.R. Tolkien |
| 2 | J.K. Rowling |
| 3 | Brandon Sanderson |

### Libros
| ID | Título | ID Saga | ISBN | Género | Idioma | Editorial | Wishlist |
| -- | ------ | ------- | ---- | ------ | ------ | --------- | -------- |
| 1 | La comunidad del anillo | 1 | 111 | Fantasía | ESP | Minotauro | True |
| 2 | Las dos torres | 1 | 222 | Fantasía | ESP | Minotauro | False |
| 3 | La piedra filosofal | 2 | 333 | Fantasía | ESP | Salamandra | True |
| 4 | The way of the king | None | 444 | Fantasía | ENG | Tor | False |
| 5 | Libro de prueba | None | 555 | Misterio | ESP | Planeta | True |

### Lecturas
| ID | ID Libro | Estado | Valoración | Formato | Fecha inicio | Fecha fin |
| -- | -------- | ------ | ---------- | ------- | ------------ | --------- |
| 1 | 1 | Leído | 5 | Físico | 2019-12-04 | 2019-12-04 |
| 2 | 1 | Leyendo | None | Ebook | 2019-12-04 | None |
| 3 | 3 | Abandonado | 2 | Físico | 2019-12-04 | 2019-12-04 |
| 4 | 4 | Leído | 8 | Ebook | 2019-12-04 | 2019-12-04 |
| 5 | 5 | Leyendo | None | AudioLibro | 2019-12-04 | None |

### Tiendas
| ID | Nombre | URL |
| -- | ------ | --- |
| 1 | Amazon | amazon.com |
| 2 | Casa del libro | casadellibro.com |
| 3 | Fnac | fnac.com |

### Históricos de precio
 ID | ID Libro | ID Tienda | Fecha | Precio | Disponible |
| -- | -------- | --------- | ----- | ------ | ---------- |
| 1 | 1 | 1 | 2019-12-01 | 15.99 | True |
| 2 | 1 | 2 | 2019-12-04 | 18.59 | True |
| 3 | 3 | 1 | 2019-12-10 | 12.99 | True |
| 4 | 4 | 3 | 2019-12-15 | 25.00 | True |
| 5 | 5 | 1 | 2019-12-20 | 9.99 | True |

## Pruebas

| Orden | Acción | Datos | Esperado |
| ----- | ------ | ----- | -------- |
| 1 | Get all sagas | Sin filtros | Devuelve las 3 sagas: El señor de los anillos, Harry Potter y Nacidos de la Bruma |
| 2 | Search saga | Nombre: `Harry` | Devuelve la saga Harry Potter |
| 3 | Search saga | Nombre: `Nacidos` | Devuelve la saga Nacidos de la Bruma |
| 4 | Search saga | Nombre inexistente | Devuelve una lista vacía |
| 5 | Get all autores | Sin filtros | Devuelve los 3 autores: J.R.R. Tolkien, J.K. Rowling y Brandon Sanderson |
| 6 | Search by autor | Autor: J.R.R. Tolkien | Devuelve las relaciones autor-libro asociadas a Tolkien |
| 7 | Search by autor | Autor: J.K. Rowling | Devuelve las relaciones autor-libro asociadas a Rowling |
| 8 | Search by autor | ID de autor inexistente | ValueError por autor inexistente |
| 9 | Get all libros | Sin filtros | Devuelve los 5 libros |
| 10 | Search by saga | Saga: El señor de los anillos | Devuelve La comunidad del anillo y Las dos torres |
| 11 | Search by saga | Saga: Harry Potter | Devuelve La piedra filosofal |
| 12 | Search by título | Texto: `anillo` | Devuelve La comunidad del anillo |
| 13 | Search by título | Texto: `torres` | Devuelve Las dos torres |
| 14 | Search by ISBN | ISBN: `333` | Devuelve La piedra filosofal |
| 15 | Search by ISBN | ISBN inexistente | Devuelve una lista vacía o `None`, según la implementación del repository/service |
| 16 | Search by autor | Autor: J.R.R. Tolkien | Devuelve La comunidad del anillo y Las dos torres |
| 17 | Search by autor | Autor: Brandon Sanderson | Devuelve The way of the king |
| 18 | Filter libros | Géneros: Fantasía | Devuelve los libros 1, 2, 3 y 4 |
| 19 | Filter libros | Géneros: Misterio | Devuelve Libro de prueba |
| 20 | Filter libros | Idiomas: ESP | Devuelve los libros 1, 2, 3 y 5 |
| 21 | Filter libros | Idiomas: ENG | Devuelve The way of the king |
| 22 | Filter libros | Editoriales: Minotauro | Devuelve La comunidad del anillo y Las dos torres |
| 23 | Filter libros | Wishlist: True | Devuelve los libros 1, 3 y 5 |
| 24 | Filter libros | Wishlist: False | Devuelve los libros 2 y 4 |
| 25 | Filter libros | Género: Fantasía + Idioma: ESP | Devuelve los libros 1, 2 y 3 |
| 26 | Filter libros | Género: Fantasía + Wishlist: True | Devuelve los libros 1 y 3 |
| 27 | Filter libros | Género: Misterio + Idioma: ENG | Devuelve una lista vacía |
| 28 | Filter libros | Sin filtros | Devuelve los 5 libros |
| 29 | Get all lecturas | Sin filtros | Devuelve las 5 lecturas |
| 30 | Search by libro | Libro: La comunidad del anillo | Devuelve las lecturas 1 y 2 |
| 31 | Search by libro | Libro: The way of the king | Devuelve la lectura 4 |
| 32 | Search by libro | ID de libro inexistente | ValueError por libro inexistente |
| 33 | Filter lecturas | Estados: Leído | Devuelve las lecturas 1 y 4 |
| 34 | Filter lecturas | Estados: Leyendo | Devuelve las lecturas 2 y 5 |
| 35 | Filter lecturas | Estados: Abandonado | Devuelve la lectura 3 |
| 36 | Filter lecturas | Valoraciones: 5 | Devuelve la lectura 1 |
| 37 | Filter lecturas | Valoraciones: 5 y 8 | Devuelve las lecturas 1 y 4 |
| 38 | Filter lecturas | Formatos: Físico | Devuelve las lecturas 1 y 3 |
| 39 | Filter lecturas | Formatos: Ebook | Devuelve las lecturas 2 y 4 |
| 40 | Filter lecturas | Estado: Leído + Formato: Ebook | Devuelve la lectura 4 |
| 41 | Filter lecturas | Estado: Abandonado + Formato: Ebook | Devuelve una lista vacía |
| 42 | Filter lecturas | Sin filtros | Devuelve las 5 lecturas |
| 43 | Get all históricos | Sin filtros | Devuelve los 5 históricos |
| 44 | Filter históricos | Libros: ID 1 | Devuelve los históricos 1 y 2 |
| 45 | Filter históricos | Libros: ID 3 | Devuelve el histórico 3 |
| 46 | Filter históricos | Tiendas: ID 1 | Devuelve los históricos 1, 3 y 5 |
| 47 | Filter históricos | Tiendas: ID 3 | Devuelve el histórico 4 |
| 48 | Filter históricos | Fecha inicio: 2019-12-01. Fecha fin: 2019-12-04 | Devuelve los históricos 1 y 2 |
| 49 | Filter históricos | Fecha inicio: 2019-12-05. Fecha fin: 2019-12-14 | Devuelve el histórico 3 |
| 50 | Filter históricos | Fecha inicio: 2019-12-04. Fecha fin: 2019-12-15 | Devuelve los históricos 2, 3 y 4 |
| 51 | Filter históricos | Fecha inicio: 2019-12-21. Fecha fin: 2019-12-31 | Devuelve una lista vacía |
| 52 | Filter históricos | Precio mínimo: 10.00. Precio máximo: 20.00 | Devuelve los históricos 1, 2 y 3 |
| 53 | Filter históricos | Precio mínimo: 9.00. Precio máximo: 10.00 | Devuelve el histórico 5 |
| 54 | Filter históricos | Precio mínimo: 30.00. Precio máximo: 40.00 | Devuelve una lista vacía |
| 55 | Filter históricos | Libro: ID 1 + Tienda: ID 1 | Devuelve el histórico 1 |
| 56 | Filter históricos | Libro: ID 1 + Precio mínimo: 10.00 + Precio máximo: 17.00 | Devuelve el histórico 1 |
| 57 | Filter históricos | Tienda: ID 1 + Precio mínimo: 10.00 + Precio máximo: 16.00 | Devuelve los históricos 1 y 3 |
| 58 | Filter históricos | Libro: ID 1 + Fecha inicio: 2019-12-01 + Fecha fin: 2019-12-03 | Devuelve el histórico 1 |
| 59 | Filter históricos | Tienda: ID 1 + Fecha inicio: 2019-12-05 + Fecha fin: 2019-12-15 | Devuelve el histórico 3 |
| 60 | Filter históricos | Libro: ID 1 + Tienda: ID 1 + Fecha inicio: 2019-12-01 + Fecha fin: 2019-12-10 + Precio mínimo: 10.00 + Precio máximo: 20.00 | Devuelve el histórico 1 |
| 61 | Filter históricos | Sin filtros | Devuelve los 5 históricos |