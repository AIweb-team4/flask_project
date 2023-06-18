import json

import requests
import xmltodict as xmltodict
from bs4 import BeautifulSoup
from flask import Blueprint

b_Cr = Blueprint('crwaling', __name__, url_prefix='/cr')

api = 'https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=s%2B1EAl1Ky%2B8jsaOUZdvQMc7AwLUjHF2bYY4evN1MohRWAm48srSsvGlvxAjTGiKAevbHdccXmCFRYFzRbxO3cw%3D%3D'

def DrugstoreJson(area1, area2):
    params = {'Q0': area1, 'Q1': area2 , 'QT':7}
    # Q1 : 지역 #QT : 날짜

    response = requests.get(api, params=params)

    xmlToJsonConverter = xmltodict.parse(response.text)

    resultList = json.loads(json.dumps(xmlToJsonConverter))
    return resultList


@b_Cr.route('/')
def Crwal():
    return 0
