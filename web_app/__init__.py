# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.bike_trail import bike_trail

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(bike_trail)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)