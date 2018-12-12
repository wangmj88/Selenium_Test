from script.module import *
import time
import os.path
import unittest
import common.HTMLTestRunner
class ECShop(unittest.TestCase):
     def setUp(self):
          print("start ecshop测试执行 ")

     def test_ECshop(self):
          tspath=os.path.abspath('.')
          tsname=tspath+'\\data\\testsuite.xlsx'
          self.assertTrue(read_testsuite(tsname))
     def test_Login(self):
          pass
     def test_Register(self):
          pass

     def tearDown(self):
          print("end ecshop测试执行")

if __name__ == '__main__':
     test=unittest.TestSuite()
     test.addTest(ECShop('test_ECshop'))
     test.addTest(ECShop('test_Login'))
     test.addTest(ECShop('test_Register'))
     rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
     file_path=os.path.abspath('.') + '\\report\\'+rq+'-result.html'
     file_result=open(file_path,'wb')
     logger.info('测试完成，正在生成测试报告')
     runner=common.HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'ECShop测试报告',description=u'用例执行情况')
     runner.run(test)
     file_result.close()

