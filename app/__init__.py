from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# Flask app setup
db = SQLAlchemy()
bcrypt = Bcrypt()

load_dotenv()  # This loads the environment variables from .env file

db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_name = os.getenv('DB_NAME', 'database')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'password')

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import account_bp
    app.register_blueprint(account_bp)
    # setup health check route
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify(success=True), 200
    @app.route('/', methods=['GET'])
    def index():
        return "hello world!", 200

    return app
