import smtplib
import imaplib
import time
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


msg = MIMEMultipart()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
conn = imaplib.IMAP4_SSL('imap.gmail.com', port = 993)
class SendEmail:
    fromaddr = ""
    toaddr = ""
    subject = ""
    password = ""
    def __init__(self, fromaddr, toaddr):
        self.fromaddr = fromaddr
        self. toaddr = toaddr

    def setCCRecipient(self,CCRec):
        msg['CC'] = CCRec
        return msg

    def SetEmailSubject(self, Subject):
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = Subject
        return msg

    def SetEmailMessage(self, message):
        msg.attach(MIMEText(message, 'plain'))
        return msg

    def Login (self,password):
        try:
            conn.login(self.fromaddr,password)
            server.ehlo()
            server.login(self.fromaddr, password)
            return server
        except Exception as e:
            print "The password is wrong\n\n"
            print str(e)

    def Send(self):
        try:
            server.sendmail(self.fromaddr,self.toaddr.split(','),msg.as_string())
            server.quit()
            print 'Succesfully Send email to '+self.toaddr
        except Exception as e:
                    print 'Failed to send email'
                    print str(e)

    def toDraft(self):
        conn.select('[Gmail]/Drafts')
        conn.append('[Gmail]/Drafts', '', imaplib.Time2Internaldate(time.time()), msg.as_string())

    # def deleteDraft(self,subject):
