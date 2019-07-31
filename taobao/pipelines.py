# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class TaobaoPipeline(object):
    def process_item(self, item, spider):

        headers = ['aliMallSeller','anony','appendComment','attributes','attributesMap','aucNumId','auctionPicUrl','auctionSku','buyCount','carServiceLocation','cmsSource','displayRatePic','displayRateSum','displayUserLink','displayUserNick','displayUserNumId','displayUserRateLink','dsr','fromMall','fromMemory','gmtCreateTime','goldUser','headExtraPic','id','memberIcon','pics','picsSmall','position','rateContent','rateDate','reply','sellerId','serviceRateContent','structuredRateList','tamllSweetLevel','tmallSweetPic','tradeEndTime','useful','userIdEncryption','userInfo','userVipLevel','userVipPic']


        with open('comments.csv','a',newline='',encoding='utf-8') as fp:
            writer = csv.DictWriter(fp,headers)
            writer.writeheader()
            writer.writerows(item['comment_dict'])
        return item
