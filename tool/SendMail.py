#############################################################################
#   Author: Nguyen Quoc Truong                                              #
#   Developer: T&T Stdudio                                                  #
#   Description: Send mail for manager when there is change in Database     #
#                or Google Sheet.                                           #
#   Usage: Included and used in DataInterface.py                            #
#############################################################################

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from GetMachineInfo import *
from constants import Managers as mng
from datetime import datetime


def send_email(body):
    # Email configuration
    sender_email = mng.BOT_GMAIL
    sender_password = mng.BOT_GMAIL_APP_PASS
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    to_emails = [
        mng.MANAGER_LIST['truong'][1],
        # mng.MANAGER_LIST['hieu'][1],
        # mng.MANAGER_LIST['khoi'][1]
    ]

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(to_emails)
    message['Subject'] = mng.MAIL_SUBJECT

    # Attach body
    message.attach(MIMEText(body, 'html'))

    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, to_emails, message.as_string())
    
    print("Send mail successfully!")

def get_manager_name():
    mac_id = get_mac_address()
    if mac_id == '08:8F:C3:43:8F:C4':
        return mng.MANAGER_LIST['truong'][0]
    elif mac_id == 'hieu_mac':
        return mng.MANAGER_LIST['hieu'][0]
    elif mac_id == 'khoi_mac':
        return mng.MANAGER_LIST['khoi'][0]
    else:
        return 'Unknown'

def create_message(name, time, data_name, mode, note):
    list_data_str = ', '.join(data_name).upper()
    message = "Xin chào,<br><br>"
    message += "Dữ liệu * <b>{}</b> * trong {} vừa được thay đổi.<br>".format(list_data_str, 'Database' if mode == 'db' else 'Google Sheet')
    message += "{} đã cập nhật ✎ vào lúc {}.<br>".format(name, time)
    if note != "":
        message += "<u>Ghi chú</u>: {}.<br>".format(note)
    message += "<br>"
    message += "Cảm ơn và trân trọng 😊,<br>"
    message += "Hi Coffee Bot"
    return message


# list_data = [ 'drink', 'cake' ]
# print(create_message(get_manager_name(get_mac_address()), datetime.now(), str(list_data), 'sh'))
# recipient_emails = [mng.MANAGER_LIST['truong'][1], mng.MANAGER_LIST['hieu'][1], mng.MANAGER_LIST['khoi'][1]]

# send_email(create_message(get_manager_name(get_mac_address()), datetime.now(), str(list_data), 'sh'))