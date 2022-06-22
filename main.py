# main.py
import requests
from bs4 import BeautifulSoup as Bs
print('hello world')

web = requests.get('https://www.daum.net')
soup = Bs(web.content, 'html.parser')

print(soup.script)


