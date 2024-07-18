from flask import Blueprint, request, jsonify, render_template, abort
from .models import Mariposa
from . import db

bp = Blueprint('main', __name__)

@bp.route('/api/mariposas/crear/', methods=['POST'])
def add_mariposa():
    data = request.json
    new_mariposa = Mariposa(
        nombre=data['nombre'],
        especie=data['especie'],
        familia=data['familia'],
        nombreCientifico=data['nombreCientifico'],
        pais=data['pais'],
        peligroExtincion=data['peligroExtincion'],
        migratoria=data['migratoria']
    )
    db.session.add(new_mariposa)
    db.session.commit()
    return jsonify(new_mariposa.id), 201

@bp.route('/api/mariposas/<int:id>', methods=['GET'])
def get_mariposa(id):
    mariposa = Mariposa.query.get_or_404(id)
    return jsonify({
        'id': mariposa.id,
        'nombre': mariposa.nombre,
        'especie': mariposa.especie,
        'familia': mariposa.familia,
        'nombreCientifico': mariposa.nombreCientifico,
        'pais': mariposa.pais,
        'peligroExtincion': mariposa.peligroExtincion,
        'migratoria': mariposa.migratoria
    })

@bp.route('/api/mariposas/<int:id>', methods=['PUT'])
def update_mariposa(id):
    mariposa = Mariposa.query.get_or_404(id)
    data = request.json

    mariposa.nombre = data.get('nombre', mariposa.nombre)
    mariposa.especie = data.get('especie', mariposa.especie)
    mariposa.familia = data.get('familia', mariposa.familia)
    mariposa.nombreCientifico = data.get('nombreCientifico', mariposa.nombreCientifico)
    mariposa.pais = data.get('pais', mariposa.pais)
    mariposa.peligroExtincion = data.get('peligroExtincion', mariposa.peligroExtincion)
    mariposa.migratoria = data.get('migratoria', mariposa.migratoria)

    db.session.commit()
    return jsonify({'message': 'Mariposa actualizada correctamente'}), 200

@bp.route('/api/mariposas/<int:id>', methods=['DELETE'])
def delete_mariposa(id):
    mariposa = Mariposa.query.get_or_404(id)
    db.session.delete(mariposa)
    db.session.commit()
    return jsonify({'message': 'Mariposa eliminada correctamente'}), 200

@bp.route('/cargabutterflies')
def cargabutterflies():
    return render_template('cargabutterflies.html')

@bp.route('/gestionbutterflies')
def gestionbutterflies():
    return render_template('gestionbutterflies.html')
