from dbModels.model import Usuario, Emergencia_usuario, UsuarioSchema, Emergencia_usuarioSchema, db
from flask import jsonify, request
from datetime import datetime

# Instancia de Schema
usuarioSchemas = UsuarioSchema(many=True)
telefonosEmergenciaSchemas = Emergencia_usuarioSchema(many=True)


#ABM telefonos
def addPhone(userId):
    try:
        dataInput=request.form                                              # obtengo los datos del formulario
        idUsuario=userId
        nombre=dataInput['nombre']
        telefono=dataInput['telefono']
        new_telefono=Emergencia_usuario(idUsuario,nombre,telefono)
        db.session.add(new_telefono)
        db.session.commit()
        data = telefonosEmergenciaSchemas.dump(new_telefono)
        code = 201
        return data, code
    except Exception as error:
        print("An exception occurred:", error)
        print("Error ")
        data = {
            "message": "Error ",
        }
        return jsonify(data), 400

def getPhones(userId):
    try:
        all_phones=Emergencia_usuario.query.filter_by(idUsuario=userId).all()    # busco el mail en la base de datos
        result=telefonosEmergenciaSchemas.dump(all_phones)                       # convierto el resultado en un diccionario
        data = {}
        code = 200
        if result:
            data = result
            code = 200
        else:
            data = []
            code = 404
        return jsonify(data), code
    except Exception as error:
        print("An exception occurred:", error)
        print("Error ")
        data = {
            "message": "Error ",
        }
        return jsonify(data), 400

def editPhone(id):
    try:
        dataInput=request.form                                              # obtengo los datos del formulario
        telefono=Emergencia_usuario.query.get(id)
        telefono.nombre=dataInput['nombre']
        telefono.telefono=dataInput['telefono']
        db.session.commit()
        return telefonosEmergenciaSchemas.jsonify(telefono)
    except Exception as error:
        print("An exception occurred:", error)
        print("Error ")
        data = {
            "message": "Error ",
        }
        return jsonify(data), 400

def deletePhone(id):
    try:
        telefono=Emergencia_usuario.query.get(id)
        db.session.delete(telefono)
        db.session.commit()
        return "ok", 200
    except Exception as error:
        print("An exception occurred:", error)
        print("Error ")
        data = {
            "message": "Error ",
        }
        return jsonify(data), 400