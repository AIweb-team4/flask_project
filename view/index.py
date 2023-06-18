from flask import request, Blueprint, render_template
from view.Crwaling import DrugstoreJson

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html');


@bp.route('/search')
def search():
    parameter_dict = request.args.to_dict()

    value1 = parameter_dict['B_area']
    value2 = parameter_dict['S_area']
    drugjson = DrugstoreJson(value1, value2)
    item = drugjson['response']['body']['items']['item']
    drugName = []
    druglong = []
    druglat = []
    drugSaStart = []
    drugSaEnd = []
    drugSuStart = []
    drugSuEnd = []
    for i in item:
        drugName.append(i['dutyName'])
        druglong.append(i['wgs84Lat'])
        druglat.append(i['wgs84Lon'])
        drugSaStart.append(i['dutyTime6s'])
        drugSaEnd.append(i['dutyTime6c'])
        drugSuStart.append(i['dutyTime7s'])
        drugSuEnd.append(i['dutyTime7c'])

    return render_template('index.html', name=drugName, long=druglong, lat=druglat, SaturS=drugSaStart,
                           SaturE=drugSaEnd, SunS=drugSuStart, SunE=drugSuEnd)


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/loginActon')
def loginAction():
    return render_template('login.html')
