from selenium import webdriver
from .basepage import BasePage
from selenium.webdriver.common.by import By
from common.loggen import Logger
from common.geturl import geturl
logger = Logger(logger="UserRegiste").getlog()
#定义注册页面中元素的识别及操作方式，通过id及xpath识别元素
class RegistePage(BasePage):
    username = (By.ID, 'username')
    email = (By.ID, 'email')
    password=(By.ID,'password1')
    confirmpw=(By.ID,'conform_password')
    submit = (By.XPATH, 'html/body/div[6]/div/form/table/tbody/tr[7]/td[2]/input[3]')
    #定义用户名输入操作函数，并写入日志
    def input_username(self, username):
          self.find_element(*self.username).send_keys(username)
          logger.info("输入用户名:%s." % username)
    #定义email输入操作函数，并写入日志
    def input_email(self,email):
          self.find_element(*self.email).send_keys(email)
          logger.info("输入email:%s." % email)
    #定义密码输入操作函数，并写入日志
    def input_password(self, password):
          self.find_element(*self.password).send_keys(password)
          logger.info("输入密码:%s." % password)
    #定义确认密码输入操作函数，并写入日志
    def input_comfirpwd(self, comfirpwd):
          self.find_element(*self.confirmpw).send_keys(comfirpwd)
          logger.info("输入确认密码:%s." % comfirpwd)
    #定义提交操作函数，并写入日志
    def click_submit(self):
          self.find_element(*self.submit).click()
          logger.info("点击注册按钮")
