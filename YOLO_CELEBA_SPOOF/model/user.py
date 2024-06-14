
from utils.mysql import execute_update,execute_query
#定义用户类，属性有用户名、密码
class User:
    def __init__(self,password,email):
        self.password = password
        self.email = email
    
    def query(self):
        sql = f"SELECT * FROM users WHERE email = '{self.email}' and password = '{self.password}';"
        results = execute_query(sql)
        if len(results) == 1:
            return "true"
        return "false"
    def insert(self):
        sql = f"INSERT INTO users (email, password) VALUES ('{self.email}', '{self.password}');"
        res = execute_update(sql)
        if res == True:
            return "true"
        return res
    #通过邮箱查看所有图片
    @staticmethod
    def query_images(email):
        sql = f"SELECT * FROM picture WHERE email = '{email}';"
        results = execute_query(sql)
        return results
    #通过邮箱查看所有视频
    @staticmethod
    def query_videos(email):
        sql = f"SELECT * FROM video WHERE email = '{email}';"
        results = execute_query(sql)
        return results