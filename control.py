import requests
from bs4 import BeautifulSoup

announcement_link = "https://support.google.com/chrome/announcements/9269159?hl=en"
def is_there_new_announce(announce_index):
    lastannounce = announcement(announce_index)
    f = open("lastannouncement.txt", "r")
    if f.read() == lastannounce.text:
        print ("there is no new announce.")
        print (lastannounce)
        return 0
    else:
        print ("there is some new announces.Mailing...")
        return 1
def announcement(index):
    r = requests.get(announcement_link)
    source = BeautifulSoup(r.content,"lxml")
    return source.findAll('tbody')[0].findAll('tr')[index]
def take_link(index):
    lastannounce = announcement(index)
    return lastannounce.findAll("td")[1].findAll("a")[0].attrs['href']
        
