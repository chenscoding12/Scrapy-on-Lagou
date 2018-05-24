# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
import json

class Myspider1Pipeline(object):

    def __init__(self):
        self.workbook = Workbook()
        self.ws = self.workbook.active
        self.ws.append(['职位名称', '工作地点', '薪资水平', '要求', '技能标签', '发布时间','公司名称','公司服务领域','公司简介','职位福利','职位详情页链接','公司详情页链接'])  # 设置表头
        # self.file = codecs.open('tencent.json','w', encoding='utf-8')

    def process_item(self, item, spider):
        line = [item['name'], item['workLocation'],item['money'], item['demand'], item['skillLabel'],
                item['publishTime'],item['company'],item['companyField'],item['companyLabelList'],item['positionAdvantage'],item['detailLink'],item['detailCompany']]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.workbook.save('lagoujobzd1.xlsx')  # 保存xlsx文件
        #line = json.dumps(dict(item), ensure_ascii=False)+ "\n"
        #self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

