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

def login():
    try:
        dataInput=request.form                                              # obtengo los datos del formulario
        all_users=Usuario.query.filter_by(email=dataInput["email"]).all()   # busco el mail en la base de datos
        result=usuarioSchemas.dump(all_users)                               # convierto el resultado en un diccionario
        data = {}
        code = 200
        if len(result)==0:                                                  # si no hay resultados, el mail no existe
            print("Usuario no encontrado")
            data = {
                "message": "Ese mail no fue encontrado en la base de datos",
            }
            code = 400
        else:                                                               # si hay resultados, el mail existe
            if result[0]["password"]==dataInput["password"]:                # si la contraseña coincide, login exitoso
                print("Login exitoso")
                data = {
                    "message": "Login exitoso",
                    "nombre": result[0]["nombre"],
                    "id": result[0]["id"],
                }
                code = 200
            else:                                                           # si la contraseña no coincide, login fallido
                print("Contraseña incorrecta")
                data = {
                    "message": "Contraseña incorrecta",
                }
                code = 404
        return jsonify(data), code
    except Exception as error:
        print("An exception occurred:", error)
        print("Error al intentar hacer login")
        data = {
            "message": "Error al intentar hacer login",
        }
        return jsonify(data), 400

def register():
    try:
        dataInput = request.form
        prev_user=Usuario.query.filter_by(email=dataInput["email"]).first()     # busco el mail en la base de datos
        data = {}
        code = 200
        if prev_user:                                                           # si el mail ya existe, no se puede registrar
            print("Usuario ya existe")
            data = {
                "message": "Ese mail ya existe en la base de datos",
            }
            code = 400
        else:                                                                   # si el mail no existe, se puede registrar
            nombre=dataInput['nombre']
            apellido=dataInput['apellido']
            fec_nac=datetime.strptime(dataInput['fec_nac'], '%d/%m/%Y').date()
            email=dataInput['email']
            password=dataInput['password']
            genero=dataInput['genero']
            print("previo init")
            new_usuario=Usuario(nombre,apellido,fec_nac,email,password,genero)
            db.session.add(new_usuario)
            db.session.commit()
            data = usuarioSchemas.dump(new_usuario)
            code = 201
        return jsonify(data), code
    except Exception as error:
        print("An exception occurred:", error)
        print("Error al intentar registrar un usuario")
        data = {
            "message": "Error al intentar registrar el usuario",
        }