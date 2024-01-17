import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

def open_browser():
    service = Service(executable_path="C:\\Git\\WebCrawling\\chromedriver.exe");
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver, login_id, login_psw):
    driver.get('') #여기에 해당 로그인 주소 써넣기
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'srchDvNm01').send_keys(str(login_id))
    driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(str(login_psw))
    driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
    driver.implicitly_wait(5)
    return driver

