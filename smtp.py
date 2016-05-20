import smtplib

# To deal with headers easily
# not strictly neccessary
from email import message

to_addr = 'exampleto@gmail.com'
from_addr = 'examplefrom@gmail.com'
password = 'your_pass'

# Initialise smtp Object
# smtp host here is 'smtp.gmail.com' and port is 587
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)	

# ehlo(Extended hello) - Make yourself known to server
smtpObj.ehlo()

# tls(Transport Layer Security) is a common
# method of encrypting communication
smtpObj.starttls()
smtpObj.ehlo()

# Login to smtp host
smtpObj.login(from_addr, password)

# Setting headers to your message
msg = message.Message()
msg.add_header('from', 'Name <' + from_addr + '>')
msg.add_header('to', to_addr)
# Note that this won't actually send the mail
# It'll just show up as cc'd to the person
msg.add_header('cc', 'examplecc@gmail.com')
msg.add_header('subject', 'First test email using smtp')
msg.set_payload("Your awesome email message")

# Function to send mail
smtpObj.sendmail(from_addr, to_addr, msg.as_string())

# Close the object connection after use
smtpObj.close()
