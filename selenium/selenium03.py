from selenium.webdriver.common.by import By
import common.browserDriver as Dr
import selenium
import time

driver = Dr.chromeDriverLoad()  # 셀레니움 크롬 드라이버 생성

#url = "https://www.naver.com"
url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000166590&dispCatNo=90000010008&trackingCd=New"

reviewData = []

try:
    print('selenium version :: ', selenium.__version__)
    driver.get(url)
    # time.sleep(3)

    driver.find_element(By.ID, 'btnGnbOpen').click()
    time.sleep(2)
    a = driver.find_elements(By.CSS_SELECTOR, 'ul.all_menu_wrap>li div li a')
    print(len(a))

    for index, x in enumerate(a):
        items = driver.find_elements(
            By.CSS_SELECTOR, 'ul.all_menu_wrap>li div li a')
        # print(item)

        # driver.execute_script(
        #     "arguments[0].click();", category_lists[category])

        driver.execute_script("arguments[0].click();", items[index])
        time.sleep(10)

except Exception as e:
    print('예외가 발생했습니다.', e)

time.sleep(10)
driver.quit()  # 종료

print('-------------------------------------')
print('-------------------------------------')
print(*reviewData, sep="\n")
print('-------------------------------------')
print('-------------------------------------')
