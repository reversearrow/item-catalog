import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app(config_filename):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), 'config', config_filename + '.py')
    app.config.from_pyfile(cfg)

    from models import db
    db.init_app(app)

    from views import catalog_bp
    app.register_blueprint(catalog_bp, url_prefix='/')

    csrf = CSRFProtect()
    csrf.init_app(app)

    return app
