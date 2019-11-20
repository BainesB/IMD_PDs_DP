
#from scrapeProductionManagers import checkforPms, GetPMsName
from small_Scraper_bits import * # nothing there at the moe
from grab_every_credit import Create_Credit_List


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time

#Website = browser.get('https://www.imdb.com/title/tt1703806/fullcredits?ref_=tt_ql_1')

'''
def test_PM_present():
    
    X = checkforPms('https://www.imdb.com/title/tt1703806/fullcredits?ref_=tt_ql_1')

    assert X == 'production manager'
    # have test tne null result. 
'''

def test_PM_name():
    url = 'https://www.imdb.com/title/tt1703806/fullcredits?ref_=tt_ql_1'
    # list is missing from this test. 
    # At the moment it just isn't finding the PMs names. 
    # i need to build a list of crew and titles.  
    # need to open a browser connection. 
    browser = webdriver.Firefox()
    browser.get('https://www.imdb.com/title/tt8080302/fullcredits?ref_=tt_ql_1')
    x = get_PM_name(checkforPms(url), url,get_production_crew(browser))
    print(x)
