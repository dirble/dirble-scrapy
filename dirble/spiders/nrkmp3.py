from scrapy.spider import Spider
from scrapy.selector import Selector

from dirble.items import Song


class NRKMP3Spider(Spider):
    name = "NRKMp3"
    allowed_domains = ["nrk.no"]
    start_urls = [
        "http://www.nrk.no/mp3/",
    ]

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

        for song in songs:
            print song
            songname = song.split(' - ')
            item = Song()
            item['artist'] = songname[0]
            item['song'] = songname[1]
            item['station_id'] = 3421
            items.append(item)

        return items
