from selenium import  webdriver
#加载元素显示超时设置函数
from selenium.webdriver.support.wait import WebDriverWait
#导入截图函数
from common.cappic import Cappic
#加载预期处理函数
from selenium.webdriver.support import expected_conditions as EC
import time
import os.path
#导入日志处理函数
from common.loggen import Logger
logger = Logger(logger="BasePage").getlog()
#定义基础页面类文件，该类仅包含查找元素及输入数据两个子函数
class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url
    #定义查找元素超时设置，当页面中某个元素在10秒内没有显示，则抛出异常，并在日志中记录
    def find_element(self, *loc):
        try:
           # loc是表示属性元组本身，*loc表述属性元组的值,EC.visibility_of_element_located需要传入2个参数，但*loc是三个参数
           # 因此，此处只能loc
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
           # 此处返回元素的属性及属性值，故使用*loc
            return self.driver.find_element(*loc)
        except:
            #当元素找不到的时候调用截图函数
            Cappic(self.driver)
            #元素找不到时在日志中记录信息
            logger.info(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def send_keys(self, loc, vaule,):
        try:
            #获取元素的属性值，以便于识别元素
            loc = getattr(self, "_%s" % loc)
            #查找元素并输入相关数据
            self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            #当元素找不到的时候调用截图函数
            Cappic(self.driver)
            #元素找不到时在日志中记录信息
            logger.info(u"%s 页面中未能找到 %s 元素" % (self, loc))