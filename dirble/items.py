from scrapy.item import Item, Field


class Song(Item):

    artist = Field()
    song = Field()
    station_id = Field()
