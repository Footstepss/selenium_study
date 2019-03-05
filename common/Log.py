import logging
import os
import time
from ReadConfig import getBrowserName


class LogGen(object):
	def __init__(self,logger):
		#new一个日志实例 参数为日志名字
		self.logger = logging.getLogger(logger)
		#设定日志级别
		self.logger.setLevel(logging.INFO)
		path = getBrowserName('Path')
		#print(path)
		#设置文件路径
		lt = time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.log'
		file = logging.FileHandler(path+'\\LogFile\\' + lt,encoding='utf-8')
		file.setLevel(logging.INFO)
		
		#打印到控制台
		console = logging.StreamHandler()
		console.setLevel(logging.INFO)
		
		#日志输出格式
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		file.setFormatter(formatter)
		#选择写入日志的文件
		self.logger.addHandler(file)
		#加入控制台
		self.logger.addHandler(console)
		#写入数据
		#logger.info('hello world')

	def getLog(self):
		return self.logger