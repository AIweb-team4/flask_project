import requests
from bs4 import BeautifulSoup
from flask import Blueprint

b_Cr = Blueprint('crwaling', __name__, url_prefix='/cr')

url = "https://www.dongyang.ac.kr/dongyang/71/subview.do"
api = 'https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=s%2B1EAl1Ky%2B8jsaOUZdvQMc7AwLUjHF2bYY4evN1MohRWAm48srSsvGlvxAjTGiKAevbHdccXmCFRYFzRbxO3cw%3D%3D'

params ={'serviceKey' : '서비스키', 'Q0' : '서울특별시', 'Q1' : '강남구', 'QT' : '1', 'QN' : '삼성약국', 'ORD' : 'NAME', 'pageNo' : '1', 'numOfRows' : '10' }

response1 = requests.get(api, params=params)

response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

scheList = []
e = soup.select('.scheList')
for i in e:
    e2 = i.select('li')
    for j in e2:
        dt = j.select_one('dt>span').get_text().replace(" ", "")
        text = j.select_one('dd>span').get_text().replace(" ", "")

        scheList.append(dt.replace("\n", "") + ', ' + text.replace("\n", ""))


@b_Cr.route('/')
def Crwal():
    return scheList


@b_Cr.route('/data')
def test():
    return response1.content
