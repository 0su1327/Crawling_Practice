import requests

from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C")

html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") #결과는 리스트 형식으로
for link in links:
    title = link.text #태그 안에 텍스트요소를 가져온다.
    url = link.attrs['href'] # href의 속성값을 가져온다
    print(title, url)
