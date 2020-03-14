import inspect
import subprocess
import time

from utils.LogWorker import LogMan


class Toolbar():
    log = LogMan(__name__)

    @classmethod
    def getReportName(cls):
        now = int(time.time())
        timeArray = time.localtime(now)
        style_time = time.strftime('%Y年%m月%d日%H点%M分%S秒', timeArray)
        # now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        report_name = '接口测试报告' + style_time + '.html'
        return "--html=../report/{}".format(report_name)

    @classmethod
    def get__function_name(cls):
        '''获取正在运行函数(或方法)名称'''
        return inspect.stack()[1][3]

    @classmethod
    def exec_allure_script(cls, path, html):
        cls.log.info('allure generate {} -o {} --clean'.format(path, html))
        try:
            subprocess.call('allure generate {} -o {} --clean'.format(path, html), shell=True)
            cls.log.info('正在生成allure报告.......')
        except:
            cls.log.error('执行allure generate ......失败 请检查')
            raise
        finally:
            cls.log.info('end.....')
