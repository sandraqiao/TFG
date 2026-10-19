# Tecnologías y herramientas

| Tecnología/Herramienta | Justificación |
|------------|---------------|
| **Git** | Sistema de control de versiones utilizado para facilitar la gestión de cambios durante el desarrollo del proyecto. |
| **Python** | Lenguaje principal de desarrollo debido a su disponibilidad de librerías para el desarrollo de aplicaciones web, el acceso a bases de datos y el web scraping. |
| **Streamlit** | Framework elegido para el desarrollo de la interfaz web, ya que permite crear aplicaciones funcionales de forma rápida y centrar el esfuerzo en la lógica de negocio y el acceso a datos. |
| **PostgreSQL** | Sistema gestor de bases de datos relacional utilizado para almacenar de forma persistente la información de libros, autores, sagas, lecturas, tiendas e históricos de precios. |
| **SQLAlchemy** | ORM utilizado para facilitar la interacción entre la aplicación y la base de datos, permitiendo trabajar con modelos y objetos Python y gestionar las operaciones de acceso a datos. |
| **BeautifulSoup** | Librería utilizada para analizar el contenido HTML obtenido durante el web scraping y extraer información bibliográfica y datos relacionados con los precios de los libros. |
| **Selenium** | Herramienta utilizada para automatizar la navegación web y obtener el contenido de Casa del Libro necesario para realizar las extracciones de información. |
| **Docker** | Plataforma utilizada para contenerizar la aplicación y facilitar la configuración y ejecución del entorno de desarrollo. |

# Arquitectura por capas
La aplicación se organiza siguiendo una arquitectura por capas para separar la interfaz de usuario, la lógica de negocio y el acceso a datos, con el objetivo de facilitar el mantenimiento, mejorar la organización del código y favorecer la reutilización de componentes.

1. **UI (User Interface):** desarrollada con Streamlit, es la encargada de mostrar la información al usuario, recoger sus acciones y gestionar la navegación entre las distintas páginas de la aplicación.
2. **Service:** contiene la lógica de negocio, las validaciones y las comprobaciones necesarias antes de realizar operaciones sobre los datos.
3. **Repository:** responsable del acceso a los datos, encapsulando las operaciones de consulta, creación, modificación y eliminación sobre la base de datos mediante SQLAlchemy.
4. **Database:** formada por PostgreSQL y los modelos definidos con SQLAlchemy, se encarga del almacenamiento persistente de la información.