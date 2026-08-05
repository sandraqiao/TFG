# Diario de Decisiones

## Ciclio personal de sesiones
1. Definir qué quiero hacer.
2. Pensar en métodos y clases que se necesiten.
3. Implementar.
4. Probar que funciona.
5. Hacer un commit.
6. Anotar en el diario decisiones importantes si ha habido alguna.

## Tecnologías
- Usar streamlit porque requiere menos esfuerzo para tener un front decente, y así poder centrarme en el back.
- Usar PostgreSQL porque es un SGBD más completo y utilizado en empresas que escala mejor en caso de necesitarlo en un futuro.
- Usar una API que recoga los datos de los libros y scraping solo para los precios de estos: una API es más rápida y requiere menos código que si scrapeamos por esos datos.
- Usar SQLAlchemy para poder trabajar con los libros más cómodamente (como si fueran objetos).

## Diagrama del dominio
- Se ha decidido modelar el historial de precios como una entidad independiente (HistorialPrecios) en vez de considerarlo como un simple atributo de la relación entre Libro y Tienda como se había planteado en un principio, porque como quiero guardar mucha información por cada scraping que se haga (precio, fecha, tienda...) el atributo deja de ser estático y pasa a ser una entidad con info propia.

## Diagrama Entidad-Relacion
- Se ha modelado el ISBN como un atributo del libro utilizándolo como identificador bibliográfico de referencia aunque un libro pueda tener varios ISBNs distintos. Se pretende gestionar obras y no ediciones en concreto.
- Las cardinalidades mínimas se han puesto de manera flexible (0) para que la lógica del dominio no afecte de manera negativa a la inserción progresiva de datos y evitar así dependencias cirulares durante la implementación.

## Diseño de la estructura de src
- database: contiene el padre de los modelos (base.py) y el engine para poder conectarnos con PostgreSQL (database.py)
- models: contiene los modelos que se usan y un archivo con todos los imports de estos (__init__.py)
- repositories: contiene las llamadas directas a la bbdd
- scraper: 
- services: contiene toda la lógica del sistema y realiza todos los checks necesarios
- ui: 
- utils:
    - constants: contiene las variables constantes de los atributos de los modelos

## Ideas que no se van a aplicar en esta versión del proyecto
- Añadir a lectura idioma porque hoy te lees libro x en español y mañana te lo leer en inglés.


# Diario de objetivos y trabajo realizado a partir del inicio del desarrollo
## 26/07/2026
### Objetivos
- Configurar el entorno de desarrillo
- Comprobar que Streamlit funciona
### Trabajo hecho
- Creación del entorno virtual (venv)
- Instalación de dependencias
- Generación del requirements.txt
- Configuración del .gitignore
- Inicio correcto de Streamlit
### Próximos pasos
- Configurar PostgreSQL
- Integrar SQLAlchemy
- Crear los primeros modelos de la base de datos

## 27/07/2026
### Objetivos
- Configurar PostgreSQL
- Integrar SQLAlchemy
- Crear los primeros modelos de la base de datos
### Trabajo hecho
- Instalación de PostgreSQL
- Creación de una bbdd en PostgreSQL para el proyecto
- Conectar SQLAlchemy con PostgreSQL (database.py)
- Inicio de la creación de la primera tabla "Libro" desde libro.py
### Próximos pasos
- Terminar modelos
- Crear "constants" para las variables que sean listados cerrados.

## 28/07/2026
### Objetivos
- Terminar los modelos de la base de datos
- Crear las tablas en PostgreSQL
- Comprobar que funciona el guardado
- Crear "constants"
### Trabajo hecho
- Creación de los modelos con sus atributos básicos
- Inicio de las relaciones (no terminado)
### Próximos pasos
- Seguir con lo que estaba haciendo y avanzar con los puntos no vistos aún

## 29/07/2026
### Objetivos
- Terminar los modelos de la bbdd
- Crear las tablas en PostgreSQL
- Comprobar que funciona el guardado
### Trabajo hecho
- Modelos de la bbdd terminados
- Creación de las tablas con SQLAlchemy y comprobado en PostgreSQL
- Creación de un libro de prueba y comprobación de que aparece en PostgreSQL correctamente
### Próximos pasos
- Falta por crear "constants"
- Empezar con la lógica de la aplicación

## 30/07/2026
### Objetivos
- Crear "constants"
- Diseñar la estructura de la capa de acceso a datos
- Implementar CRUD de Saga
- Implementar CRUD de Libro
### Trabajo hecho
- Constanst creadas
- Planeada la estructura de la capa de acceso a datos
- Creado repository de saga
### Siguientes pasos
- Terminar todos los CRUD que quedan

## 03/08/2026
### Objetivos
- Implementar los CRUD que faltan
### Trabajo hecho
- Implementar CRUD de Libro
- Implementar CRUD de Autor
- Implementar CRUD de Lectura
- Implementar CRUD de Tienda
- Implementar CRUD de HistoricoPrecio
- Implementar CRUD de AutorLibro
### Siguientes pasos
- Empezar con services

## 04/08/2026
### Objetivos
- Implementar saga_service completo
- Empezar con libro_service
### Trabajo hecho
- Añadida función get_by_exact_name() en saga_repository
- Creado el _build_saga(), create(), update y delete en saga_service
- Añadida función get_by_exact_name() y get_by_isbn en libro_repository
- Creado el _build_saga(), create(), update y delete en libro_service
### Siguientes pasos
- Mirar dependencias de borrado entre saga y libro
- Continuar con los services

## 05/08/2026
### Objetivos
- Realizar dependencias de borrado
- Continuar con los services
### Trabajo hecho
- Realizadas y finiquitadas todas las dependencias de borrado
- Añadidas las constraints en los modelos
- Cambios menores en constants.py 
- Finiquitado (por ahora) libro/saga_repository y libro/saga_service
