from extensions import db
from datetime import datetime

class Reparation(db.Model):
    __tablename__ = 'reparations'

    id             = db.Column(db.Integer, primary_key=True)
    numero_serie   = db.Column(db.String(100), nullable=False, index=True)
    machine_type   = db.Column(db.String(100), nullable=False)   # ex: "MOULIN SANTOS 40AN" / "Conti CC102"
    technicien     = db.Column(db.String(100), default='')
    date_reparation = db.Column(db.Date, nullable=False)
    notes          = db.Column(db.Text, default='')
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    # Relation 1 → N avec les pièces
    pieces = db.relationship('PieceChangee', backref='reparation',
                              lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Reparation {self.numero_serie} - {self.date_reparation}>'