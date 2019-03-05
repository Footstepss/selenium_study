import unittest
from Log import LogGen
from selenium import webdriver
#隐性加载时间
from selenium.webdriver.support.wait import WebDriverWait
from CapPic import CapPic#导入截图函数
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BrowserStart import BrowserStart
from ReadConfig import getBrowserName
from loginpage import LoginPage
from Log import LogGen
from db1 import MysqlClient,RedisClient

logger = LogGen(logger="LoginPage").getLog()

class logintest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		#cls.mysql_host = getBrowserName(Mysql_Host)
		#cls.redis_host = getBrowserName(Redis_Host)
		#cls.url = getBrowserName(Url)
		pass

	def setUp(self):
		pre = BrowserStart()
		#self.driver = pre[0]
		#self.url = pre[1]
		self.loginpage = LoginPage(pre[0],pre[1])


	def test_login_1(self):	
		'''
		DataSet1:数据类型为元祖 该测试用例 css选择器 xpath url等数据
		DataSet2:数据类型为元祖 对界面需要进行输入的数据
		'''	
		#ttbar-login > a.link-login
		DataSet1 = ['#ttbar-login > a.link-login','#content > div > div.w > div > div.login-tab.login-tab-r > a','#loginname','#nloginpwd','#loginsubmit']
		DataSet2 = ['京东账号','京东密码']

		self.loginpage.click_login(DataSet1[0])
		logger.info('点击进入登陆页面')
		self.loginpage.click_login(DataSet1[1])
		logger.info('点击账户登陆')
		self.loginpage.input_username(DataSet2[0],DataSet1[2])
		#logger.info('输入账号')
		self.loginpage.input_pwd(DataSet2[1],DataSet1[3])
		#logger.info('输入密码')
		self.loginpage.click_login(DataSet1[4])
		logger.info('进行登陆')

if __name__ == '__main__':
	unittest.main()