import urllib.request
import urllib.parse #1 한글을 아스키문자로 변환 모듈
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query="
plus_url = urllib.parse.quote_plus(input('검색어를 입력하세요.')) #1 한글 아스키 문자로 변환
url = base_url + plus_url

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='total_tit') #일단 find_all로 모두 찾아서 리스트화 시키고 그것을 for로 돌리면 .text나 attrs사용 가능

for i in title:
    print(i.text)
    print(i.attrs['href'])
    print()

