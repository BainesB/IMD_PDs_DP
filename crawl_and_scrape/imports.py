# I would like to know if there is a way to import all my imports... 

from selenium.webdriver.common.keys import Keys
import webbrowser
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import sqlite3
import inspect
import re
import time
import Just_titles


from small_Scraper_bits import *

browser = webdriver.Firefox()
browser.get('https://www.imdb.com/title/tt1777610/fullcredits?ref_=tt_ql_1')
#browser.get('https://www.imdb.com/title/tt8080302/fullcredits?ref_=tt_cl_sm#cast')

#checkforPms(browser)

url = browser.current_url

PMs_Name = get_PM_name(checkforPms(browser), url, get_production_crew(browser),browser)

# pm test is not working. I have no idea why???
