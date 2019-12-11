from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://my_db.sqlite'

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return render_template('base.html', title='hello')

    return app
