# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from project_name.database_connector import db_connector

class ProjectNamePipeline:
    def process_item(self, item, spider):
        conn = db_connector()
        conn.insert("authors",item)

        return item
