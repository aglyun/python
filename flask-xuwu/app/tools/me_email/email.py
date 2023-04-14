# 工具文件
from flask_mail import Mail, Message

mail = Mail()


# 邮箱
def send_mail(subject, to, body):
    # 自定义函数，用于发送邮件
    msg = Message(subject,  # 主题
                  sender="guixu001@qq.com",  # 发送人邮箱
                  recipients=[to], body=body)  # 接收人邮箱
    mail.send(msg)
