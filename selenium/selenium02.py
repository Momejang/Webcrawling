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

reviewData = []

try :
    print('selenium version :: ',selenium.__version__)
    driver.get(url)
    #time.sleep(3)
    
    driver.find_element(By.XPATH,'//*[@id="reviewInfo"]/a').click() # 댓글 클릭

    # 10 페이지만 리뷰를 저장하자
    for reviewPageNum in range(1,8) :
        time.sleep(2)
        reviewElement = driver.find_element(By.CLASS_NAME,'review_list_wrap') # 리뷰 DIV
        time.sleep(2)
        reviewLilist = reviewElement.find_elements(By.CSS_SELECTOR, '.inner_list>li') # 리뷰 li list elements
        
        # sample = {'seq':0, 'id':'', 'content':'', 'date':''}

        for index, item in enumerate(reviewLilist) :
            id = item.find_element(By.CSS_SELECTOR, '.id').text
            content = item.find_element(By.CSS_SELECTOR, '.txt_inner').text
            date = item.find_element(By.CSS_SELECTOR, '.date').text
            
            item.get_attribute('class')

            reviewNum = str(reviewPageNum-1) +'.'+ str(index+1) # 순번작성

            tempData = {'seq':reviewNum, 'id':id, 'content':'a', 'date':date}
            reviewData.append(tempData)
    
        print('======== '+str(reviewPageNum)+' ============')
        anchor = driver.find_element(By.CSS_SELECTOR, '.pageing>a')
        nextPage = reviewPageNum + 1
        time.sleep(2)
        driver.execute_script("arguments[0].setAttribute('data-page-no',arguments[1])",anchor, nextPage) # 다음페이지 설정
        time.sleep(1)
        anchor.click() # 다음 리뷰페이지로 이동
        time.sleep(2)

except Exception as e:
    print('예외가 발생했습니다.', e)

#time.sleep(3)
driver.quit() # 종료

print('-------------------------------------')
print('-------------------------------------')
print(*reviewData, sep = "\n")
print('-------------------------------------')
print('-------------------------------------')
