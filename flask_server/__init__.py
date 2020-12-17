from flask import Flask
from flask_cors import CORS

static_folder = 'bootstrap'
app = Flask(__name__, static_folder=static_folder)
## for form
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
CORS(app)

