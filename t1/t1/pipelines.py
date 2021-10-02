# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


import pymongo
class T1Pipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient (
             'localhost',
              27017
            )
        db = self.conn['mydatabase']

        #**************TAST(1)*****************create table quotes_tb1
        #self.collection = db['quotes_tb1']
        #***************END TASK 1*************


        #**************TAST(2)*****************
        # self.collection = db['all_tags']
        #**************END TAST(2)*************



         #**************TAST(3)*****************
        self.collection = db['quotes']
         #**************End TAST(3)*****************

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
