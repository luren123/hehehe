#1、什么是正则表达式？ 编写规范查找需要的字符串
#2、正则表达式的组成：原义字符 和 元字符
#3、如何用Python来解析？
#4、使用正则表达式的场景#---参数化  比如查找一些邮箱、手机号码，身份证号码...
#.点号 可以匹配单个字符、汉字、英文、符号、数字
import re
from API_5.common.get_data import GetData
# target = "{'mobliephone':'#normal_user#','pwd':'#bormal_user#'}"
# p = 'normal_user'  #原义字符串查找
# p2 = '#(.*?)#' #元字符查找,圆括号代表正则表达式组的概念
# m = re.search(p2,target) #在目标的字符串里面查找，如果有匹配的字符串就返回对象
# print(m)
# print(m.group())  #不传参的情况下，返回表达式和你匹配的字符串
# print(m.group(1)) #我只要找的的第一个，传参就是只匹配字符串，也就是当前表达式所匹配到的字符串
# m2 = re.findall(p2,target)  #找到所有匹配到的字符，返回的是一个列表
# print(m2)

#matach() 从字符串的开头位置进行匹配
#search() 对字符串的任意位置进行匹配，但是匹配到第一个就会返回
#findall() 返回字符串中所有匹配的字符串并返回一个列表的形式
#finditer()返回一个包含了所有匹配对象的迭代器

#sub函数使用：将匹配的字符串进行替换
#pattern ：正则表达式
#repl：替换的字符串，也可以作为一个函数。
#string
# target2 = re.sub(p2,"18510267039",target,count=1)
# print(target2)
class replace:
    def tiqvshoujihao(self):
        target = "{'mobliephone':'#normal_user#','pwd':'#normal_pwd#'}"
        p2 = '#(.*?)#'

        while re.search(p2,target):   #查找参数的字符串matach ,如果找到那么返回Ture
            m = re.search(p2, target)  # 在目标的字符串里面查找，如果有匹配的字符串就返回对象
            # print(m)
            key = m.group(1)           #拿到对应的key
            # print(key)
            value = getattr(GetData,key)       #拿到我们想要替换的内容
            # print(value)
            target = re.sub(p2,value,target,count=1)    #进行替换

if __name__ == '__main__':
    res = replace().tiqvshoujihao()
    print(res)