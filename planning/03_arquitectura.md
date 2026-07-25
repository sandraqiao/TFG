# Tecnologías y herramientas

| Tecnología/Herramienta | Justificación |
|------------|---------------|
| **Git** | Sistema de control de versiones utilizado para facilitar la gestión de cambios durante el desarrollo del proyecto. |
| **Python** | Lenguaje principal de desarrollo debido a su amplia disponibilidad de librerías para desarrollo web, acceso a bases de datos y web scraping. |
| **Streamlit** | Framework elegido para el desarrollo de la interfaz web por permitir crear aplicaciones funcionales de forma rápida, reduciendo el tiempo dedicado al desarrollo del front-end y permitiendo centrar el esfuerzo en la lógica de negocio y el acceso a datos. |
| **PostgreSQL** | Sistema Gestor de Bases de Datos relacional seleccionado por su robustez, buen rendimiento y amplia utilización en entornos profesionales. |
| **SQLAlchemy** | ORM utilizado para facilitar la interacción entre la aplicación y la base de datos, permitiendo trabajar con objetos Python en lugar de escribir consultas SQL manualmente en la mayor parte de la aplicación. |
| **API de libros** | Se utilizará una API para obtener la información bibliográfica de los libros (título, autor, sinopsis, portada, etc.), evitando realizar scraping sobre datos estructurados que ya están disponibles mediante un servicio especializado. |
| **BeautifulSoup** | Librería empleada para realizar web scraping sobre distintas tiendas y obtener el precio actualizado de los libros. |

# Arquitectura por capas
La aplicación se organizará siguiendo una arquitectura por capas para separar la interfaz de usuario, la interfaz lógica de negocio y el acceso a datos con el objetivo de faciliatar el mantenimiento, mejorar la escalabilidad y ayudar con la reutilización de componentes.

1. **UI (User interface):** desarrollada con Streamlit, será la encargada de mostrar la información al usuario y recoger sus acciones.
2. **Service:** encargada de la lógica de negocio de la aplicación.
3. **Repository:** responsable del acceso a los datos, encapsulando las operaciones realizadas sobre la base de datos mediante SQLAlchemy.
4. **Database:** formada por PostgreSQL y los modelos definidos con SQLAlchemy, será la encargada del almacenamiento persistente de la información.