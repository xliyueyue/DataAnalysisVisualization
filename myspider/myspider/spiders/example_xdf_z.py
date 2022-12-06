# -*- coding: utf-8 -*-
import scrapy
import re
from myspider.items import MyspiderItem

class ExampleSpider(scrapy.Spider):
    name = 'example_xdf_z'
    allowed_domains = ['souke.xdf.cn']
    start_urls = []
    #高中阶段
    for page in range(1, 100):
        start_urls.append('http://souke.xdf.cn/MiddleSchool-1.html?attr=935&page=' + str(page))
    # 初中阶段
    for page in range(1, 100):
        start_urls.append('http://souke.xdf.cn/MiddleSchool-1.html?attr=934&page=' + str(page))

    def parse(self, response):
        for page in range(1, 21, 2):
            li_list = response.xpath('/html/body/div[6]/div[1]/div[' + str(page) + ']')

            for li in li_list:
                item = MyspiderItem()

                item["type"] = li.xpath('./div[2]/h3/span/text()').extract_first()

                item["type1"] = li.xpath('./div[2]/h3/span[2]/text()').extract_first()
                if item["type1"] is not None:
                    item["type"] = item["type1"]

                item["period"] = li.xpath('./div[2]/p[1]/text()').extract()[1]
                if '课次' in item["period"]:
                    item["period"] = item["period"].split("课次")[1].replace("/", "").replace("课时\r\n", "").replace(" ",
                                                                                                                  "")
                item["price"] = int(li.xpath('./div[3]/div/span/text()').extract_first())
                if item["price"] == 1:
                    continue

                item["course_name"] = li.xpath('./div[2]/h3/a/text()').extract_first()
                english = '英语|听力|词汇|口语'
                if "语文" in item["course_name"]:
                    item["course_name"] = "语文"
                elif "数学" in item["course_name"]:
                    item["course_name"] = "数学"
                elif re.search(english, item["course_name"]):
                    item["course_name"] = "英语"
                elif "物理" in item["course_name"]:
                    item["course_name"] = "物理"
                elif "化学" in item["course_name"]:
                    item["course_name"] = "化学"
                elif "生物" in item["course_name"]:
                    item["course_name"] = "生物"
                elif "历史" in item["course_name"]:
                    item["course_name"] = "历史"
                elif "政治" in item["course_name"]:
                    item["course_name"] = "政治"
                elif "地理" in item["course_name"]:
                    item["course_name"] = "地理"
                else:
                    item["course_name"] = "联报"

                item["grade"] = li.xpath('./div[2]/h3/a/text()').extract_first()
                a = "初中|初一|初二|中考|初三"
                b = "高中|高一|高二|高考|高三"
                if re.search(a, item["grade"]):
                    if "初一" in item["grade"]:
                        item["grade"] = "初一"
                    elif "初二" in item["grade"]:
                        item["grade"] = "初二"
                    elif "初三" in item["grade"]:
                        item["grade"] = "初三"
                    else:
                        item["grade"] = "初三"
                elif re.search(b, item["grade"]):
                    if "高一" in item["grade"]:
                        item["grade"] = "高一"
                    elif "高二" in item["grade"]:
                        item["grade"] = "高二"
                    elif "高三" in item["grade"]:
                        item["grade"] = "高三"
                    else:
                        item["grade"] = "高三"

                yield item
