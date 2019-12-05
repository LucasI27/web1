from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuario.db'
app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class cadastro(FlaskForm):
    username = StringField('usuario')
    password = PasswordField('senha')
    email = StringField('email')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def form():
    form = cadastro()
    if form.validate_on_submit():
        novo_user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(novo_user)
        db.session.commit()

    return render_template('cadastro.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)