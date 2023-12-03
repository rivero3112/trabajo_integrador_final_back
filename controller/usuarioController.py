from dbModels.model import Usuario, Emergencia_usuario, UsuarioSchema, Emergencia_usuarioSchema, db
from flask import jsonify, request
from datetime import datetime

# Instancia de Schema
usuarioSchemas = UsuarioSchema(many=True)
telefonosEmergenciaSchemas = Emergencia_usuarioSchema(many=True)

