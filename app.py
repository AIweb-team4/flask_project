from flask import Flask
from flask_migrate import Migrate

from view import Crwaling, index, model
def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    DBURI = f"postgresql://postgres:1234@localhost:5432/users"

    app.config['SQLALCHEMY_DATABASE_URI'] = DBURI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(Crwaling.b_Cr)
    app.register_blueprint(index.bp)

    model.db.init_app(app)
    migrate = Migrate(app, model.db)
    return app
# 구글 맵 키 = AIzaSyANuV_UHwrGrk4WStt1jJLTgWkg1DJ1ZSE
