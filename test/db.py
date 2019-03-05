import redis
#from proxypool.error import PoolEmptyError
from setting import *

class RedisClient(object):
	def __init__(self,host = HOST,port = PORT,db=db):
		if PASSWORD:
			self._db = redis.Redis(host=host, port=port, password=PASSWORD,db=db)
		else:
			self._db = redis.Redis(host=host, port=port,db=db)

	def s_set(self,key,data):
		return self._db.set(key,data)

	def s_get(self,key):
		return self._db.get(key)

if __name__ == '__main__':
	r = RedisClient(db = 2)
	r.s_set('name','test')
	print(r.s_get('name'))