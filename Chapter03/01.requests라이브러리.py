import requests  #우리의 source 코드로 library 가져옴

response = requests.get("https://www.naver.com") #requests의 get요청을 보낸다.
html = response.text #html에 우측의 값을 넣어준다.
print(html)