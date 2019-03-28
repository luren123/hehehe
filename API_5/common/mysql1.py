from  mysql import connector
from API_5.common.read_config import ReadConfig
from API_5.common import project_path
class DoMysql:
    """操作数据库的类"""
    def domysql(self,query,flag=1):
        """
        query: sql 查询语句
        flag:   标志 1 查询单条数据  2查询多条数据
        """
        #根据配置文件获取接口·数据库连接信息
        db_config = eval(ReadConfig(project_path.conf_path).get_str("SQL","db_config"))
        cnn = connector.connect(**db_config)  # 建立一个连接  字典作为关键字参数不需要加两个星号
        # 获取游标 获取操作数据库的权限
        cursor = cnn.cursor()
        #这里是传入的数据库语句
        cursor.execute(query)
        # 获取并打印结果 fetchone 获取单行数据
        if flag==1:
            res = cursor.fetchone()  # 如果单行的和多行的数据一块查，根据光标位置读取,返回的值是元祖
        else:
            res = cursor.fetchall()  # 返回的是列表嵌套元组
        return res
if __name__ == '__main__':
    query = "select ID,MobilePhone from member where ID<=23528"
    res = DoMysql().domysql(query,1)
    print("数据库查询的结果是：{}".format(res))