# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()                # 职位名称
    workLocation = scrapy.Field()        # 工作地点
    catalog = scrapy.Field()             # 职位类别
    money = scrapy.Field()                # 薪资水平
    demand = scrapy.Field()                # 要求
    skillLabel = scrapy.Field()            # 技能标签
    publishTime = scrapy.Field()         # 发布时间
    company = scrapy.Field()             # 公司名称
    companyField = scrapy.Field()          # 公司服务领域
    companyLabelList = scrapy.Field()      # 公司简介
    positionAdvantage = scrapy.Field()     # 职位福利
    detailLink = scrapy.Field()          # 职位详情页链接
    detailCompany = scrapy.Field()         # 公司详情页链接
