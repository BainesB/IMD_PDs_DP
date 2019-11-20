from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import sqlite3 
import inspect 
import re 
import time
import Just_titles
from grab_every_credit import Create_Credit_List
from small_Scraper_bits import *

# open the browser at imdab

title_list = Just_titles.List_of_titles

def getIMDB(prodname):

    browser = webdriver.Firefox()
    browser.get('https://www.imdb.com')

    try:
        # locate the search box. 
        searchbox = browser.find_element_by_xpath('//*[(@id = "navbar-query")] ')
        print('enter prog name')

        searchbox.send_keys(prodname) # I need this to be i

        print('press enter')
        searchbox.send_keys(Keys.ENTER)

        print('put links in a list')

        time.sleep(5) 

        result = browser.find_element_by_xpath(f'//a[contains(.,"{prodname}")]')
        print('made result')
        print(result.text)
        # now I need to click this link.    
        result.click()

    except:
       print(f'could not find link to {prodname}') 

    try:
        # now click full cast and crew.
        time.sleep(5)
        fullcrew = browser.find_element_by_xpath('//a[contains(.,"FULL CAST AND CREW")]')  

        print(fullcrew.text) 
        fullcrew.click()
    except:
       print(f'could not find link to FULL CAST AND CREW for {prodname}') 
    # what to check if therer is a See full cast link
    try:
        find_See_full_cast(browser)
    except:
        pass 
    try:
        ## where we scrape. 
        time.sleep(5)
        url = browser.current_url
        print('url:', url)

        TherePm = checkforPms(browser)
        #print('TherePm', TherePm)
        production_crew = get_production_crew(browser)
        #print('production_crew length', len(production_crew))
        ## For some reason it can't run this next line of code. 
        PMs_Name = get_PM_name(TherePm, url, production_crew, browser)
        #time.sleep(2) 

        print('PMs_Name: ', PMs_Name ) 
        return PMs_Name

    except:
        print('not able to scrape PM for this production')


    print('closing browser')
    time.sleep(3)
    browser.close()
    print('closed page')


for i in title_list:
    time.sleep(2)
    try:
        name = str(getIMDB(i))
        title = str(i)
        print('Name that came out:', name)
        time.sleep(2)
        print('Enter title and PM into DB')
        DBName = 'IMDB.db'
        conn = sqlite3.connect(DBName) # this must need changing. 
        cursor = conn.cursor()
    
        try:
            cursor.execute(f'''
            INSERT INTO PM (title, ProductionManager)
            VALUES('{i}', '{name}');
            ''')
            conn.commit()

        except:
            print(f'''unable to enter value into database: {DBName}''')
            pass
    
        conn.close()
    except: 
        print('Probably connection refused')
        time.sleep(20)

    # Want to add 'i' to the DB 
    # changed the code above to return PMs_Name. 
    # this is not working so it think you need to try and gett it working in the shell. 
