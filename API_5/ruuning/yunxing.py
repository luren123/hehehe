import HTMLTestRunnerNew
import unittest
from API_5.common import test_recharge

suite = unittest.TestSuite()  #测试套件
loader = unittest.TestLoader()#用来加载用例 加载器
suite.addTest(loader.loadTestsFromModule(test_recharge))  #运行Testadd类下面的所有用例

with open("text.html","wb") as file:  #创建一个文件存储测试报告
      runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                verbosity=2,
                                                title="接口自动化测试报告",
                                                description="2019.3.10测试报告",
                                                tester="路人")
      runner.run(suite) #执行测试套间里面的用例