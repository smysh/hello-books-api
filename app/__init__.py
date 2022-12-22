from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# SQLALCHEMY extension class
db = SQLAlchemy()
# Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
migrate = Migrate()

def create_app(test_config=None):
    # create FLask application object
    # It is passed the name of the module or package of the application.
    # If you are using a single module, __name__ is always the correct value. 
    # If you however are using a package, it’s usually recommended to hardcode the name of your package there.
    app = Flask(__name__)
    # SQLALCHEMY_TRACK_MODIFICATIONS if enabled, records all insert, update, and delete operations on models 
    # then sends in models_committed and before_models_committed signals when session.commit() is called.
    # This adds a significant amount of overhead to every session. Changed in version 3.0: Disabled by default.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # connection URL format: dialect://username:password@host:port/database
    # included dialects : PostgreSQL, MySQL, MariaDB, SQLite, Oracle, Microsoft SQL Server
    # PostgreSQL dialect uses psycopg2 as the default DBAPI. Other PostgreSQL DBAPIs include pg8000 and asyncpg
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    # initialize the app with extension
    # sets default configuration values, configures the extension on the application and creates the engines for each bind key. 
    # Therefore, this must be called after the application has been configured. 
    # Changes to application config after this call will not be reflected.
    db.init_app(app)
    # initializes the migrate extension with the spplication instance and the Flask-SQLAlchemy database instance
    migrate.init_app(app,db)

    # Register a Blueprint on the application. 
    # Calls the blueprint’s register() method after recording the blueprint in the application’s blueprints.
    # Parameters :
    # blueprint – The blueprint to register.
    # url_prefix – Blueprint routes will be prefixed with this.
    # subdomain – Blueprint routes will match on this subdomain.
    # url_defaults – Blueprint routes will use these default values for view arguments.
    from app.models.book import Book
    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app