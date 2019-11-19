from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#Initialize the app
app = Flask(__name__,instance_relative_config = True)

#The configuration settings
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initialize Bootstrap
bootstrap = Bootstrap(app)

from main import views