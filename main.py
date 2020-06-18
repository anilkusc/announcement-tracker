import startup
import control
import screenshot
import mail
import time
import datetime
import os
import teias_control

debug = os.getenv('DEBUG','false')

if debug == 'true':
        recipients = ["akuscu95@gmail.com"]
else:
    recipients = ["akuscu95@gmail.com"]

print ("starting.Debug is :" + debug)

startup.tpys()
startup.init()

var = 1
while var == 1 :

    if debug == 'true':
        time.sleep(10)
    else:
        time.sleep(600)

    if control.is_there_new_announce(0) == 1:
        screenshot.print_announcement(control.take_link(0))
        for recipient in recipients:
            mail.sendmail(recipient,control.take_link(0))
        startup.init()                        
    else:

        if debug == 'true':
            print ( str(datetime.datetime.now()) + " there is no new announce.")    
