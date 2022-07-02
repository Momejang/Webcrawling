from importlib.resources import contents
import time
# 크롬 브라우저 조작을 위한 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium

chomeDriverPath = "C:\Python\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chomeDriverPath, options=options)

#url = "https://www.naver.com"
url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000166590&dispCatNo=90000010008&trackingCd=New"

try :
    print('selenium version :: ',selenium.__version__)
    driver.get(url)
    #time.sleep(3)

    #driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[5]/a').click()
    #driver.find_element(By.CSS_SELECTOR,'a.nav.shop').click()
    #driver.execute_script("arguments[0].click();", element)
    #print(sampleText)

    #driver.find_element(By.ID,"query").send_keys("한글사전")
    #driver.find_element(By.ID,"search_btn").click()
    
    driver.find_element(By.XPATH,'//*[@id="reviewInfo"]/a').click() # 댓글 클릭
    #reviewElement = driver.find_element(By.ID,'gdasList') # 댓글 list elements
    reviewElement = driver.find_element(By.CLASS_NAME,'review_list_wrap')

    time.sleep(2)

    reviewLilist = reviewElement.find_elements(By.CSS_SELECTOR, '.inner_list>li') # 댓글 li list elements

    reviewData = []
    # sample = {'seq':0, 'id':'', 'content':'', 'date':''}
    # reviewData = append(sample)

    for index, item in enumerate(reviewLilist) :
        id = item.find_element(By.CSS_SELECTOR, '.id')
        # content = item.find_element(By.CSS_SELECTOR, '.txt_inner').text
        # date = item.find_element(By.CSS_SELECTOR, '.date').text
        
        # tempData = {'seq':index, 'id':id, 'content':'a', 'date':date}
        # reviewData.append(tempData)

        print(id.text)
        print(id.get_attribute('data-attr'))
        
        # driver.execute_script
        driver.execute_script("arguments[0].setAttribute('data-attr',arguments[1])",id, 'abcddddd')

    
except Exception as e:
    print('예외가 발생했습니다.', e)

#time.sleep(3)
# driver.quit() # 종료

print('-------------------------------------')
print('-------------------------------------')
print(reviewData)
print('-------------------------------------')
print('-------------------------------------')
