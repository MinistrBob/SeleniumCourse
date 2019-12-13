import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")
