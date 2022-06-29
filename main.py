# main.py
import requests
from bs4 import BeautifulSoup as Bs
print('hello world')

url = 'https://finance.naver.com/item/main.nhn?code=005930'
url2 = 'https://www.daum.net'
web = requests.get(url)
soup = Bs(web.content, 'html.parser')
pf = soup.select_one('#_nowVal')

#print(soup.script)
print(pf)
print('@@@')


