from scrapy.exceptions import DropItem
import json

class SaveToDb(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
    
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
