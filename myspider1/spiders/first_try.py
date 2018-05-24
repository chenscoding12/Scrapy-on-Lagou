# -*- coding: UTF-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import json
from myspider1.items import Myspider1Item
from time import sleep

# class FirstToWebSpider(scrapy.Spider):
#     name = "ToWeb58"
#     start_urls = [
#         "http://bj.58.com/chuzu/",
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.des'):
#             yield {
#                 'title': quote.css('h2 > ::text').extract_first(),
#                 'type': quote.css('p.room::text').extract_first(),
#                 'location': quote.css('p.add > ::text').extract_first(),
#             }
#
#         next_page_url = response.css('div.pager a.next::attr(href)').extract_first()
#         if next_page_url is not None:
#             next_page_url = response.urljoin(next_page_url)
#             yield scrapy.Request(next_page_url, callback=self.parse)


# class FirstToWebSpider(scrapy.Spider):
#     name = "ToWebXC"
#     start_urls = [
#         "http://hotels.ctrip.com/hotel/beijing1#ctm_ref=ctr_hp_sb_lst",
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.hotel_new_list'):
#             yield {
#                 'name': quote.css('ul.hotel_item a::attr(title)').extract_first(),
#                 'score': quote.css('div.hotelitem_judge_box span.hotel_value::text').extract_first(),
#                 'location_tags&address': quote.css('p.hotel_item_htladdress ::text').extract(),
#                 'price': quote.css('div.hotel_price span.J_price_lowList::text').extract(),
#             }
#
#         next_page_url = response.css('div.page_box a.c_down::attr(href)').extract_first()
#         if next_page_url is not None:
#             next_page_url = response.urljoin(next_page_url)
#             yield scrapy.Request(next_page_url, callback=self.parse)


class FirstToWebSpider(scrapy.Spider):
    name = "ToWebLagou"
    start_urls = [
        "https://www.lagou.com/zhaopin/shujuwajue/28",
    ]

    def start_requests(self):
        url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
        requests = []

        for pn in range(1, 22):
            formdata = {'first': 'false',
                        'pn': str(pn),
                        'kd': '交互设计',
            }
            request = FormRequest(url, callback=self.parse, formdata=formdata)  # FormRequest函数(地址, 回调(使用的主要爬虫函数), 请求内容)
            requests.append(request)
            print(request)
        return requests

    # def after_login(self, response):
    #     for url in self.start_urls:
    #         yield self.make_requests_from_url(url)

    def parse(self, response):
        # for quote in response.css('li.con_list_item'):
        #     yield {
        #         'company': quote.css('div.company_name > a::text').extract_first(),
        #         'position': quote.css('div.position h3::text').extract_first(),
        #         'location': quote.css('span.add > ::text').extract_first(),
        #         'money': quote.css('span.money::text').extract_first(),
        #         # 'tags': quote.css('div.li_b_l').extract(),
        #     }

        # next_page_url = response.css('#s_position_list > div.item_con_pager > div > a:last-child::attr(href)').extract_first()
        # if next_page_url is not None:
        #     next_page_url = response.urljoin(next_page_url)
        #     yield scrapy.Request(next_page_url, callback=self.parse)

        print(response.body.decode())
        jsonBody = json.loads(response.body.decode())
        results = jsonBody['content']['positionResult']['result']
        items = []
        for result in results:
            item = Myspider1Item()
            item['name'] = result['positionName']
            item['workLocation'] = result['city']
            if result['district']:
                item['workLocation'] += result['district']
            if result['businessZones']:
                for zone in result['businessZones']:
                    item['workLocation'] += zone
                    # item['catalog']
            item['money'] = result['salary']
            item['demand'] = result['workYear'] + "/" + result['education']
            item['skillLabel'] = ",".join(result['positionLables'])
            item['positionAdvantage'] = result['positionAdvantage']
            item['publishTime'] = result['formatCreateTime']
            item['company'] = result['companyFullName']
            item['companyField'] = result['industryField']
            item['companyLabelList'] = ",".join(result['companyLabelList'])
            item['detailLink'] = "https://www.lagou.com/jobs/" + str(result['positionId']) + ".html"
            item['detailCompany'] = "https://www.lagou.com/gongsi/" + str(+result['companyId']) + ".html"
            items.append(item)
        return items

