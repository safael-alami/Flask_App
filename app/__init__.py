from flask import Flask
from app.config import Config
from app.db import mysql, create_tables

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

 
    mysql.init_app(app)

    create_tables(app)

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app
