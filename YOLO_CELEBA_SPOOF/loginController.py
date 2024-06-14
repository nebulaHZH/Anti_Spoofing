#登录注册模块
#登录模块controller层
from flask import request,Blueprint
from model.user import User
from utils.mysql import create_connection
from utils.verify import send_verification_code
verify = dict()
log_app = Blueprint('log',__name__)
#定义用户登录模块
@log_app.route('/login',methods=['POST'])
def login():
    #获取登录传来的参数
    email = request.form.get('email')
    password = request.form.get('password')
    # 假设这里是从数据库中查询用户名和密码
    # 调用model层的方法，根据用户名获取用户信息
    user = User(email=email,password=password)
    return user.query()
    

#定义用户注册时的模块
@log_app.route('/register',methods=['POST'])
def register():
    #获取注册传来的参数
    password = request.form.get('password')
    email = request.form.get('email')
    verify_code = request.form.get('verify')
    print(verify[email],verify_code)
    if (str)(verify[email]) == (str)(verify_code):
        verify.pop(email)
        # 假设这里将用户信息插入到数据库中
        # 调用model层的方法，插入用户信息
        user = User(email=email,password=password)
        res = user.insert()
        if res == 'true' :
            return "ok"
        else:
            return str(res)
    return "false"


#定义发送验证码的模块
@log_app.route('/send_verify_code',methods=['POST'])
def send_verify_code():
    #获取发送验证码传来的参数
    email = request.form.get('email')
    verify_code = send_verification_code(email)
    print(verify_code)
    if verify_code != None:
        verify[email] = verify_code
        return (str)(verify_code)
    else:
        return "发送失败"
#查看该用户的所有图片
@log_app.route('/get_images',methods=['POST'])
def get_images():
    email = request.form.get('email')
    result = User.query_images(email=email)
    a = []
    b = []
    for r in result:
        if r['name'][:8] == 'analysis':
            a.append(r)
        else:
            b.append(r)
    return {'img':b,'analysis_img':a}
#查看该用户的所有视频
@log_app.route('/get_videos',methods=['POST'])
def get_videos():
    email = request.form.get('email')
    result = User.query_videos(email=email)
    a = []
    b = []
    for r in result:
        if r['name'][:8] == 'analysis':
            a.append(r)
        else:
            b.append(r)
    return {'video':b,'analysis_video':a}