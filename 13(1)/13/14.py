#encoding:gbk
import win32com
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import sys


def login_qq():
    try:
        driver = webdriver.Chrome()
        print('������Ѵ�')
        driver.get('https://ke.qq.com/')
        driver.maximize_window()
        print('��ҳ�Ѵ�')
        driver.find_element_by_id('js_login').click()
        time.sleep(2)
        print('��½�ɹ������Ͻ�����ת')
        driver.find_element_by_class_name('ptlogin-wrap').click()
        time.sleep(1)
        driver.find_element_by_css_selector('a[report-tdw="module=index_web_center&action=clickCourse"]').click()
        time.sleep(1)
    except NoSuchElementException:
        print('δ֪�����޷��򿪣�����')


if __name__ == '__main__':
    login_qq()
    print('�������н�������رմ˴���')