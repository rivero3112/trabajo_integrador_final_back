from dbModels.model import Usuario, UsuarioSchema
from flask import jsonify, request

def login():
    all_users=Usuario.query.all()              # el metodo query.all() lo hereda de db.Model
    result=usuarioSchema.dump(all_users)     # el metodo dump() lo hereda de ma.schema y
    return jsonify(result)                          # retorna un JSON de todos los registros de la tabla
    #data = request.form
    #print(data)
    #return jsonify(data), 201

def register():
    data = request.form
    print(data)
    return jsonify(data), 201