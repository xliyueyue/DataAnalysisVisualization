# -*- coding: utf-8 -*-
import scrapy
import re
from myspider.items import MyspiderItem

class ExampleSpider(scrapy.Spider):
    name = 'example_jh_x'
    allowed_domains = ['class.hujiang.com']
    start_urls = []
    # 小学
    for page in range(1, 7):
        start_urls.append('https://class.hujiang.com/category/116?a=true&p=' + str(page))

    def parse(self, response):
        li_list = response.xpath('//*[@id="listData"]/ul/li')
        for li in li_list:
            item = MyspiderItem()
            item["course_name"] = li.xpath("./div/div[2]/div/a[1]/span/text()").extract_first()
            if "语文" in item["course_name"]:
                item["course_name"] = "语文"
            elif "数学" in item["course_name"]:
                item["course_name"] = "数学"
            elif "英语" in item["course_name"]:
                item["course_name"] = "英语"
            else:
                item["course_name"] = "联报"

            item["grade"] = li.xpath("./div/div[2]/div/a[1]/span/text()").extract_first()
            if "一年级" in item["grade"]:
                item["grade"] = "一年级"
            elif "二年级" in item["grade"]:
                item["grade"] = "二年级"
            elif "三年级" in item["grade"]:
                item["grade"] = "三年级"
            elif "四年级" in item["grade"]:
                item["grade"] = "四年级"
            elif "五年级" in item["grade"]:
                item["grade"] = "五年级"
            elif "六年级" in item["grade"]:
                item["grade"] = "六年级"
            else:
                item["grade"] = "六年级"

            item["price"] = li.xpath("./div/div[2]/p/span/span[2]/text()").extract_first()

            yield item
