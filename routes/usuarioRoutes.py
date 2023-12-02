#from app import app
from . import usuario_routes  # Importa desde el propio paquete
from controller.usuarioController import login, register


app.post('/api/usuario/login')(login)

app.post('/api/usuario/register')(register)

# Crear un nuevo ingrediente
#app.post('/api/ingredientes')(crear_ingrediente)

# Actualizar un ingrediente por ID
#app.put('/api/ingredientes/<int:id>')(actualizar_ingrediente)

# Eliminar un ingrediente por ID
#app.delete('/api/ingredientes/<int:id>')(eliminar_ingrediente)