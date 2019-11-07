from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

class usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<MSG %r>' % self.msg


