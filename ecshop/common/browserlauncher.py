import configparser
import os.path
from selenium import webdriver
from common.loggen import Logger
logger = Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver_path=dir + '/tools/geckodriver.exe'
    def __init__(self, driver):
        self.driver = driver
    # 从config.ini文件中读取driver类型
    def get_browser(self, driver):
        if self.browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif self.browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif self.browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

       # driver.implicitly_wait(10)
       # logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
