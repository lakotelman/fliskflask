from flask import Flask, render_template
from config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    from app.blueprints.main import bp as main_bp

    app.register_blueprint(main_bp)
    from app.blueprints.blog import bp as blog_bp

    app.register_blueprint(blog_bp)
    from app.blueprints.auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    return app
