# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class MyspiderPipeline(object):

    def process_item(self, item, spider):
        with open("K12_edu_data/xdf_high_school.txt", "a", encoding='utf-8') as f:
            # xdf_high_school.txt    xdf_primary_school.txt
            # jh_high_school.txt    jh_junior_high_school.txt   jh_primary_school.txt
            content = "{},{},{},{},{}\n".format(item["course_name"], item["grade"], item["price"], item["type"], item["period"])
            f.write(content)
#2020/4/11 至 2020/4/11 13:30-15:00 ,共计1课次 /1课时
