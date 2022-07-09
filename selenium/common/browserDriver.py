# 크롬 브라우저 조작을 위한 모듈
from selenium import webdriver

chomeDriverPath = 'C:\Python\chromedriver\chromedriver.exe'
safariDriverPath = ''


def chromeDriverLoad():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(chomeDriverPath, options=options)
    return driver


def safariDriverLoad():
    print('개발중')
