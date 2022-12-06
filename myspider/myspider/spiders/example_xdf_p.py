# -*- coding: utf-8 -*-
import scrapy

from myspider.items import MyspiderItem


class ExampleSpider(scrapy.Spider):
    name = 'example_xdf_p'
    allowed_domains = ['souke.xdf.cn']
    start_urls = []
    #小学阶段
    for page in range(1, 4):
        start_urls.append('http://souke.xdf.cn/search?cid=1&ccc=40&page=' + str(page))

    def parse(self, response):
        for page in range(1, 21, 2):
            li_list = response.xpath('/html/body/div[8]/div[1]/div[2]/div[' + str(page) + ']')
            for li in li_list:
                item = MyspiderItem()
                item["price"] = li.xpath('./div[1]/div/div/span/text()').extract_first()
                item["type"] = li.xpath('./div[1]/h2/span/i/text()').extract_first()
                if "住宿" in item["type"]:
                    item["type"] = "住宿"

                item["course_name"] = li.xpath('./div[1]/h2/a/text()').extract_first()
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

                item["grade"] = li.xpath('./div[1]/h2/a/text()').extract_first()

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

                yield item
