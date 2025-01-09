import smtplib
from email.mime.text import MIMEText
from email.header import Header
def main():
    automail('rogers2288@gmail.com', 'this is a test')
    print('ok')

def automail(usermail, bodytext):
    mail_account  = 'yshr@yeoshe.com.tw'
    mail_password = '5yjm%rdx'
    from_add = mail_account #寄件者
    to = usermail           #收件者
    subject = u'Test send mail' #主旨
    body = bodytext

    message = MIMEText(body, 'html','utf-8')
    message['From'] = Header(from_add)
    #message['To'] = Header('twa115@yeoshe.com.tw')
    message['To'] = Header(usermail)
    message['Subject'] = Header(subject)

    smtpObj = smtplib.SMTP('220.168.100.105', 25) #連線mail server
    smtpObj.login(mail_account, mail_password) #登入
    smtpObj.sendmail(from_add, to, message.as_string()) #寄信
    smtpObj.close #結束
    
if __name__ == '__main__':
    main()
