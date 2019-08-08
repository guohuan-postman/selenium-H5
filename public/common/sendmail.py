#coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.common.log import Log
from config import globalparam


from email import encoders
import os
import traceback
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



# 中文处理
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(to_addr_in, filepath_in):
	# 邮件发送和接收人配置
	from_addr = 'a15652002761@163.com'
	smtp_server = 'smtp.163.com'
	password = 'aa123456'  # 这是你邮箱的第三方授权客户端密码，并非你的登录密码
	to_addr = to_addr_in
	to_addrs = to_addr.split(',')

	msg = MIMEMultipart()
	#msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)  # 显示的发件人
	msg['From'] = _format_addr('郭玉欢 <%s>' % from_addr)  # 显示的发件人
	# msg['To'] = _format_addr('管理员 <%s>' % to_addr)                # 单个显示的收件人
	msg['To'] = ",".join(to_addrs)  # 多个显示的收件人
	#msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()  # 显示的邮件标题
	msg['Subject'] = Header('H5的UI自动化邮件报告……', 'utf-8').encode()  # 显示的邮件标题

	# 需要传入的路径
	# filepath = r'D:\test'
	filepath = filepath_in
	r = os.path.exists(filepath)
	if r is False:
		msg.attach(MIMEText('no file...', 'plain', 'utf-8'))
	else:
		# 邮件正文是MIMEText:
		msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
		# 遍历指定目录，显示目录下的所有文件名
		pathDir = os.listdir(filepath)
		pathDir.sort()

		for allDir in pathDir:

			child = os.path.join(filepath, allDir)
			#child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
			# 添加附件就是加上一个MIMEBase，从本地读取一个文件

			with open(child, 'rb') as f:
				# 设置附件的MIME和文件名，这里是html类型:
				mime = MIMEBase('file', 'html', filename=allDir)
				# 加上必要的头信息:
				mime.add_header('Content-Disposition', 'attachment', filename=allDir)
				mime.add_header('Content-ID', '<0>')
				mime.add_header('X-Attachment-Id', '0')
				# 把附件的内容读进来:
				mime.set_payload(f.read())
				# 用Base64编码:
				encoders.encode_base64(mime)
				# 添加到MIMEMultipart:
				msg.attach(mime)
				


	try:
		server = smtplib.SMTP(smtp_server, 25)
		# server.starttls()
		server.set_debuglevel(1)  # 用于显示邮件发送的执行步骤
		server.login(from_addr, password)
		# print to_addrs
		server.sendmail(from_addr, to_addrs, msg.as_string())
		server.quit()
	except Exception:
		print("Error: unable to send email")
		traceback.format_exc()
reportPath = globalparam.report_path

if __name__ == '__main__':

	send_email('guoyuhuan8602@dingtalk.com,2639339651@qq.com','C:/Users/Administrator/Desktop/seleniumUI/report/testreport/')










'''

# 测试报告的路径
reportPath = globalparam.report_path
print(reportPath)
logger = Log()
# 配置收发件人
recvaddress = ['henan5620@dingtalk.com', '2639339651@qq.com', 'guoyuhuan8602@dingtalk.com', 'xhbn2639339651@163.com','a15652002761@163.com','yanbo@yaopin.onaliyun.com']
# 163的用户名和密码
sendaddr_name = 'a15652002761@163.com'  #登入密码a123456
sendaddr_pswd = 'aa123456'        #设置客户端授权码 aa123456

class SendMail:
	def __init__(self,recver=None):
		"""接收邮件的人：list or tuple"""
		if recver is None:
			self.sendTo = recvaddress

		else:
			self.sendTo = recver

	def __get_report(self):
		"""获取最新测试报告"""
		dirs = os.listdir(reportPath)
		dirs.sort()
		newreportname = dirs[-1]
		print('The new report name: {0}'.format(newreportname))
		return newreportname

	def __take_messages(self):
		"""生成邮件的内容，和html报告附件"""
		newreport = self.__get_report()
		self.msg = MIMEMultipart()
		# 此处告知是邮件标题
		self.msg['Subject'] = '测试报告主题'
		self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

		with open(os.path.join(reportPath,newreport), 'rb') as f:
			mailbody = f.read()
			print(mailbody)
		html = MIMEText(mailbody,_subtype='html',_charset='utf-8')
		self.msg.attach(html)
		
		# html附件
		att1 = MIMEText(mailbody, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		att1["Content-Disposition"] = 'attachment; filename="H5页面自动化测试报告.html"'
		self.msg.attach(att1)

	def send(self):
		"""发送邮件"""
		self.__take_messages()
		self.msg['from'] = sendaddr_name

		try:
			smtp = smtplib.SMTP('smtp.163.com', 25)
			smtp.login(sendaddr_name, sendaddr_pswd)
			smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
			smtp.close()
			logger.info("发送邮件成功")
		except Exception:
			logger.error('发送邮件失败')
			raise

if __name__ == '__main__':
	sendMail = SendMail()
	sendMail.send()
'''
        
