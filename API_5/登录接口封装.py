import requests
login = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
login_param = {'mobilephone':'18510267039','pwd':'123456'}
class denglujikou:
    def __init__(self):
        self.url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
        self.method = "get"
        self.param = {'mobilephone':'18510267039','pwd':'123456'}
    def http_requests(self): #默认值
        """根据请求判断请求是get还是post
           method是get、post  http 请求方式
        """
        if self.method.upper()=="GET":                 #判断是否是get请求
            try:
                res = requests.get(self.url,self.param)
            except Exception as e:
                print("执行的get请求出错：{}".format(e))
                res = print("Error:get请求报错{}".format(e))
        elif self.method.upper() =="POST":             #判断是否是post请求
            try:
                res = requests.post(self.url,self.param)

            except Exception as e:
                print("执行的post请求出错{}".format(e))
                res = print("Error:post请求报错{}".format(e))
        else:
            print("你的请求方式不对!")
            res =  print("Error:post请求报错{}".format(self.method))
        return res.cookies
if __name__ == '__main__':

    a = denglujikou().http_requests()
    print(a)