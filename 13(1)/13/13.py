#encoding:gbk
from selenium import webdriver
import time
def login():
    environment=input("�������Ӧ������1.���� 2.��ʽ")
    time.sleep(1)

    if environment ==str():
        driver = webdriver.Chrome()
        driver.get('http://manager-test.ggn.cn/')

    else:
        driver = webdriver.Chrome()
        driver.get('http://manager.ggn.top/')

    time.sleep(5)
    driver.maximize_window()
    account = input("�������˺ţ�")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/form/div[1]/input").send_keys(account)

    time.sleep(5)
    password = input("���������룺")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/form/div[2]/input").send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/form/button").click()
    time.sleep(60)
    return driver

login()



