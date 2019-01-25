# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import LyricsItem
class HebeSpider(scrapy.Spider):
    name = 'hebe'
    allowed_domains = ['mojim.com']
    start_urls = ['http://mojim.com/twh109122.htm']

    def parse(self, response):
        source = BeautifulSoup(response.text,'lxml')
        hc3_tags = source.select('dd span.hc3 a')
        hc4_tags = source.select('dd span.hc4 a')
        all_a_tags = hc3_tags + hc4_tags
        for a in all_a_tags:
            meta = {
                'link':response.urljoin(a.get('href')),
                'title':a.text
            }
            yield scrapy.Request(meta['link'], callback=self.lyrics_parse, meta=meta)
    
    def lyrics_parse(self, response):
        item = LyricsItem()
        title = response.meta['title']
        source = BeautifulSoup(response.text, 'lxml')
        content = source.select_one('dl#fsZx1 dd.fsZx3').text.replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網','')
        want_delete_index = content.find('[') 
        content = content.replace(content[want_delete_index:], '')
        item['title'] = title
        item['content'] = content
        return item
            