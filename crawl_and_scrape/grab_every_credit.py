'''
# I want to clean up the production mangers name. 
# I want to grab all the .credits on the page. 
# and then run a for loop of over the Every_credit_list and if present strip()
# the credit from then name
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time




def Create_Credit_List(credits_object ):

    # return the list

    credits = []
    for i in credits_object: 
        credits.append(i.text)

    for i in credits:
        print('credit:', i)

    #print('credits', credits)
    time.sleep(3) 
    return credits





