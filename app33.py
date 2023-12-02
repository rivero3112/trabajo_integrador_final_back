from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

@app.route('/',methods=['GET'])
def index():
    return jsonify({'mensaje':'Bienvenido a mi API'})


# crea los endpoint o rutas (json)
# @app.route('/productos',methods=['GET'])
# def get_Productos():
#     all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
#     result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
#                                                  # trae todos los registros de la tabla
#     return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




# @app.route('/productos/<id>',methods=['GET'])
# def get_producto(id):
#     producto=Producto.query.get(id)
#     return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro




# @app.route('/productos/<id>',methods=['DELETE'])
# def delete_producto(id):
#     producto=Producto.query.get(id)
#     db.session.delete(producto)
#     db.session.commit()
#     return producto_schema.jsonify(producto)   # me devuelve un json con el registro eliminado


# @app.route('/productos', methods=['POST']) # crea ruta o endpoint
# def create_producto():
#     #print(request.json)  # request.json contiene el json que envio el cliente
#     nombre=request.json['nombre']
#     precio=request.json['precio']
#     stock=request.json['stock']
#     imagen=request.json['imagen']
#     new_producto=Producto(nombre,precio,stock,imagen)
#     db.session.add(new_producto)
#     db.session.commit()
#     return producto_schema.jsonify(new_producto)


# @app.route('/productos/<id>' ,methods=['PUT'])
# def update_producto(id):
#     producto=Producto.query.get(id)
 
#     nombre=request.json['nombre']
#     precio=request.json['precio']
#     stock=request.json['stock']
#     imagen=request.json['imagen']


#     producto.nombre=nombre
#     producto.precio=precio
#     producto.stock=stock
#     producto.imagen=imagen


#     db.session.commit()
#     return producto_schema.jsonify(producto)


# programa principal *******************************

from routes import usuarioRoutes

if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000