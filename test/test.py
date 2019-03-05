from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pyquery import PyQuery as pq
import re
import time

"""
def wait_element_time(driver,time,func):
	return WebDriverWait(driver,time).until(func)


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

input = wait_element_time(driver,1,EC.element_to_be_clickable((By.CSS_SELECTOR,'#kw')))
input.send_keys('约定的梦幻岛')
"""

login_config = {
		'loginlink':'#ttbar-login > a.link-login',
		'user_css' :'#loginname',
		'password_css':'#nloginpwd',
		'login_css':'#loginsubmit'
}

print(login_config['loginlink'])

def test():
	return 1,2,3

a = test()
print(a)