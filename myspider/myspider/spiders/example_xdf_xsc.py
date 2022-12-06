# -*- coding: utf-8 -*-
import scrapy
import re
from myspider.items import MyspiderItem


class ExampleSpider(scrapy.Spider):
    name = 'example_xdf_xsc'
    allowed_domains = ['souke.xdf.cn']

    # 小升初阶段
    start_urls = []
    for page in range(1, 50):
        start_urls.append('http://souke.xdf.cn/MiddleSchool-1.html?attr=1041&page=' + str(page))

    def parse(self, response):
        for page in range(1, 21, 2):
            li_list = response.xpath('/html/body/div[6]/div[1]/div[' + str(page) + ']')
            for li in li_list:
                item = MyspiderItem()

                item["price"] = int(li.xpath('./div[3]/div/span/text()').extract_first())
                if item["price"] == 1:
                    continue

                item["course_name"] = li.xpath('./div[2]/h3/a/text()').extract_first()
                if "语文" in item["course_name"]:
                    item["course_name"] = "语文"
                elif "数学" in item["course_name"]:
                    item["course_name"] = "数学"
                elif "英语" in item["course_name"]:
                    item["course_name"] = "英语"
                elif "科学" in item["course_name"]:
                    item["course_name"] = "科学"
                else:
                    item["course_name"] = "联报"

                item["grade"] = li.xpath('./div[2]/h3/a/text()').extract_first()
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

                item["type"] = li.xpath('./div[2]/h3/span/text()').extract_first()
                item["type1"] = li.xpath('./div[2]/h3/span[2]/text()').extract_first()
                if item["type1"] is not None:
                    item["type"] = item["type1"]

                item["period"] = li.xpath('./div[2]/p[1]/text()').extract()[1]
                if '课次' in item["period"]:
                    item["period"] = item["period"].split("课次")[1].replace("/", "").replace("课时\r\n", "").replace(" ", "")

                yield item
