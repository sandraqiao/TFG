# Verificación y validación de services

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
| 85 | Delete saga | ID de una saga existente con libros asociados: Crónicas de Narnia. Libro asociado: Libro de Wishlist | Los libros asociados mantienen su id_saga con valor NULL |
| 86 | Delete libro | ID de un libro existente con lecturas asociadas: Libro de Wishlist | Se elimina el libro y sus lecturas asociadas |
| 87 | Delete libro | ID de un libro existente con históricos de precio asociados: Libro de Wishlist | Se elimina el libro y sus históricos de precio asociados |
| 88 | Delete libro | ID de un libro existente con relaciones autor-libro: Libro de Wishlist + J.R.R. Tolkien | Se elimina el libro y sus relaciones autor-libro asociadas |
| 89 | Delete tienda | ID de una tienda existente con históricos de precio asociados: Amazon | Se elimina la tienda y sus históricos de precio asociados |
| 90 | Delete autor | ID de un autor existente con relaciones autor-libro: J.R.R. Tolkien + Libro de Wishlist | Se elimina el autor y sus relaciones autor-libro asociadas |