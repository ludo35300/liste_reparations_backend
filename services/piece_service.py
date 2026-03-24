from extensions import db
from models import PieceChangee

def get_pieces_par_reparation(rep_id: int) -> list:
    return PieceChangee.query.filter_by(reparation_id=rep_id).all()

def pieces_les_plus_changees(limit=10) -> list:
    return db.session.query(
        PieceChangee.ref_piece,
        PieceChangee.designation,
        db.func.sum(PieceChangee.quantite).label('total')
    ).group_by(PieceChangee.ref_piece) \
     .order_by(db.desc('total')) \
     .limit(limit).all()