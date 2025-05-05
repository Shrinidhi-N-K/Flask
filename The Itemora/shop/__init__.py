from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv


# Load environment variables from .env file

load_dotenv()

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Set configuration from .env file
    app.config['SECRET_KEY'] = os.getenv("SECRET")

    # Get the base directory and use it to construct the absolute path for the SQLite DB
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Set up strong protection login view and message category
    login_manager.session_protection = 'strong' 
    login_manager.login_view = 'main.login_page'
    login_manager.login_message_category = 'info'

    # Import models after initializing db
    from shop.models import Item

    # Create the tables if they do not exist
    with app.app_context():
        db.create_all()

    # Register the routes
    from shop.routes import main
    app.register_blueprint(main)

    return app
