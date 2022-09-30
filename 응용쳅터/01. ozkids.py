import requests
import json
import openpyxl


wb = openpyxl.Workbook()

ws = wb.create_sheet('ozkids 크롤링')

ws['A1'] = 'product_price'
ws['B1'] = 'product_code'

row = 2
#  ozkiz1.com
#  discoveryglobal

for i in range(5010,5020) :
    print(f"{i}페이지 입니다.---------------------------")
    try:
        res = func1()
        
        try:
            requestdata = requests.get(f"https://medi.cafe24api.com/api/v2/products/{i}?shop_no=1&cafe24_app_key=KU5HdZg4BVXlfoLDEPu6EC&cafe24_api_version=2022-06-01")
        except:
            requestdata = requests.get(f"https://medi.cafe24api.com/api/v2/products/{i}?shop_no=1&cafe24_app_key=KU5HdZg4BVXlfoLDEPu6EC")
        # jsonData = None
        if requestdata.status_code == 200 :
            jsonData = requestdata.json()
            for data in jsonData :
                ws[f'A{row}'] = jsonData.get(data).get("price")
                ws[f'B{row}'] = jsonData.get(data).get("product_code")

                row = row + 1
                
                print(data, " : ", jsonData.get(data).get("price"), " : ", jsonData.get(data).get("product_code"))

    except:
        print("HTML루 파싱")



wb.save(r'D:\WebCrawling\파이썬엑셀다루기\참가자_data.xlsx')

# def func1() :
#     try:
#         requestdata = requests.get(f"https://medi.cafe24api.com/api/v2/products/{i}?shop_no=1&cafe24_app_key=KU5HdZg4BVXlfoLDEPu6EC&cafe24_api_version=2022-06-01")
#     except:
#         return func2()      

    


# def func2() :
#     try:
#         requestdata = requests.get(f"https://medi.cafe24api.com/api/v2/products/{i}?shop_no=1&cafe24_app_key=KU5HdZg4BVXlfoLDEPu6EC")

#     except:
#         return func3()

    


# def func3() :
#     html
