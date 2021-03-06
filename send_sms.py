# -*- coding: utf-8 -*-
"""

example:
  python send_sms.py "1234567890@txt.att.net" "lol"
  
  First argument is the email address associated with a mobile phone
  Second argument is the message to be sent

@author: julian.irwin@gmail.com
"""
import imp
import sys

SMSNotifier = imp.load_source('SMSNotifier', r'...path_to_file\SMSNotifier.py')
creds = imp.load_source('SMSCredentials', r'...path_to_file\SMSCredentials.py')

credentials = creds.labview_credentials
credentials[3] = sys.argv[1]

phone = SMSNotifier.SMSNotifier(*credentials)
phone.send(sys.argv[2])



