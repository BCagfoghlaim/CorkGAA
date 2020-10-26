from bs4 import BeautifulSoup
import requests

url = 'https://gaacork.ie/fixtures/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

infoList =[]
myTeam = 'Douglas' #Insert your team name here

matchDate = soup.find_all('ul', {'class':'column-eight table-body fixtures-'})
for match in matchDate:
  if match['data-hometeam'] == myTeam or match['data-awayteam']== myTeam:
    infoList.append(match['data-hometeam']+" vs. "+match['data-awayteam'])
    infoList.append("Date: "+match['data-date'])
    infoList.append(match['data-compname'])
    infoList.append(match['data-comment'])
    infoList.append("Venue: "+match['data-venue'])
    infoList.append("Time: "+match['data-time'])
    infoList.append("")

if not infoList:
  infoList.append("No fixtures available for " + myTeam + " at the moment.")

import smtplib

email_sender = 'SENDEREMAIL@email.com' #Insert the email address for the sender here
email_recipient = ['RECIPIENTEMAIL@email.com'] #Insert the email address for the recipient here
server = smtplib.SMTP('smtp.gmail.com', 587, timeout=300)
server.ehlo()
server.starttls()

server.login(email_sender,'PASSWORD') #Insert the login password for the sender's email here

SUBJECT = myTeam + "Fixtures"
TEXT = '\n'.join(infoList)
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

server.sendmail(email_sender,email_recipient,message)
server.quit()

