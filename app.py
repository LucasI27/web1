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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def form():
    form = cadastro()
    if form.validate_on_submit():
    	return '<h1>a senha é {}. e o usuario é {}.'.format(form.password.data, form.username.data)
    return render_template('cadastro.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)