from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time

# As of 31 of July 2019 they only have 4 pages of results.

DSP_IMDB_URLs = [

            'https://www.imdb.com/search/title/?companies=co0174816',
            'https://www.imdb.com/search/title/?companies=co0174816&start=51&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?companies=co0174816&start=101&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?companies=co0174816&start=151&ref_=adv_nxt',

        ]

    # I need to have a seriously think about what information I want to store. 
    # I need the production Name and the dirrect. 
    # I also want to get the Production Managers Name. 

def getIMDB_Titles(url):
    browser = webdriver.Firefox()
    browser.get(url)
    Titles = browser.find_elements_by_class_name('lister-item-header')
    for i in Titles:
        print('title.text:',i.text) 
    
def getIMDB_Dirrectors_Titles(url):

    browser = webdriver.Firefox()
    print('getting page')
    browser.get(url)
    print('extract text.')
    # gets all the text. 

    TextContent = browser.find_elements_by_class_name("lister-item-content")
    Titles = browser.find_elements_by_class_name('lister-item-header')

    # Trys to get the dirrectors name if it is there. 
    print('printing text')

    for i in TextContent:
        try:
            content_list =  i.text.split('Director:')
            content_sublist = content_list[1].split('|')
            director_name = content_sublist[0]
            title_content_list = i.text.split('.')
            title_content_sublist = title_content_list[1].split('(')
            
            date_content_list = i.text.split('(')
            date_content_sublist = date_content_list[1].split(')') 
            
            #print(date_content_sublist[0])

            print(
                    'Title:',
                    title_content_sublist[0],
                    'Director:',
                    director_name,  
                    'ProdDate:',
                    date_content_sublist[0]
                    )

        except:
            print('######### Could not find director #########')

    browser.close()
    print('Close Browser')
   
#x = getIMDB_Dirrectors(DSP_IMDB_URLs[0])


for i in DSP_IMDB_URLs:
    D = getIMDB_Dirrectors_Titles(i)
    time.sleep(5)
