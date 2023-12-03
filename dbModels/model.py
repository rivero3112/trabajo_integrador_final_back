from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# defino las tablas


def init_app(app):
     # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fit21User:Comision23520@coiote.ar:3306/fit21'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configura la base de datos con la aplicación Flask
    db.init_app(app)
    ma.init_app(app)

    # Creación de las tablas
    with app.app_context():
        db.create_all()