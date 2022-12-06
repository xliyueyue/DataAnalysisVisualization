# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

class ExampleSpider(scrapy.Spider):
    name = 'example_jh_g'
    allowed_domains = ['class.hujiang.com']
    # 高中
    start_urls = []
    for page in range(1, 9):
        start_urls.append('https://class.hujiang.com/category/118?a=true&p=' + str(page))

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
            elif "物理" in item["course_name"]:
                item["course_name"] = "物理"
            elif "化学" in item["course_name"]:
                item["course_name"] = "化学"
            elif "生物" in item["course_name"]:
                item["course_name"] = "生物"
            else:
                item["course_name"] = "联报"

            item["grade"] = li.xpath("./div/div[2]/div/a[1]/span/text()").extract_first()
            if "高一" in item["grade"]:
                item["grade"] = "高一"
            elif "高二" in item["grade"]:
                item["grade"] = "高二"
            elif "高三" in item["grade"]:
                item["grade"] = "高三"
            else:
                item["grade"] = "高三"

            item["price"] = li.xpath("./div/div[2]/p/span/span[2]/text()").extract_first()

            item["textbook"] = li.xpath("./div/div[2]/div/a[1]/span/text()").extract_first()
            if "人教" in item["textbook"]:
                item["textbook"] = "人教"
            elif "沪教" in item["textbook"]:
                item["textbook"] = "沪教"
            else:
                item["textbook"] = "全国通用"

            yield item
