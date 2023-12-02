from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
#crea el objeto ma de de la clase Marshmallow

# importo la clase de modelos

db=SQLAlchemy()   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow()   
# defino la tabla
class Usuario(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(50))
    apellido=db.Column(db.String(50))
    fec_nac=db.Column(db.Date)
    email=db.Column(db.String(60))
    password=db.Column(db.String(255))
    genero=db.Column(db.String(10))
    def __init__(self,nombre,precio,stock,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.fec_nac=fec_nac
        self.email=email
        self.password=password
        self.genero=genero

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','apellido','fec_nac','email','password','genero')

usuario_schema=UsuarioSchema()            # El objeto producto_schema es para traer un producto
usuarios_schema=UsuarioSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto
#tabla_schema=TablaSchema()
#tablas_schema=TablaSchema(many=True)



from .model import db

def init_app(app):
    # Configura la base de datos con la aplicación Flask
    db.init_app(app)
    ma.init_app(app)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fit21User:Comision23520@coiote.ar:3306/fit21'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Creación de las tablas
    with app.app_context():
        db.create_all()