from flask import Flask
from flask_cors import CORS       # del modulo flask_cors importar CORS
from dbModels.model import init_app
from routes.usuarioRoutes import usuario_routes

app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

init_app(app)

# Registrar el blueprint de usuario
app.register_blueprint(usuario_routes)

if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000