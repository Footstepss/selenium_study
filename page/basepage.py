from selenium import webdriver
#隐性加载时间
from selenium.webdriver.support.wait import WebDriverWait
from CapPic import CapPic#导入截图函数
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Log import LogGen
from BrowserStart import BrowserStart
logger = LogGen(logger="BasePage").getLog()

class BasePage(object):
	def __init__(self,driver,url):
		self.driver = driver
		self.base_url = url
		#self.logger = LogGen(logger="BasePage").getLog()

	def wait_element_time(self,time=None):
		#return WebDriverWait(driver,time).until(func)
		return WebDriverWait(self.driver,time)

	def find_element(self,time,func):
		try:
			return self.wait_element_time(time).until(func)
			#return self.driver.find_element(*loc)
		except Exception as e:
			#找不到元素调用截图
			CapPic(self.driver)
			#传入日志
			logger.info(e)

	def click_submit(self,time,func):
		#self.wait_element_time(time).until(func).click()
		
		try:
			self.wait_element_time(time).until(func).click()
		except Exception as e:
			CapPic(self.driver)
			logger.info(e)
		

	def send_Val(self,time,func,content):

		try:
			self.wait_element_time(time).until(func).send_keys(content)
		except Exception as e:
			CapPic(self.driver)
			logger.info(e)


if __name__ == '__main__':
	pre = BrowserStart()
	bp = BasePage(pre[0],pre[1])
	bp.click_submit(5,EC.element_to_be_clickable((By.CSS_SELECTOR,'#ttbar-login > a.link-logi')))