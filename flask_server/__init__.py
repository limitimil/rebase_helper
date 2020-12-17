from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap

app = Flask(__name__)
## for form
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
CORS(app)
Bootstrap(app)

