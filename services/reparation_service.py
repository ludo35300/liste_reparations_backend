from extensions import db
from models import Reparation, PieceChangee
from datetime import datetime

def creer_reparation(data: dict) -> Reparation:
    rep = Reparation(
        numero_serie    = data['numero_serie'].strip().upper(),
        machine_type    = data.get('machine_type', ''),
        technicien      = data.get('technicien', ''),
        date_reparation = datetime.strptime(data['date_reparation'], '%d/%m/%Y').date(),
        notes           = data.get('notes', '')
    )
    db.session.add(rep)
    db.session.flush()  # Obtenir l'ID avant le commit

    for p in data.get('pieces', []):
        piece = PieceChangee(
            reparation_id = rep.id,
            ref_piece     = p['ref_piece'],
            designation   = p.get('designation', ''),
            quantite      = int(p.get('quantite', 1))
        )
        db.session.add(piece)

    db.session.commit()
    return rep

def get_historique(numero_serie: str) -> list:
    return Reparation.query \
        .filter_by(numero_serie=numero_serie.upper()) \
        .order_by(Reparation.date_reparation.desc()) \
        .all()

def get_reparation_by_id(rep_id: int) -> Reparation:
    return Reparation.query.get_or_404(rep_id)

def supprimer_reparation(rep_id: int):
    rep = Reparation.query.get_or_404(rep_id)
    db.session.delete(rep)
    db.session.commit()

def get_stats() -> dict:
    total = Reparation.query.count()
    machines = db.session.query(Reparation.numero_serie).distinct().count()
    from models import PieceChangee
    total_pieces = db.session.query(
        db.func.sum(PieceChangee.quantite)
    ).scalar() or 0
    return {
        "total_reparations": total,
        "machines_uniques":  machines,
        "total_pieces":      total_pieces
    }
