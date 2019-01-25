# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
class LyricsPipeline(object):
    def process_item(self, item, spider):
        if '-' in item['content']:
            item['content'] = item['content'].replace('-','')
        return item

class DuplicatesTitlePipeline(object):
    def __init__(self):
        self.songs = set()
    def process_item(self, item, spider):
        title = item['title'] 
        if title in self.songs:
            raise DropItem('duplicates title found %s', item)
        self.songs.add(title)
        return(item)