from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time



base_url = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
plus_url = quote_plus(input('Please text what you want...'))

url = base_url + plus_url

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find(class_ = 'wrap_thumb')


print(img)
print(url)