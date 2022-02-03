from tokenize import String
from bs4 import BeautifulSoup
import requests
import smtplib
import os
#sending mail set up
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#get the text file from a web page
htmlContent = requests.get('https://www.masterduelmeta.com/').text

soup = BeautifulSoup(htmlContent,'lxml')

newCards = soup.find_all('div',class_='perspective svelte-kncn9e')
 
 # create an empty string
mailContent = ""




for newCard in newCards:
    tile = newCard.find('p', class_='title svelte-kncn9e').text
    updateTime = newCard.find('div', class_='sub-text full-width svelte-kncn9e').text
    anchorLink = newCard.find('a',class_='image-card svelte-kncn9e')
    mailContent = mailContent + ("\n ---------------------------------------------------------------------------------- \n")
    anchorHref = anchorLink['href']
    updateTime.rstrip("\n")
    anchorHref.rstrip("\n")
    mailContent = mailContent + ("Tile: "+ tile + "\n")
    if(len(updateTime) != 0):
       mailContent = mailContent + ("Info: "+ updateTime)
    mailContent = mailContent + ("Link:" + 'https://www.masterduelmeta.com'+anchorHref)




mail_content = mailContent
#The mail addresses and password
sender_address = 'tannguyen1220@gmail.com'
sender_pass = os.environ.get('MAIL_PASS')
receiver_address = 'nguyentaan1220@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Today news. It has an attachment.'   #The subject line
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
print('Mail Sent')
