import imp
from itertools import count
from random import random
from urllib.request import urlopen, urlretrieve
import urllib
from urllib.parse import quote_plus, quote
from bs4 import BeautifulSoup
from selenium import webdriver # 페이징 없이 자바스크립트로 페이지 불러오며 스크롤 내리면 로딩되며 보여지는 페이지 크롤링 적합
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  #파인드 엘리먼트 활성화 위해
import time
import random
import pyperclip
import csv

# id 입력
# tag_id.click()
# pyperclip.copy('아이디')
# tag_id.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)

# options = webdriver.ChromeOptions()
# options.add_argument('lang=ko_KR')    # 언어 설정

plusurl = input('검색어를 입력해 주세요. : ')
# pyperclip.copy(plusurl)
# new_text = pyperclip.paste()
# new_text = plusurl
# url = baseurl + quote_plus(plusurl)

# new_text = search_text()

print('start searching...')
baseurl = 'https://www.instagram.com/'
driver = webdriver.Chrome(executable_path='chromedriver') #html 소스가 아닌 자바에서 html 구하기 위한 과정
driver.implicitly_wait(15)
driver.get(baseurl)
driver.implicitly_wait(15)
# #로그인
id = 'thelambs1979@gmail.com'
pw = '#Autumn21'
login_id = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
login_id.send_keys(id)  
login_pw = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
login_pw.send_keys(pw)
login_pw.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
driver.implicitly_wait(10)

try:
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
except:
    driver.refresh()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    driver.implicitly_wait(5)
key_text ='고아라'   
search_text = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_text.send_keys(key_text)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
time.sleep(random.uniform(6,8)) 

##페이지 계속 내리기##
SCROLL_PAUSE_TIME = 1 #스크롤 후 대기 타임
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        #try: #driver.find_element_by_xpath('더보기 버튼 찾아서 클릭소스').click() except: break
        break 
    last_height = new_height
##페이지 계속 내리기##   

insta = driver.find_elements_by_css_selector('.v1Nh3.kIKUG')
""" reple = driver.find_element_by_css_selector('.C4VMK')
print(reple)
time.sleep(5) """
# html = driver.page_source #페이지 소스를 html에 넣는다 그래야 뷰티풀숩에서 추출 시작 //
# soup = BeautifulSoup(html,'html.parser')
#insta = soup.select('.FFVAD')
# for title in titles:
#     print(title.text, title.get_attribute('href'))
driver.implicitly_wait(10)
count = 1
total_list = []

for imgUrl in insta[:3]:
    
    try:
        img_get = imgUrl.find_element_by_tag_name('img').get_attribute('src')
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(img_get, "img/" + str(count) + ".jpg")
        imgUrl.find_element_by_tag_name('a').click()
        time.sleep(2)
        
        try:
            reple = driver.find_elements_by_css_selector('.C4VMK')
            tags = driver.find_elements_by_css_selector('.xil3i')
            tag_list = []
            for tag in tags:
                tag_text = tag.text
                tag_list.append(tag_text)
            text_list =[]
            for re_text in reple:
                text = re_text.find_elements_by_tag_name('span')[-1].text
                text_list.append(text)
        except:
            print('nothing')
        
        print(count)
        count = count + 1
        img_list = []
        img_list.append(img_get)
        total_list.append(tag_list)
        total_list.append(text_list)
        total_list.append(img_list)
        
        
        time.sleep(5)
        driver.find_element_by_css_selector('.NOTWr').click()
        print("창닫기 성공")
    except:
        pass
print(total_list)
print("모두 다운로드 하였습니다.")
file = open(f'{key_text}.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(file)
writer.writerow(['태그', '답글', '링크'])
for i in total_list:
    writer.writerow(i)

file.close()
print("모두 액셀파일로 저장 하였습니다.")

driver.close #가상 크롬 브라우저를 항상 닫아준다




