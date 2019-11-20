from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time

from filters import PM_filter 

def checkforPms(Browser):
    time.sleep(2)
    browser = Browser

    time.sleep(0)


    for i in range(0,5):
        try:
            #print('trying to get result1')
            result1 = browser.find_element_by_xpath(f"(//td[@class='credit'][contains(.,'production manager')])[i]")
            #print('result1', result1.text)
            if result1.text == 'production manager':
                return 'production manager' 
            else: 
                #print('PM not found')
                return 'no pm found'
        except:
            pass
            #print('could not create result1')
    try:
        #print('trying to get result2')
        results2 = browser.find_elements_by_xpath(f"(//td[@class='credit'][contains(.,'production manager')])")
        #print('results2 length:', len(results2))
        
        for i in results2:
            #print('i.text:', i.text)    
            if PM_filter(i.text) == 'production manager':
                return 'production manager' 
            else: 
                pass
                #print('some other manager', i.text)
    except:    
        print('could not create result2')



def get_production_crew(Browser):
    time.sleep(2)
    #print('get_production_crew')
    browser = Browser 
    # this seems to be breaking it at the moment. 
    CastandCrew = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "listo", " " ))]')

    #print('CastandCrew.text', len(CastandCrew.text))
    bigstring = CastandCrew.text
    biglist = bigstring.split('..')
    biglist2 = []
    for i in biglist:
        sub = i.split('\n')
        for i in sub:
            biglist2.append(i)
    #for i in biglist2:
        ##print(i)

    #print('return biglist2')
    return biglist2

def get_every_name(Browser):
    time.sleep(0) 
    #print('get_every_name')
    browser = Browser 
    #print('creating NamesObject')
    #print('browser:', browser)
    NamesObject = browser.find_elements_by_xpath('//*[(@id = "fullcredits_content")]//a')
    Names = []
    #print('looping over NamesObject')
    for i in NamesObject:
        Names.append(i.text)
    #print('Names', len(Names))    
    #print('return Names')
    return Names

def get_PM_name(PMtest, URL, List, Browser):

    time.sleep(0) 
    Crew_and_titles = List 
    #print('^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    #print('in side get_PM_name')
    #print('PMtest:', PMtest,)
    #print('url:', URL,)
    #print('List_len:',len(List))

    browser = Browser
    #print('check what PMtest is returning')
    if PMtest == 'production manager':  
        #print('PMtest:', PMtest)
        ## seem like the break down is happening in here!!!
        for i in range(0,len(Crew_and_titles)):
             ##print('for i in range()')
             if 'production manager' in Crew_and_titles[i]: 
                    # need to filter post production manager
                    if 'post-production manager' not in Crew_and_titles[i]:

                 # this is where i can find the heads of. 

                        PMsNameNumb = i-1
                        #print('PMsNameNumb:', PMsNameNumb)
                        NameText = Crew_and_titles[PMsNameNumb]
                        #print('NameText:', NameText)
                        NameText = NameText.strip(' . ')
                        #print('NameText stripped:', NameText)
                        Namelistsplist = NameText.splitlines()
                        #print('Namelistsplist:',Namelistsplist)
                        #print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        #print('Namelistsplist[0]', Namelistsplist[0])
                        #print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                        #print('PM', Namelistsplist[0],PMsNameNumb)
                        return Namelistsplist[0]
                        ## this seems to be the issue.### there is some issue with this list. Almost there!!!

             else:
                 ##print('PM name not in crew list')
                 pass 
    else: 

        return 'No PM' 



# I need to check to see if there is a 'See full cast' link and click it. 

def find_See_full_cast(Browser):
    #print('find_See_full_cast')
    browser = Browser

    seefullcast = browser.find_element_by_xpath('//a[contains(.,"See full cast")]')  
    #print('seefullcast.text', seefullcast.text)
    
    seefullcast.click()




# it is only getting one PM's name, but I can live with that. 
# it is not closing the Browser. That seems to be an issue. 
# i think i need a way to store the url created buy the crawl to pass it to the scrapper. 
# I still seem to have the [2] xpath issue. 


#url = 'https://www.imdb.com/title/tt1703806/fullcredits?ref_=tt_ql_1'
#L = get_PM_name(checkforPms(url), url, get_production_crew(url))
##print(L)

