from flask import Flask, request, render_template,  abort, redirect, url_for, session, escape
from .routes.index import Routeclass
import sample_flask_app.config.devConfig as config
import sys
sys.path.append("..")

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = config.SECRET_KEY
app.debug = config.DEBUG
app.register_blueprint(Routeclass.routes)

