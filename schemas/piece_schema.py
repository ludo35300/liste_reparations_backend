from extensions import marshmallow
from models import PieceChangee

class PieceChangeeSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = PieceChangee
        load_instance = True
        exclude = ('reparation_id',)