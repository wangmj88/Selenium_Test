import os.path
from .basepage import BasePage
from selenium.webdriver.common.by import By
from common.loggen import Logger
from selenium import  webdriver
logger = Logger(logger="MainPage").getlog()
#定义主页面中所涉及到的元素，userid及退出按钮，通过xpath方式识别
class MainPage(BasePage):
        userid_loc = (By.XPATH, './/*[@id=\'ECS_MEMBERZONE\']/font/font')
        exit_btn_loc=(By.XPATH, './/*[@id=\'ECS_MEMBERZONE\']/font/a[2]')
        # 定义打开超链接方法，并将此操作写入日志
        def open(self,base_url):
            self._open(self.base_url, self.pagetitle)
            logger.info("打开链接: %s." % base_url)
        #定义显示userid信息，并将此操作写入日志
        def show_userid(self):
                userid = self.find_element(*self.userid_loc).text
                logger.info("当前用户id是:%s." % userid)
                return userid
        #定义退出操作，点击退出按钮，并写入日志
        def exit_sys(self):
            self.find_element(*self.exit_btn_loc).click()
            logger.info("退出测试系统")