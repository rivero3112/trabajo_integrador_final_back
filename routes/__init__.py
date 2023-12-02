from flask import Blueprint
usuario_routes = Blueprint('usuario_routes', __name__)
# Importa las rutas desde el archivo usuarioRoutes.py
from .usuarioRoutes import *
# Puedes agregar más Blueprints aquí si es necesario