from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Import our app blueprints and config

from config import Config 


# Initialize extensions required for app
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
     
    # Load config
    # app.config.from_object('app.config.Config')
    app.config.from_object(Config)
     
    # Initialize app with extensions
    db.init_app(app)
    bcrypt.init_app(app)

    #register blueprints   
    from app.routes import main
    app.register_blueprint(main)
     




     
    #Global error handling
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app