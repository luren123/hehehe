import re
from API_5.common.read_config import ReadConfig
from API_5.common import project_path
config = ReadConfig(project_path.conf_path)
class GetData:
      '''可以动态的进行增删改的操作'''
      COOKIES = None
      LOAN_ID = None
      normal_user = config.get_str("data","normal_user")
      normal_pwd = config.get_str("data","normal_pwd")
def raplace(target):
       p2 = '#(.*?)#'
       while re.search(p2, target):  # 查找参数的字符串matach ,如果找到那么返回Ture
           m = re.search(p2, target)  # 在目标的字符串里面查找，如果有匹配的字符串就返回对象
           key = m.group(1)  # 拿到对应的key
           value = getattr(GetData, key)  # 拿到我们想要替换的内容
           target = re.sub(p2, value, target, count=1)  # 进行替换
       return target