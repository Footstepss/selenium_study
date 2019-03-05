from selenium import webdriver
#隐性加载时间
from selenium.webdriver.support.wait import WebDriverWait
from CapPic import CapPic#导入截图函数
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Log import LogGen
from basepage import BasePage
from BrowserStart import BrowserStart
logger = LogGen(logger="LoginPage").getLog()


class LoginPage(BasePage):
	def __init__(self,driver,url):
		self.driver = driver
		self.base_url = url

	def input_username(self,username,user_css):
		self.send_Val(5,EC.element_to_be_clickable((By.CSS_SELECTOR,user_css)),username)
		logger.info('输入账号: %s.' % username)

	def input_pwd(self,password,pwd_css):
		self.send_Val(5,EC.element_to_be_clickable((By.CSS_SELECTOR,pwd_css)),password)
		logger.info('输入密码: %s.' % password)

	def click_login(self,login_css):
		self.click_submit(5,EC.element_to_be_clickable((By.CSS_SELECTOR,login_css)))
		#logger.info('点击登陆')

