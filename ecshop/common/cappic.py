import logging
import os.path
import time
def Cappic(driver):
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    pic_path = os.path.abspath('.') + '\\picture\\'
    pic_name = pic_path + rq + '.png'
    driver.get_screenshot_as_file(pic_name)
    #driver.quit()
    return pic_name
