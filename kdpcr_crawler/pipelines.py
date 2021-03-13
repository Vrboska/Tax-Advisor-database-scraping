# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from logging import log
from sqlite3 import dbapi2 as sqlite

class KdpcrCrawlerPipeline:
    def process_item(self, item, spider):
        return item
    
    
class scrapeDatasqLitePipeline(object):
    def __init__(self):
        # Possible we should be doing this in spider_open instead, but okay
        self.connection = sqlite.connect('./tax_advisors.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS tax_advisors')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tax_advisors ' \
                    '(name VARCHAR(256) PRIMARY KEY, location VARCHAR(80), phone_number VARCHAR(80)'\
                    ',email_address VARCHAR(1028))')

    # Take the item and put it in database - do not allow duplicates
    def process_item(self, item, spider):
        self.cursor.execute("select * from tax_advisors where name=?", (item['name'],))
        result = self.cursor.fetchone()
        if result:
            pass#log.msg("Item already in database: %s" % item, level=log.DEBUG)
        else:
            self.cursor.execute(
                "insert into tax_advisors (name, location, phone_number, email_address) values (?, ?, ?, ?)",
                    (item['name'], item['location'], item['phone_number'], item['email_address']))

            self.connection.commit()

            #log.msg("Item stored : " % item, level=log.DEBUG)
        return item

    def handle_error(self, e):
        log.err(e)
