#encoding:gbk
import win32com
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import sys


def login_qq():
    try:
        driver = webdriver.Chrome()
        print('浏览器已打开')
        driver.get('https://ke.qq.com/')
        driver.maximize_window()
        print('网页已打开')
        driver.find_element_by_id('js_login').click()
        time.sleep(2)
        print('登陆成功，马上进行跳转')
        driver.find_element_by_class_name('ptlogin-wrap').click()
        time.sleep(1)
        driver.find_element_by_css_selector('a[report-tdw="module=index_web_center&action=clickCourse"]').click()
        time.sleep(1)
    except NoSuchElementException:
        print('未知错误无法打开！！！')


if __name__ == '__main__':
    login_qq()
    print('程序运行结束，请关闭此窗口')