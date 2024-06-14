#定义一个视频类，属性包括：类型、上传时间、所属者、url、视频名



from utils.mysql import execute_query, execute_update


class Video:
    def __init__(self, upload_time, email, url, name):
        self.upload_time = upload_time
        self.email = email
        self.url = url
        self.name = name
    #定义视频加入数据库
    def insert_vedio(self):
        #查看数据库是否有相同名字和所有者的数据
        sql = f"select * from video where name='{self.name}' and email='{self.email}';"
        result = execute_query(sql)
        if len(result) > 0:
            sql = "UPDATE video SET url=%s, upload_time=%s WHERE name=%s AND email=%s;"
        else:
            sql = f"insert into video(url,upload_time,name, email) values(%s,%s,%s,%s);"
        execute_update(sql,self.url,self.upload_time,self.name,self.email)
    #定义视频从数据库删除
    def delete_vedio(self):
        sql = f"delete from video where url={self.url}"
        return execute_update(sql)