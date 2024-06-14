from utils.mysql import execute_update,execute_query
#定义图片类，有url、图片名、上传时间、所属者、类型
class Picture:
    def __init__(self, url, name, upload_time, email):
        self.url = url
        self.name = name
        self.upload_time = upload_time
        self.email = email
        
    def __str__(self):
        return f"Picture: {self.name}, Uploaded by {self.email}"
        
    def __repr__(self):
        return f"Picture(url={self.url}, name={self.name}, upload_time={self.upload_time}, owner={self.email})"
        
    def to_dict(self):
        return { 
            "url": self.url,
            "name": self.name,
            "upload_time": self.upload_time,
            "email": self.email,
        }
    #把图片信息加入数据库
    def insert_picture(self):
        #查看数据库是否有相同名字和所有者的数据
        sql = f"select * from picture where name='{self.name}' and email='{self.email}';"
        result = execute_query(sql)
        if len(result) > 0:
            sql = "UPDATE picture SET url=%s, upload_time=%s WHERE name=%s AND email=%s;"
        else:
            sql = f"insert into picture(url,  upload_time,name, email) values(%s,%s,%s,%s);"
        execute_update(sql,self.url,self.upload_time,self.name,self.email)
    #把图片信息删除
    def delete_picture(self):
        sql = f"delete from picture where url={self.url}"
        execute_update(sql)

    