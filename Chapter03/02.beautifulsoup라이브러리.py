import requests

from bs4 import BeautifulSoup

#naver 서버에게 대화를 시도(get 방식)
response = requests.get("https://www.naver.com") 

#naver에서 html을 줌
html = response.text

#BeautifulSoup로 html을 파싱
soup = BeautifulSoup(html, 'html.parser')

#id값이 NM_set_home_btn인 것 한개를 word에 넣는다.
word = soup.select_one('#NM_set_home_btn')

#위에서 고른 word를 출력(원하는 텍스트 요소 출력)
print(word)