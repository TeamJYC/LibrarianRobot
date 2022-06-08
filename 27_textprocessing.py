#-*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET
from collections import Counter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

global callnum_queue, isnbn_queue
callnum_queue, isbn_queue = [], []

def get_callnum(text):
    
    count = 0
    text = text.replace(" ", "")
    
    for idx, val in enumerate(text): # 리스트 요소 하나씩 접근
        if (ord(val) >= 48 and ord(val) <= 57):
            count += 1
        else:
            count = 0
            
        if count == 3:
            callnum_single = text[idx-2:idx+1]
            callnum_queue.append(callnum_single)
            getcallnum = True
            
            print(callnum_single)
            
            if len(callnum_queue) == 10:
                callnum_queue.pop(0)
                
            callnum_counter = Counter(callnum_queue)
            
            if int(callnum_counter.most_common(1)[0][1]) >= 3:
                callnum = callnum_counter.most_common(1)[0][0]
                return callnum
            break
        
            
def get_isbn(text):
    count = 0
    text = text.replace(" ", "")
    
    for idx, val in enumerate(text):
            
        if (ord(val) >= 48 and ord(val) <= 57):
            count += 1
        else:
            count = 0
        
        if count == 13:
            isbn_single = text[idx-12:idx+1]
            isbn_queue.append(isbn_single)
            
            print(isbn_single)
            
            if len(isbn_queue) == 10:
                isbn_queue.pop(0)
            
            isbn_counter = Counter(isbn_queue)
            
            if int(isbn_counter.most_common(1)[0][1]) >= 2:
                isbn = isbn_counter.most_common(1)[0][0]
                return isbn
            break
             
        
def callnum_to_kdc(callnum):
     kdc = callnum[0]
     return kdc

        
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

if __name__ == "__main__":
    for i in range(0,10):
        text = "aaa,9791162542743.86-x492"
        
        callnum = get_callnum(text)
        isbn = get_isbn(text)
        
        if callnum and not isbn :
            kdc = callnum_to_kdc(callnum)
        elif isbn:
            kdc = isbn_to_kdc(isbn)