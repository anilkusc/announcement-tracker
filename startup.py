import control
def init():
    lastannounce = control.announcement(0)
   #TO-DO : check if is the link ready ? For example web page changed.notifiy users.  
    f = open("lastannouncement.txt", "w")
    print("Writing last announcing to file...")
    f.write(lastannounce.text)
    print("Writed")
    f.close()
