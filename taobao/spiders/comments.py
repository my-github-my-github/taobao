# -*- coding: utf-8 -*-
import scrapy
import re
import json
from taobao.items import CommentItem


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['taobao.com','tmall.com']
    start_urls = ['https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D&commend=all']

    def parse(self, response):
        text = response.text
        detail_urls = re.findall(r'"detail_url":"(.+?)"', text)
        detail_urls = list(map(lambda x: x.encode('utf-8').decode('unicode_escape'), detail_urls))
        new_detail_urls = list(map(lambda x: "https:" + x, detail_urls[1:]))
        new_detail_urls.append(detail_urls[0])
        for new_detail_url in new_detail_urls:
            if 'detail.tmall' in new_detail_url:
                request = scrapy.Request(url=new_detail_url,callback=self.establish_url)
                yield request

    def establish_url(self,response):
        text = response.text

        spuId = re.findall(r'.*"spuId":(\d+).*', text)[0]
        itemId = re.findall(r'.*"itemId":(\d+).*', text)[0]
        userId = re.findall(r'.*"userId":"(\d+)".*', text)[0]
        comment_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=%s&spuId=%s&sellerId=%s&order=3&currentPage=%d' % (itemId, spuId, userId, 1)
        request = scrapy.Request(url=comment_url,callback=self.parse_json)
        yield request

    def parse_json(self,response):
        text = response.text
        json_str = re.findall(r'jsonp\d+\((.*)\)', text)[0]
        comments_dict = json.loads(json_str,encoding='utf-8')
        comments = comments_dict['rateDetail']['rateList']
        print(type(comments))
        item = CommentItem(comment_dict=comments)
        print('插入一条')
        yield item
