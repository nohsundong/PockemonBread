from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip

# 크롬 드라이버 위치 환경변수 추가 필요
driver = webdriver.Chrome()
print("LOG: Chrome 드라이버 로딩 성공")

url = 'https://naver.com'
driver.get(url)
# 창 최대화
driver.maximize_window()
    
time.sleep(1)

## 네이버 로그인 과정
driver.find_element_by_xpath("//a[@class='link_login']").click()
time.sleep(1)

tag_id = driver.find_element_by_name('id')
tag_id.clear()
tag_id.click()
############################## 아이디 입력
pyperclip.copy('여기에 아이디 입력 하세요')  ## ID입력
############################## 아이디 입력
tag_id.send_keys(Keys.CONTROL, 'v')

tag_pw = driver.find_element_by_name('pw')
tag_pw.clear()
tag_pw.click()

############################## 패스워드 입력
pyperclip.copy('여기에 패스워드 입력 하세요')  ## 패스워드 입력
############################## 패스워드 입력

tag_pw.send_keys(Keys.CONTROL, 'v')

driver.find_element_by_id('log.login').click()
print("LOG: 네이버 로그인 성공")

time.sleep(1)

# 포켓몬빵 구매 사이트 URL
ProuctsUrl = 'https://brand.naver.com/samlip/products/6510954368' 

driver.get(ProuctsUrl)
driver.maximize_window() 

while True:
    try:
        thumb = driver.find_elements(By.CLASS_NAME, 'OgETmrvExa')
        #구매하기
        thumb[0].click()
        print("LOG: 구매하기 클릭 성공")
        time.sleep(2)
        #일반결제클릭
        driver.find_element(By.CSS_SELECTOR, '#chargePointScrollArea > div.payment > ul.paymethod_list._paymentsArea > li.paymethod._payMethodTab._generalPaymentsTab > div.header > span.ajax_radio.radio-applied._payMethodRadio > span').click()
        print("LOG: 일반결제 클릭 성공")
        time.sleep(0)
        #나중에 결제클릭
        # deprecated in selenium
        driver.find_element(By.CSS_SELECTOR, '#chargePointScrollArea > div.payment > ul.paymethod_list._paymentsArea > li.paymethod._payMethodTab._generalPaymentsTab > ul > li.payment_item.tooltip_area > span.ajax_radio.radio-applied._payMeansClassRadio._payMeanSkip > span').click()
        print("LOG: 나중에 결제 클릭 성공")
        time.sleep(0)
        #주문하기
        driver.find_element(By.CSS_SELECTOR, '#orderForm > div > div.payment_agree_wrap > button').click()
        print("LOG: 주문 하기 클릭 성공")
        break
    except Exception:
        driver.refresh()
        print("LOG: 실패 새로고침")
        time.sleep(1)
driver.quit()