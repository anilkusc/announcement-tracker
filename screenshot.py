from selenium import webdriver
import io
from PIL import Image
import time

def print_announcement(link):
    fox = webdriver.Firefox()
    fox.get(link)
    time.sleep(5)
    image = fox.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div/div[2]').screenshot_as_png
    imageStream = io.BytesIO(image)
    im = Image.open(imageStream)
    im.save("/mnt/image.png")
    fox.quit()
