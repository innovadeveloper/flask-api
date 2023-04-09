import logging
import os
from flask import Flask
from app import main
from app.main.database import db, migration
from app.main.logging import LOGGING_CONFIG
from app.main.api import api

# Flask App Initialization
app = Flask(__name__)
# configuration = main.settings[os.environ.get('APPLICATION_ENV', 'default')]
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'


# Logs Initialization
console = logging.getLogger('console')

# Database ORM Initialization
from app import models
db.init_app(app)

# Database Migrations Initialization
migration.init_app(app, db)

# Flask API Initialization
api.init_app(app)
