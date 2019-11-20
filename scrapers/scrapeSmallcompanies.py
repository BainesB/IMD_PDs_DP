from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time

# As of 31 of July 2019 they only have 4 pages of results.


Plumb_Pictures_Urls = [

        'https://www.imdb.com/search/title/?companies=co0284770&ref_=adv_prv',
        'https://www.imdb.com/search/title/?companies=co0284770&start=51&ref_=adv_nxt',
        'https://www.imdb.com/search/title/?companies=co0284770&start=101&ref_=adv_nxt',
            ]

Impossible_pictures = [

        'https://www.imdb.com/search/title/?companies=co0111305',
        'https://www.imdb.com/search/title/?companies=co0111305&start=51&ref_=adv_nxt',

            ]

Oxford_film_urls = [

        'https://www.imdb.com/search/title/?companies=co0081846',
        'https://www.imdb.com/search/title/?companies=co0081846&start=51&ref_=adv_nxt',
        'https://www.imdb.com/search/title/?companies=co0081846&start=101&ref_=adv_nxt',
            ]


Lion_TV_urls = [

        'https://www.imdb.com/search/title/?companies=co0103830',
        'https://www.imdb.com/search/title/?companies=co0103830&start=51&ref_=adv_nxt',
        'https://www.imdb.com/search/title/?companies=co0103830&start=101&ref_=adv_nxt',
        'https://www.imdb.com/search/title/?companies=co0103830&start=151&ref_=adv_nxt',
        'https://www.imdb.com/search/title/?companies=co0103830&start=201&ref_=adv_nxt',

        ]

    # I need the production Name and the dirrect. 

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
   

Company_list_strings = ['Plumb_Pictures_Urls','Impossible_pictures','Oxford_film_urls', 'Lion_TV_urls' ] 


Company_dict = {'Plumb_Pictures_Urls': Plumb_Pictures_Urls,'Impossible_pictures':Impossible_pictures, 'Oxford_film_urls':Oxford_film_urls,'Lion_TV_urls': Lion_TV_urls } 


for name in Company_list_strings:
    print('Company Name:', name)
    urls = Company_dict[name]
    for i in urls:
        D = getIMDB_Dirrectors_Titles(i)
        time.sleep(5)
