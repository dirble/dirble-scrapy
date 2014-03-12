# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirble.spiders']
NEWSPIDER_MODULE = 'dirble.spiders'
DEFAULT_ITEM_CLASS = 'dirble.items.Song'

ITEM_PIPELINES = {
    'dirble.pipelines.SaveToDb':300
}
