# Diario de Decisiones

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