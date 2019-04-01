import requests #引入requests模块

     #创建初始化对象，每次请求需要提供url param两个参数
class jikoufengzhuang:
    # def __init__(self,url,param):
    #     self.url = url
    #     self.param = param
    def http_requests(self,url,method,param,cookies): #默认值
        """根据请求判断请求是get还是post
           method是get、post  http 请求方式
        """
        if method.upper()=="GET":                 #判断是否是get请求
            try:
                res = requests.get(url=url,params=param,cookies=cookies) #传递一个cookies
            except Exception as e:
                print("执行的get请求出错：{}".format(e))
                res = print("Error:get请求报错{}".format(e))
        elif method.upper() =="POST":             #判断是否是post请求
            try:
                res = requests.post(url=url,params=param,cookies=cookies)

            except Exception as e:
                print("执行的post请求出错{}".format(e))
                res = print("Error:post请求报错{}".format(e))
        else:
            print("你的请求方式不对!")
            res =  print("Error:post请求报错{}".format(method))
        return res



if __name__ == '__main__':

    res =jikoufengzhuang().http_requests(url ="http://120.78.128.25:8080/futureloan/mvc/api/member/register",param={'mobilephone':'18510267039','pwd':'123456'},method="post",cookies=None)
    print(res.text)
    # print(type(res.json()["status"]))