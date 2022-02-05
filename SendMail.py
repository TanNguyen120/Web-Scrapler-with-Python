import smtplib
import os
from dotenv import load_dotenv

#sending mail set up
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
# project_folder = os.path.expanduser('~/my-project-dir')  # adjust as appropriate
# load_dotenv(os.path.join(project_folder, '.env'))
def sendMailTo(mailContent, reciverAddress, Subject):
    mail_content = mailContent
    #The mail addresses and password
    sender_address = 'tannguyen1220@gmail.com'
    sender_pass = os.environ.get('MAIL_PASS')
    receiver_address = reciverAddress
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = Subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.ehlo
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent With Subject' + Subject)