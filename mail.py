From = "your-email-address"
Host= "your-smtp-host"
Password = "your-password"
Port = 587
Recipients = "To@gmail.com"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = Recipients
msg['Subject'] = 'There is New Announcement'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP(Host,587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(From, Password)

mailserver.sendmail(From,Recipients,msg.as_string())

mailserver.quit()
