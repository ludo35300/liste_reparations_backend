from flask import Blueprint, jsonify
from services.reparation_service import get_stats
from services.piece_service import pieces_les_plus_changees

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/stats', methods=['GET'])
def stats():
    data = get_stats()
    data['pieces_les_plus_changees'] = [
        {"ref": r, "designation": d, "total": t}
        for r, d, t in pieces_les_plus_changees(10)
    ]
    return jsonify(data), 200