from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'vcjgdvoiagvfdigahfj*^%$&$(&^hjgvsdcyws'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0212@localhost/mysaleappdb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app = app)
app.app_context().push()
login = LoginManager(app)

