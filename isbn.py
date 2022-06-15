# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET

def isbn_to_kdc(isbn):
    host = 'https://www.nl.go.kr/NL'
    path = '/search/openApi/search.do?'
    key = 'a3678243a7ca64ca37c6ff5edb7cf7f3ef12f378fbad97de528d0f32769798a1'
    params = {'key' : key, 'detailSearch' : 'true', 'isbnOp' : 'isbn', 'isbnCode' : isbn}
    url = host + path

    result = requests.get(url,params=params)
    xmlstr = result.text
    root = ET.fromstring(xmlstr)
    kdc = root.find('result').find('item').find('kdc_code_1s').text
    return kdc
