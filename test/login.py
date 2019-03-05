from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pyquery import PyQuery as pq
import re
import time
import unittest


url = 'https://www.jd.com'

def wait_element_time(driver,time,func):
	return WebDriverWait(driver,time).until(func)

def openBrower():
	"""
	return web handle
	"""
	return webdriver.Chrome()

def openUrl(driver,url):
	driver.get(url)
	driver.maximize_window()

def findElement(driver,login_css):
	if 'loginlink' in login_css:
		print('1111')
		submit = wait_element_time(driver,10,EC.element_to_be_clickable((By.CSS_SELECTOR,login_css['loginlink'])))
		print('22222')
		submit.click()

	driver.find_element_by_link_text('账户登录').click()

	user_input = driver.find_element_by_css_selector(login_css['user_css'])
	#user_input.send_keys('18634868274')
	password_input = driver.find_element_by_css_selector(login_css['password_css'])
	#password_input.send_keys('z461458149')
	submit = driver.find_element_by_css_selector(login_css['login_css'])
	print('333333')
	#submit.click()
	return user_input,password_input,submit

def sendVal(elementuple,loginlist):
	i = 0
	for input in elementuple:
		if i != 2:
			input.send_keys(loginlist[i])
			i += 1
		else:
			input.click()

	#print('请开始拖动滑块')
	#time.sleep(10)

def checkResult(driver):
	pass

def main():
	login_css = {
		'loginlink':'#ttbar-login > a.link-login',
		'user_css' :'#loginname',
		'password_css':'#nloginpwd',
		'login_css':'#loginsubmit'
	}

	loginlist = ['18634868274','z461458149']

	driver = openBrower()
	openUrl(driver,url)
	elementuple = findElement(driver,login_css)

	sendVal(elementuple,loginlist)
	time.sleep(3)
	print('close browser')
	time.sleep(3)
	#driver.close()

	
if __name__ == '__main__':
	main()