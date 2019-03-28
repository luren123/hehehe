import HTMLTestRunnerNew  # 导入测试报告模块
import unittest  # 导入模块
import json
from API_5.common.do_excel import DoExcsl  # 导入类
from ddt import data, ddt
from API_5.common import project_path  # 导入用例的绝对路径
from API_5.common.接口日志 import Mylog
from API_5.common.http_request import jikoufengzhuang

#获取测试用例
test_Register = DoExcsl(project_path.case_path,"login").login_excel()
# print(test_Register)
#实例化logging
logger = Mylog()
# print(test_Register)
COOKIES = None
@ddt#装饰用例
class TestHttpRequest(unittest.TestCase):  #定义一个类
    def setUp(self):
        self.t = DoExcsl(project_path.case_path,"login")

        print("开始执行用例了！")
    @data(*test_Register)         #准备测试工作/测试环境
    def test_001(self,L):
            # print(L["ExpectedResult"])
            global TesReult  # 定义全局变量
            global COOKIES
            print("---------------")
            logger.info("********")
            logger.info("正在执行{}模块第{}条用例：{}".format(L["Module"],L["Case_id"],L["Title"]))
            logger.info("请求的数据是：{}".format(L["Params"]))
            #执行http请求
            res = jikoufengzhuang(L["url"],param=eval(L["Params"])).http_requests(L["Method"],cookies=COOKIES)  #实际结果
            print("用例执行的结果是：{}".format(res.text))
            try:
                self.assertEqual(json.loads(L["ExpectedResult"]),res.json())
                TesReult = "PASS"               #如果不报错，则结果为PASS
            except AssertionError as e:         #对比实际结果与预期结果
                logger.info("http请求测试用例出错了，错误是：".format(e))
                print("实际结果与预期结果不一致！")
                TesReult = "Fail"               #如果报错，则结果为Feil
                print("异常的报错为：".format(e))
                raise e


            finally:  #执行完毕后最终都要写在Excel中
                #这里利用了用例的ID与用例刚好是加一的关系
                logger.info("******开始写入数据******")
                self.t.write_excel(L["Case_id"]+1, 9, TesReult)
                self.t.write_excel(L["Case_id"]+1, 8, res.text)  #写入实际结果
                logger.info("******结束写入数据******")

suite = unittest.TestSuite()  #测试套件
loader = unittest.TestLoader()#用来加载用例 加载器
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))  #运行Testadd类下面的所有用例

with open("text.html","wb") as file:  #创建一个文件存储测试报告
      runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                verbosity=2,
                                                title="接口自动化测试报告",
                                                description="2019.3.10测试报告",
                                                tester="路人")
      runner.run(suite) #执行测试套间里面的用例