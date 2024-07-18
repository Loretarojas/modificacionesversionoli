from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder="../pages")
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/CSS/<path:filename>')
    def serve_css(filename):
        return send_from_directory('../CSS', filename)

    @app.route('/js/<path:filename>')
    def serve_js(filename):
        return send_from_directory('../js', filename)

    return app
