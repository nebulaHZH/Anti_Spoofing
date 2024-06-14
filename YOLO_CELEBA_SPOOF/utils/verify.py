#定义一个函数发送验证码到qq邮箱并返回该验证码
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random

def send_verification_code(email):
    # 设置SMTP服务器
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    smtp_username = '3113631254@qq.com'  # 替换为你的QQ邮箱账号
    smtp_password = 'iefwrapnwtbndeha'  # 替换为你的QQ邮箱密码
    
    # 设置邮件内容
    verification_code = random.randint(1000, 9999)
    subject = '人脸反欺诈在线分析验证码'
    content = f'你的验证码为: {verification_code}'
    
    # 创建邮件对象
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = smtp_username
    msg['To'] = Header(email, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    
    # 发送邮件
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, [email], msg.as_string())
        server.quit()
        return verification_code
    except Exception as e:
        print(f"Failed to send email: {e}")
        return None