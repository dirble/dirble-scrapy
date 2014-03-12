dirble-scrapy
=============

This is the project where we collect all the radio stations we scrape the song information from.

Scraper
-------
We use this scrapers to get song information from radio station’s websites.

When a scraper will be used for a station the default streamscrobbler scraper will be switched off for that station and it will just use this scraper.



pull-requests
-------------
If you want to add a scraper for a station you can’t find song-information for, you can fork the develop branch and create a new spider with the NRKMP3 template. You need to use the Song item. Make a pull-request of the spider file and I will accept it after it have been tested.