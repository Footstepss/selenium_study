from common.ReadConfig import getBrowserName
from selenium import webdriver
import os
from common.CapPic import CapPic
from common.Log import LogGen

def BrowserStart():
	logger = LogGen(logger = '浏览器启动加载').getLog()
	browsername = getBrowserName('Browser')
	url = getBrowserName('Url')
	driver = None
	if browsername == 'Chrome':
		logger.info('启动Chrome浏览器')
		driver = webdriver.Chrome()
		logger.info('打开页面')
		driver.get(url)
		driver.maximize_window()
	
	if browsername == 'Ie':
		driver = webdriver.Ie()
		driver.get(url)
	
	if browsername == 'Firefox':
		driver = webdriver.Firefox()
		driver.get(url)

	#还需要一个无头浏览器
	#if browsername == ''
	#CapPic(driver)	
	return driver,url