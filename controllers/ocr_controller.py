from flask import Blueprint, request, jsonify
from services.ocr_service import analyser_fiche

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route('/scan', methods=['POST'])
def scan():
    if 'image' not in request.files:
        return jsonify({"error": "Aucun fichier image reçu"}), 400
    fichier = request.files['image']
    if fichier.filename == '':
        return jsonify({"error": "Fichier vide"}), 400

    result = analyser_fiche(fichier.read())
    return jsonify(result), 200