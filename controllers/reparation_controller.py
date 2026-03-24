from flask import Blueprint, request, jsonify
from services import reparation_service as svc
from schemas import ReparationSchema, ReparationCreateSchema
from marshmallow import ValidationError

rep_bp = Blueprint('reparations', __name__)
rep_schema      = ReparationSchema()
reps_schema     = ReparationSchema(many=True)
create_schema   = ReparationCreateSchema()

@rep_bp.route('/reparations', methods=['POST'])
def creer():
    try:
        data = create_schema.load(request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.messages}), 422
    rep = svc.creer_reparation(data)
    return jsonify(rep_schema.dump(rep)), 201

@rep_bp.route('/reparations/<numero_serie>', methods=['GET'])
def historique(numero_serie):
    reps = svc.get_historique(numero_serie)
    return jsonify(reps_schema.dump(reps)), 200

@rep_bp.route('/reparations/<int:rep_id>', methods=['GET'])
def detail(rep_id):
    rep = svc.get_reparation_by_id(rep_id)
    return jsonify(rep_schema.dump(rep)), 200

@rep_bp.route('/reparations/<int:rep_id>', methods=['DELETE'])
def supprimer(rep_id):
    svc.supprimer_reparation(rep_id)
    return jsonify({"message": "Réparation supprimée"}), 200
