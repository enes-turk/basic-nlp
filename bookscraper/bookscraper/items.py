# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field # object to indacate in fields in the item


class BookscraperItem(scrapy.Item):
    title = Field()
    price = Field()
    upc = Field() # unique produc id
    image_url = Field()
    url = Field()
    
