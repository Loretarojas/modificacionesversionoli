from . import db

class Mariposa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especie = db.Column(db.String(80), nullable=False)
    familia = db.Column(db.String(80), nullable=False)
    nombreCientifico = db.Column(db.String(80), nullable=False)
    pais = db.Column(db.String(80), nullable=False)
    peligroExtincion = db.Column(db.Boolean, default=False)
    migratoria = db.Column(db.Boolean, default=False)
