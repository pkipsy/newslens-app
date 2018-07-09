from flask import Flask

import sys
#sys.path.insert(0, '/Documents/Insight/flask_app/app_folder')
sys.path.insert(0, '/newslens-app/app_folder')

from keysecret import keys

app = Flask(__name__, instance_path=keys['path'])
app.config['SECRET_KEY'] = keys['secret']
