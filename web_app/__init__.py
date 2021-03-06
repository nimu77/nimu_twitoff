# web_app/__init__.py

from flask import Flask
from web_app.model import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.bike_trail import bike_trail
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.stats_routes import stats_routes
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(bike_trail)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)