from flask import Flask

from app_folder.keysecret import keys

app = Flask(__name__, instance_path=keys['path'])
app.config['SECRET_KEY'] = keys['secret']

from app_folder import routes

