from db import db


# Define the SQLAlchemy model for the search history
class ModeloBusca(db.Model):
    __tablename__ = "coletas"

    id = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.DateTime, nullable=False)
    CO = db.Column(db.Integer, nullable=False)
    coleta = db.Column(db.String(50), nullable=False)