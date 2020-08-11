import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template


html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from']= 'Nida Bandukwala'
email['to']= '' // add email of recipient
email['subject']='helllloooo'

email.set_content(html.substitute(name ="nida", age = '19', university = 'McMaster University'))

with smtplib.SMTP(host='smtp.gmail.com',port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('nida.bandukwala@gmail.com','')
	smtp.send_message(email)
	print("all done")

