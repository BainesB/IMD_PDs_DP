# IMPORTS 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
from grab_every_credit import Create_Credit_List

# open a browser connection. 

browser = webdriver.Firefox()

# list of urls where i know there is a PM

#browser.get('https://www.imdb.com/title/tt1777610/fullcredits?ref_=tt_ql_1')
browser.get('https://www.imdb.com/title/tt1703806/fullcredits?ref_=tt_ql_1')
#browser.get('https://www.imdb.com/title/tt0861731/fullcredits?ref_=tt_ql_1')
credits_object = browser.find_elements_by_xpath("//td[@class='credit']")


def checkforPms():
    # sometimes there is more than one PM. 

    result = browser.find_element_by_xpath(f"(//td[@class='credit'][contains(.,'production manager')])[2]")

    # this is interesting sometimes the '[2]' at the end of the xpath works sometimes it makes it miss and i have to get rid of it. 
    

    count = 0
    PMsNameNumb = 0

    if result.text == 'production manager':
        #print('pm', result.text)

        CastandCrew = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "listo", " " ))]')

        bigstring = CastandCrew.text
        biglist = bigstring.split('..')
        NameText = ''

        for i in range(0,len(biglist)):

            if 'production manager' in biglist[i] and 'post-production manager' not in biglist[i]:
                #print('biglist[i]:', biglist[i])
                #print('&&&&&&&&&&&&&&&&&&&&')
                PMsNameNumb = i-1

                #print('..........................')
                #print('PMs number', PMsNameNumb, biglist[PMsNameNumb])
               
                #print('PMs biglist[PMsNameNumb]:',biglist[PMsNameNumb])
                #print('**************************')
                NameText = biglist[PMsNameNumb]
                print('NameText',NameText)

                return NameText


            count += 1

    else: 
        return 'nope' 

# turn this into a function. 

def GetPMsName(checkforPms,credits_object):
    time.sleep(1)
    Name_longstring = checkforPms

    credit_list = Create_Credit_List(credits_object)

    for i in credits_object:
        string = str(i.text)
        if string in Name_longstring:
            stripped_name = Name_longstring.strip(' . '+string).strip('\n')
            print('Production Manager', stripped_name)
            # works but she is on the line bellow
            return stripped_name

PMs_Name = GetPMsName(checkforPms(),credits_object)

print('PMs_Name: ', PMs_Name ) 

browser.close()

