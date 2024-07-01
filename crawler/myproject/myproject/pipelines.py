# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from myproject.database_connector import db_connector

class MyprojectPipeline:
    def remove_string(self,str):
        return ''.join(char for char in str if char.isdigit() or char=='.')


    def process_item(self, item, spider):
        # if spider.name == 'example':
        #     return item
            # raise DropItem("Skipping pipeline for spider: %s" % spider.name)


        adapter = ItemAdapter(item)
        adapter['price'] = self.remove_string(adapter['price'])
        # print("adapter------------------------------")
        # print(adapter)
        # print(item)
        conn = db_connector()
        rsl = conn.insert("books",item)
        print(rsl)
        return item
