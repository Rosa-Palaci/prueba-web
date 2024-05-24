from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_lista = db.Column(db.String(50), nullable=False)
    grupo = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    ciclo_escolar = db.Column(db.String(50), nullable=False)
