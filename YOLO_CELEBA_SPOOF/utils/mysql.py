#定义mysql相关连接
import pymysql
connection = None
# 创建数据库连接
def create_connection():
    global connection
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='face_anti_spoofing',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        print("成功连接到数据库")
        
    except pymysql.MySQLError as e:
        print("连接到MySQL时发生错误:", e)

# 关闭数据库连接
def close_connection(connection):
    connection.close()
    print("数据库连接已关闭")\
# 执行SQL查询
def execute_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
# 执行SQL更新
def execute_update(query,*args):
    with connection.cursor() as cursor:
        try:
            #print(query)
            cursor.execute(query,args)
            
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return e