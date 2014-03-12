from scrapy.spider import Spider
from scrapy.selector import Selector

from dirble.items import Song


class NRKMP3Spider(Spider):
    name = "NRKMp3"
    allowed_domains = ["nrk.no"]
    start_urls = [
        "http://www.nrk.no/mp3/",
    ]

    # This takes care of the stationid so you don't need to think about that.
    # Just send in the station id when you do a pull-request
    # You find the station id on station page and under contribute, you will see the id in the url.
    def __init__(self, stationid=''):
        self.station_id = stationid

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.nrk.no/mp3/
        @scrapes NRKMP3
        """
        sel = Selector(response)
        songs = sel.xpath('//*[@id="wrapper"]/div[3]/div[2]/div/table/tbody/tr[1]/td/span/text()').extract()
        
        items = []
        
        # After the songs changes i'm not sure if for is needed.
        for song in songs:
            print song
            songname = song.split(' - ')
            item = Song()
            item['artist'] = songname[0]
            item['song'] = songname[1]
            item['station_id'] = self.station_id
            items.append(item)

        return items
