# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Diemthidaihoc2021Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    w_math = scrapy.Field()
    w_literature = scrapy.Field()
    w_foreign_language = scrapy.Field()
    x_physics = scrapy.Field()
    x_chemistry = scrapy.Field()
    x_biology = scrapy.Field()
    y_history = scrapy.Field()
    y_geography = scrapy.Field()
    y_civic_education = scrapy.Field()
    z_average = scrapy.Field()
    z_max = scrapy.Field()
    z_min = scrapy.Field()