import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "your-email@your-provider.com"
toaddr = "your-recipient@your-recipient.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your Subject"

body = "Your Message"

msg.attach(MIMEText(body,'plain'))

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(fromaddr, "Your Password")
    server.sendmail(fromaddr,toaddr,msg.as_string())
    server.quit()
    print 'Succesfully Send email to '+toaddr
except Exception as e:
    print 'Failed to send email'
    print str(e)
