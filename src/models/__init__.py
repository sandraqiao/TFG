# imports de todos los modelos para que Base.metadata vea los hijos que tiene
# este file se lee cuando se hace "import models"

from models.libro import Libro
from models.saga import Libro
from models.autor import Autor
from models.lectura import Lectura
from models.tienda import Tienda
from models.historico_precio import HistoricoPrecio
from models.autor_libro import AutorLibro