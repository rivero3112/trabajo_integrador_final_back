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
        
class Usuario(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(50))
    apellido=db.Column(db.String(50))
    fec_nac=db.Column(db.Date)
    email=db.Column(db.String(60))
    password=db.Column(db.String(255))
    genero=db.Column(db.String(10))
    def __init__(self,nombre,apellido,fec_nac,email,password,genero):   #crea el  constructor de la clase
        self.nombre=nombre
        self.apellido=apellido
        self.fec_nac=fec_nac
        self.email=email
        self.password=password
        self.genero=genero

class Emergencia_usuario(db.Model):                     # la clase emergencia_usuario hereda de db.Usuario    
    id=db.Column(db.Integer, primary_key=True)          #define los campos de la tabla
    idUsuario=db.Column(db.Integer)
    nombre=db.Column(db.String(255))
    telefono=db.Column(db.String(20))
    def __init__(self, idUsuario, nombre, telefono):      #crea el  constructor de la clase
        self.idUsuario=idUsuario
        self.nombre=nombre
        self.telefono=telefono

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','apellido','fec_nac','email','password','genero')

class Emergencia_usuarioSchema(ma.Schema):
    class Meta:
        fields=('id','idUsuario','nombre','telefono')