import configparser
import os

def getBrowserName(name):
	cf = configparser.ConfigParser()
	cfpath = os.path.dirname(os.path.abspath('.')) + r'\config\config.ini'
	cf.read(cfpath)
	browsername = cf.get('Browser',name)
	return browsername
#print(browser)
#print(getBrowserName('Browser'))

if __name__ == '__main__':
	Redis_Password = getBrowserName('Redis_Password')
	print(Redis_Password == '')