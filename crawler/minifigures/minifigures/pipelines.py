# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from minifigures.database_connector import  db_connector

class MinifiguresPipeline:
    def process_item(self, item, spider):
        db = db_connector()
        db.insert("mfs_tbl",item)

        return item
