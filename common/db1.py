import redis
#from proxypool.error import PoolEmptyError
from common.ReadConfig import getBrowserName
import mysql.connector
from Log import LogGen
logger = LogGen(logger = 'DataBase').getLog()

class MysqlClient(object):
	def __init__(self,host,user,passwd,database):
		try:
			self.mydb = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database,auth_plugin='mysql_native_password')
			self.mycursor = self.mydb.cursor()
		except Exception as e:
			logger.info(e)

	def search(self,sql):
		#返回的数据 一行数据以列表，每个字段作为元祖d
		try:
			self.mycursor.execute(sql)
			return self.mycursor.fetchall()
		except Exception as e:
			logger.info(e)

class RedisClient(object):
	def __init__(self,host,port,db,password):
		try:
			if password:
				self._db = redis.Redis(host=host, port=port, password=password,db=db)
			else:
				self._db = redis.Redis(host=host, port=port,db=db)
		except Exception as e:
			logger.info(e)

	def s_set(self,key,data):
		#字符串增加或修改
		try:
			return self._db.set(key,data)
		except Exception as e:
			logger.info(e)

	def s_get(self,key):
		#查询字符串
		try:
			return self._db.get(key)
		except Exception as e:
			logger.info(e)
