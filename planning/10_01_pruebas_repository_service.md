# Pruebas de services

| Orden | Acción | Datos | Esperado |
| ----- | ------ | ----- | -------- |
| 1 | Create saga | Nombre: Crónicas de Narnia | Se crea correctamente |
| 2 | Create saga | Nombre: Crónicas de Narnia | ValueError por nombre repetido |
| 3 | Create saga | Nombre: Saga de prueba | Se crea correctamente |
| 4 | Update saga | Cambiamos Saga de prueba. Nuevo nombre: El Archivo de las Tormentas | Se modifica correctamente |
| 5 | Update saga | Cambiamos El Archivo de las Tormentas. Nuevo nombre: Crónicas de Narnia | ValueError por nombre repetido |
| 6 | Update saga | ID de una saga inexistente. Nombre: Saga inexistente | ValueError por saga inexistente |
| 7 | Delete saga | ID de El Archivo de las Tormentas | Se elimina correctamente |
| 8 | Delete saga | ID de una saga inexistente | ValueError por saga inexistente |
| 9 | Create autor | Nombre: J.R.R. Tolkien | Se crea correctamente |
| 10 | Create autor | Nombre: J.R.R. Tolkien | ValueError por nombre repetido |
| 11 | Create autor | Nombre: J.K. Rowling | Se crea correctamente |
| 12 | Update autor | Cambiamos J.K. Rowling. Nuevo nombre: George R.R. Martin | Se modifica correctamente |
| 13 | Update autor | Cambiamos George R.R. Martin. Nuevo nombre: J.R.R. Tolkien | ValueError por nombre repetido |
| 14 | Update autor | ID de un autor inexistente. Nombre: Autor inexistente | ValueError por autor inexistente |
| 15 | Delete autor | ID de George R.R. Martin | Se elimina correctamente |
| 16 | Delete autor | ID de un autor inexistente | ValueError por autor inexistente |
| 17 | Create libro | Título: El Hobbit. ISBN: 9780261102217. Páginas: 310. Saga: Crónicas de Narnia. Wishlist: false | Se crea correctamente |
| 18 | Create libro | ISBN: 9780261102217 | ValueError por ISBN repetido |
| 19 | Create libro | Saga inexistente | ValueError por saga inexistente |
| 20 | Create libro | Páginas: 0 | ValueError por número de páginas inválido |
| 21 | Create libro | Páginas: -10 | ValueError por número de páginas inválido |
| 22 | Create libro | Wishlist: false. Prioridad: 3 | ValueError por prioridad sin Wishlist |
| 23 | Create libro | Wishlist: true. Prioridad: None | Se crea correctamente con prioridad 0 |
| 24 | Create libro | Wishlist: true. Prioridad: 5 | Se crea correctamente |
| 25 | Update libro | Cambiar título del libro creado | Se modifica correctamente |
| 26 | Update libro | Cambiar ISBN por uno perteneciente a otro libro | ValueError por ISBN repetido |
| 27 | Update libro | ID de libro inexistente | ValueError por libro inexistente |
| 28 | Update libro | Saga inexistente | ValueError por saga inexistente |
| 29 | Update libro | Páginas: 0 | ValueError por número de páginas inválido |
| 30 | Update libro | Wishlist: false. Prioridad: 3 | ValueError por prioridad sin Wishlist |
| 31 | Update libro | Wishlist: true. Prioridad: None | Se modifica correctamente con prioridad 0 |
| 32 | Delete libro | ID de un libro existente | Se elimina correctamente |
| 33 | Delete libro | ID de un libro inexistente | ValueError por libro inexistente |
| 34 | Create tienda | Nombre: Amazon. URL: https://www.amazon.es | Se crea correctamente |
| 35 | Create tienda | Nombre: Amazon | ValueError por nombre repetido |
| 36 | Create tienda | Nombre: Fnac. URL: https://www.fnac.es | Se crea correctamente |
| 37 | Update tienda | Cambiar nombre de Fnac a Casa del Libro | Se modifica correctamente |
| 38 | Update tienda | Cambiar nombre a Amazon | ValueError por nombre repetido |
| 39 | Update tienda | ID de una tienda inexistente | ValueError por tienda inexistente |
| 40 | Delete tienda | ID de Casa del Libro | Se elimina correctamente |
| 41 | Delete tienda | ID de una tienda inexistente | ValueError por tienda inexistente |
| 42 | Create lectura | Libro existente. Estado: Leyendo. Valoración: 8. Fecha inicio: 2026-08-01. Fecha fin: None. Formato: Físico | Se crea correctamente |
| 43 | Create lectura | Libro inexistente | ValueError por libro inexistente |
| 44 | Create lectura | Estado: Inventado | ValueError por estado inválido |
| 45 | Create lectura | Valoración: -1 | ValueError por valoración fuera de rango |
| 46 | Create lectura | Valoración: 11 | ValueError por valoración fuera de rango |
| 47 | Create lectura | Formato: Papel | ValueError por formato inválido |
| 48 | Create lectura | Fecha inicio: 2026-08-10. Fecha fin: 2026-08-01 | ValueError por fechas inválidas |
| 49 | Update lectura | Cambiar estado a Leído y añadir fecha fin: 2026-08-10 | Se modifica correctamente |
| 50 | Update lectura | ID de lectura inexistente | ValueError por lectura inexistente |
| 51 | Delete lectura | ID de una lectura existente | Se elimina correctamente |
| 52 | Delete lectura | ID de una lectura inexistente | ValueError por lectura inexistente |
| 53 | Create autor-libro | Libro existente + Autor existente | Se crea correctamente |
| 54 | Create autor-libro | Misma combinación de libro + autor | ValueError por relación existente |
| 55 | Create autor-libro | Libro inexistente + Autor existente | ValueError por libro inexistente |
| 56 | Create autor-libro | Libro existente + Autor inexistente | ValueError por autor inexistente |
| 57 | Delete autor-libro | Relación existente | Se elimina correctamente |
| 58 | Delete autor-libro | Relación inexistente | ValueError por relación inexistente |
| 59 | Create histórico precio | Libro existente + Tienda existente. Precio: 15.99. Descuento: 10 | Se crea correctamente |
| 60 | Create histórico precio | Libro inexistente | ValueError por libro inexistente |
| 61 | Create histórico precio | Tienda inexistente | ValueError por tienda inexistente |
| 62 | Create histórico precio | Precio: -5 | ValueError por precio fuera de rango |
| 63 | Create histórico precio | Descuento: -1 | ValueError por porcentaje fuera de rango |
| 64 | Create histórico precio | Descuento: 101 | ValueError por porcentaje fuera de rango |
| 65 | Create histórico precio | Descuento: None | Se crea correctamente |
| 66 | Create histórico precio | Precio: 0 | Se crea correctamente |
| 67 | Update histórico precio | Cambiar precio a 12.99 | Se modifica correctamente |
| 68 | Update histórico precio | ID de histórico inexistente | ValueError por histórico inexistente |
| 69 | Update histórico precio | Libro inexistente | ValueError por libro inexistente |
| 70 | Update histórico precio | Tienda inexistente | ValueError por tienda inexistente |
| 71 | Update histórico precio | Precio: -1 | ValueError por precio fuera de rango |
| 72 | Update histórico precio | Descuento: 101 | ValueError por porcentaje fuera de rango |
| 73 | Delete histórico precio | ID de un histórico existente | Se elimina correctamente |
| 74 | Delete histórico precio | ID de un histórico inexistente | ValueError por histórico inexistente |

## Pruebas de borrado en cascada

| Orden | Acción | Datos | Esperado |
| ----- | ------ | ----- | -------- |
| 75 | Delete saga | Borrar una saga que tenga libros asociados | Los libros mantienen su `id_saga` con valor `NULL` |
| 76 | Delete libro | Borrar un libro que tenga lecturas asociadas | Se eliminan sus lecturas |
| 77 | Delete libro | Borrar un libro que tenga históricos de precio asociados | Se eliminan sus históricos de precio |
| 78 | Delete libro | Borrar un libro que tenga relaciones autor-libro | Se eliminan sus relaciones autor-libro |
| 79 | Delete tienda | Borrar una tienda con históricos de precio asociados | Se eliminan sus históricos de precio |
| 80 | Delete autor | Borrar un autor con relaciones autor-libro | Se eliminan sus relaciones autor-libro |