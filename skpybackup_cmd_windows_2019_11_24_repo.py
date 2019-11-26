#
# https://pypi.org/project/auto-py-to-exe/

#
import sys

# https://skpy.t.allofti.me/
# pip install skpy
from skpy import Skype

# https://pandas.pydata.org/
# pip install pandas
import pandas as pd

#
import smtplib

#
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#
import datetime

#


class SkypeBackup:

    def __init__(self, user, password, connect=False):

        self.user = user
        self.password = password
        self.connect = connect

        self.sk = Skype(self.user, self.password, self.connect)

    def get_contacts_csv(self, sep=';', encoding="utf-8"):

        self.data_frame_contacts = pd.DataFrame(
            [vars(contact) for contact in self.sk.contacts])

        return self.data_frame_contacts.to_csv(sep=sep, encoding=encoding)

#


class Utils():

    @staticmethod
    def save_to_file(file_name, content):

        fh = open(file_name, 'w')
        fh.write(content)
        fh.close()


#
success = False

#
username = None
password = None

#
message = None

#
try:

    #
    try:

        # Username
        username = sys.argv[1]

    except:

        #
        username = None
    #
    try:

        # Password
        password = sys.argv[2]

    except:

        #
        password = None

    #
    if (username != None) and (password != None):

        #
        skype_backup = SkypeBackup(username, password)

        #
        skype_contacts_csv = skype_backup.get_contacts_csv()

        #
        file_name = (
            "contacts_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".csv")

        #
        Utils.save_to_file(file_name, skype_contacts_csv)

        #
        success = True

        #
        message = sys.argv[0].replace(sys.argv[0].split("\\")[-1], file_name)

    else:

        #
        success = False

        #
        message = "Insufficient parameters: <USERNAME> <PASSWORD>"

except Exception as e:

    #
    success = False

    #
    message = str(e)

#
print(success)

#
if (message != None):

    #
    print(message)
