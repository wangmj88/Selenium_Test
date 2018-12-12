import os
import configparser
def ReadConfig(name):
    cf = configparser.ConfigParser()
    # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
    parpath=os.path.abspath('.')
    #parpath=parpath.split(os.path.basename('.'))
    parpath=os.path.dirname(parpath)
    configPath = parpath + '\\config\\config.ini'
    cf.read(configPath)
    #获取配置文件中BrowserName对应的值
    browserconfig = cf.get('browser',name)
    return browserconfig