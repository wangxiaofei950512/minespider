# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MinespiderPipeline(object):
    def process_item(self, item, spider):
        with open("/Users/admin/wang/Socialpeta2.0/minespider/minespider/logs/my_meiju.txt", 'a', encoding='utf-8') as fp:
            fp.write(item['name'] + '\n')


