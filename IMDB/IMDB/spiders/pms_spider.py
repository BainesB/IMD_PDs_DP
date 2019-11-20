import scrapy 

# this one works. 

class PmsSpider(scrapy.Spider):
    name = "pms"
    start_urls = [
            'https://www.imdb.com/title/tt1777610/fullcredits?ref_=tt_ql_1',
    ]

    def parse(self, response):
        for pms in response.css('.listo'):   
            print('pms::::: response.css', pms)
            yield {

                    'Name': pms.css('a::text').getall(),
                    'Credit': pms.css('.credit::text').getall(), 
                }

# The names and the credits are seperated in two lists. I need to put them back together and work out how to do the crawl. 
# I need to work out how to junck everyone accept the PM's. 
    # might be ablet to create a dict and extract just the production manager 
# need to work out how to get in touch with them. 
 
# going to work out how to follow links. 
