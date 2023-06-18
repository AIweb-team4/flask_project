from flask import Flask
from view import Crwaling, index


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    app.register_blueprint(Crwaling.b_Cr)
    app.register_blueprint(index.bp)

    return app
# 구글 맵 키 = AIzaSyANuV_UHwrGrk4WStt1jJLTgWkg1DJ1ZSE
