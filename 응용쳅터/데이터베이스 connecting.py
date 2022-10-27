from logging import exception
import string
import requests
import json
import pymysql
from bs4 import BeautifulSoup as bs
import pyautogui
from email import header
from http.client import ImproperConnectionState
import urllib.request
from urllib.error import URLError, HTTPError





# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', user='root', password='fouridiot1234',
                       db='Capstone', charset='utf8') # 한글처리 (charset = 'utf8')

# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

# func1이 실행되면 cafe의 json을 가진 사이트를 파싱
def func1(list, k, app_key) : 
    try:
        requestdata = requests.get(f"https://{list}.cafe24api.com/api/v2/products/{k}?cafe24_app_key={app_key}")
        print(requestdata.status_code)

        return requestdata
    except:
        return func2()
   
# 모든 function이 실행되지 않으면 어쩔 수 없이 html 전체를 파싱해서 값을 가져오기(ex 메디큐브)
def func2() :
    # page = requests.get("https://www.carrieandshop.co.kr/goods/goods_view.php?goodsNo=1779")
    # soup = bs(page.text, "html.parser", encoding='UTF-8')
    print("return.")
    # return soup
    try:
        header = {'User-Agent' : 'Chrome/66.0.3359.181'}
        request = urllib.request.Request("https://themedicube.co.kr/product/detail.html?product_no=1103&cate_no=466&display_group=2", headers=header)
        print(request)
        html = urllib.request.urlopen(request)
        source = html.read()
        soup = bs(source, 'html.parser')
    except HTTPError as e:
        err = e.read()
        code = e.getcode()

    a = soup('a')
    return html

# python은 인터프리터 언어이기 때문에 순서를 잘 생각해야 한다.

arr = [['ozkiz1', 'KU5HdZg4BVXlfoLDEPu6EC'],['nsmall2022','KU5HdZg4BVXlfoLDEPu6EC']]  #DB에서 불러와야함 (DICTIONARY 형태로)

#platform이름하고 api-key값만 받아서 변수로 저장해서 
key = pyautogui.prompt("key 값을 입력해주세요..")
platform = pyautogui.prompt("json header를 입력해주세요..")


for k in range(3950, 4000) :
    # list = arr[i][0]
    # app_key=arr[i][1]
    requestdata = func1(platform, k, key)
    
    if requestdata.status == 200 :
        jsonData = requestdata.json()
        for data in jsonData :
            # price와 같은 
            if jsonData.get(data).get("price") != None :
                # print(f"{k}페이지 입니다.----------------------------------------------")
                #일단 5가지만 mysql에 저장해보기
                
                price :int = jsonData.get(data).get("price")
                code :int = jsonData.get(data).get("product_code")
                tax_free_price :int = jsonData.get(data).get("price_excluding_tax")
                name :string = jsonData.get(data).get("product_name")
                platform_name :string = platform

                str = f"INSERT IGNORE INTO platform_item VALUES('{name}', '{code}' ,'{price}','{tax_free_price}','{platform_name}')"

                cur.execute(str)
            
                con.commit()
                

                print(data, " : ", price, ", product_code", " : ", code)
            
            else :
                continue
    else:      
        func2()
con.close()