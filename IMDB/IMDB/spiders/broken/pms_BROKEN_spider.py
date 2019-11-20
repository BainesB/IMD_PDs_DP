# this one is broken. nothing goes in the doc. . 

import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class Pm2Spider(scrapy.Spider):
    name = 'pm2'
    allowed_domains = ['https://www.imdb.com/']
    start_urls = ['https://www.imdb.com/search/title/?companies=co0146284']

    # This is the first page of results for atlantics films.

    # This is the second page of results. 
    # https://www.imdb.com/search/title/?companies=co0146284&start=51&ref_=adv_nxt
    
    rules = (

        # Extract links matching 'some quality' (but not matching some other quality.)
        # and follow links from them means follow=True by default).
        Rule(LinkExtractor(allow=( 'https://www.imdb.com/title/tt*','https://www.imdb.com/title/tt*/fullcredits?ref_*', ),
            deny=('https://www.imdb.com/search/', ))),

        Rule(LinkExtractor(allow=('https://www.imdb.com/title/tt*','https://www.imdb.com/title/tt*/fullcredits?ref_*',)), callback='parse_item'),
            ) 
# my crawler is not doing anything. I don't know why. I think my regular expressions need working on in the shell. 
# I think you should look a regex book again to makes sure that the are not too open. 
# at the moment your parse_item function is not grabbing anything. 


    def parse_item(self, response):
        # follow links to the specific show. 
        for href in response.css('lister-item-header a::attr(href)'):
   
            for pms in response.css('.listo'):   
                yield {

                    'Name': pms.css('a::text').getall(), # this is grabbing the names. 
                    'Credit': pms.css('.credit::text').getall(), # this is grabbing the credits. 
                    }
