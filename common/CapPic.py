import time
import os

"""
	屏幕截图
"""

def CapPic(driver):
#获取当前时间
	pt = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
#print(pt)
#前半段为获取上一层目录的绝对路径 + 
	picname = os.path.dirname(os.path.abspath('.')) +'\\picture\\'+pt+ '.png'
	driver.get_screenshot_as_file(picname)