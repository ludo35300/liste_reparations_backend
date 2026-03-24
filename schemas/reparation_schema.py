from extensions import marshmallow
from marshmallow import fields, validate
from models import Reparation
from .piece_schema import PieceChangeeSchema

class ReparationSchema(marshmallow.SQLAlchemyAutoSchema):
    pieces = fields.List(fields.Nested(PieceChangeeSchema), dump_default=[])

    class Meta:
        model = Reparation
        load_instance = True
        include_fk = True

class ReparationCreateSchema(marshmallow.Schema):
    numero_serie    = fields.Str(required=True, validate=validate.Length(min=1))
    machine_type    = fields.Str(required=True)
    technicien      = fields.Str(load_default='')
    date_reparation = fields.Date(required=True, format='%d/%m/%Y')
    notes           = fields.Str(load_default='')
    pieces          = fields.List(fields.Dict(), load_default=[])