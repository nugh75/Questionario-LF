from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Risposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    testo = db.Column(db.Text, nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    risposte = db.Column(db.JSON, nullable=False)
    
    # Medie per area
    media_motivazione = db.Column(db.Float)
    media_risorse = db.Column(db.Float)
    media_elaborazione = db.Column(db.Float)
    media_tempo = db.Column(db.Float)
    media_strategie = db.Column(db.Float)
    media_concentrazione = db.Column(db.Float)
    media_selezione = db.Column(db.Float)
    media_atteggiamento = db.Column(db.Float)
    media_monitoraggio = db.Column(db.Float)
    media_ansia = db.Column(db.Float)
