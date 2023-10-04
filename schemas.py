from marshmallow import Schema, fields

class ModeloBuscaSchema(Schema):
    id = fields.Int(dump_only=True)
    hora = fields.DateTime(required=True)
    CO = fields.Int(required=True)
    coleta = fields.Str(required=True)

