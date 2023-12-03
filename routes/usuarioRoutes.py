#from app import app
from controller.usuarioController import login, register, getPhones, addPhone, editPhone, deletePhone
from flask import Blueprint

usuario_routes = Blueprint('usuario_routes', __name__)

usuario_routes.route('/api/usuario/login', methods=['POST'])(login)
usuario_routes.route('/api/usuario/register', methods=['POST'])(register)

# Telefonos
usuario_routes.route('/api/usuario/telefono/<int:userId>', methods=['GET'])(getPhones)
usuario_routes.route('/api/usuario/telefono/<int:userId>', methods=['POST'])(addPhone)
usuario_routes.route('/api/usuario/telefono/<int:id>', methods=['PUT'])(editPhone)
usuario_routes.route('/api/usuario/telefono/<int:id>', methods=['DELETE'])(deletePhone)