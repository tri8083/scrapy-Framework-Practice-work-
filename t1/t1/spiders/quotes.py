import scrapy
from scrapy import item
from ..items import T1Item

class quotesspider(scrapy.Spider):
    name = 'data'
    start_urls = [ 
        
        'https://quotes.toscrape.com/' 
    
    
    ] 
#**************************************TAST(1)create Collection with 2 field(tag_name and tags_value)*****************************************************************************
    # def parse(self, response):

    #     items = T1Item()
    #     all_data = response.css('div.quote')

        
    #     tag_name = all_data.css('.tag::text').extract()
    #     tag_value = all_data.css('div.tags a').xpath('@href').extract()


    #     items['tag_name'] = tag_name
    #     items['tag_value'] = tag_value


    #     yield items

#**************************************END TASK 1********************************************************************






#***********************************TASK 2 Scrap all tags from Quotes to Scrape**************************************
    # def parse(self, response):
    #     items = T1Item()
    #     all_data = response.css('div.quote')

    #     tag = all_data.css(".tag::text").extract()

    #     items['tag'] =tag

    #     yield items

#**************************************END TASK 2********************************************************************




#***********************************TASK 3 - Scrape quotes from Quotes to Scrape website - **************************

    # def parse(self, response):
    #         items = T1Item()
    #         quotes = response.css('span.text::text').getall()
    #         items['quotes'] =quotes

    #         yield items

#*********************************** END TASK 3  - **************************








