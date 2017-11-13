from pymongo import MongoClient
from config import *
from flask import jsonify
import traceback
import json
import datetime
# from utils import scraper_csv_file
from bson import ObjectId


#############################################
#                                           #
#                                           #
#              DATABASE CLASS               #
#                                           #
#                                           #
#############################################
class Mdb:

    def __init__(self):
        # local db
        conn_str = "mongodb://%s:%s@%s:%d/%s" \
             % (DB_USER, DB_PASS, DB_HOST, DB_PORT, AUTH_DB_NAME)
        # conn_str = 'mongodb://scrapuser:scrappass@ds257495.mlab.com:57495/scrap_utils'
        client = MongoClient(conn_str)
        self.db = client['scrap_utils']

    def indeed_scraper_data(self, title, location, sal, summary):
        try:
            rec= {
                'title': title,
                'location': location,
                'sal': sal,
                'summary': summary
            }
            self.db.indeed.insert(rec)
        except Exception as exp:
            print('[IndeedScraper] :: indeed_scraper_data() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def get_indeed_data(self):
        result = self.db.indeed.find()
        ret = []
        for data in result:
            ret.append(data)
        return ret

    def overstock_scraper_data(self, price, title, rating):
        try:
            rec = {
                'price': price,
                'title': title,
                'rating': rating,
            }
            self.db.overstock.insert(rec)
        except Exception as exp:
            print('[OverStockScraper] :: overstock_scraper_data() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def get_overstock_data(self):
        result = self.db.overstock.find()
        ret = []
        for data in result:
            ret.append(data)
        return ret

    def bedbathandbeyond_scraper_data(self, title, price):
        try:
            rec= {
                'title': title,
                'price': price
            }
            self.db.bedbathandbeyond.insert(rec)
        except Exception as exp:
            print('[BedBathAndBeyond] :: bedbathandbeyond_scraper_data() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def get_bedbathandbeyond_data(self):
        result = self.db.bedbathandbeyond.find()
        ret = []
        for data in result:
            ret.append(data)
        return ret

    def google_news_data(self, headlines, subheadline):
        try:
            rec = {
                'headlines': headlines,
                'subheadline': subheadline
            }
            self.db.googlenews.insert(rec)
        except Exception as exp:
            print('[GoogleNewsScraper] :: google_news_data() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def get_google_news_data(self):
        result = self.db.googlenews.find()
        ret = []
        for data in result:
            ret.append(data)
        return ret

    def homedepot_data(self, model, price, stock):
        try:
            rec = {
                'model': model,
                'price': price,
                'stock': stock
            }
            self.db.homedepot.insert(rec)
        except Exception as exp:
            print('[HomeDepotScraper] :: homedepot_data() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def get_homedepot_data(self):
        result = self.db.homedepot.find()
        ret = []
        for data in result:
            ret.append(data)
        return ret

    def samsclub_data(self, name, rating, price, save_price):
        try:
            rec = {
                'name': name,
                'rating': rating,
                'price': price,
                'save_price': save_price
            }
            self.db.samsclub.insert(rec)
        except Exception as exp:
            print('[SamsClubScraper] :: samsclub_data() :: Got exception: %s' % exp)
            print(traceback.format_exc())

    def get_samsclub_data(self):
        result = self.db.samsclub.find()
        ret = []
        for data in result:
            ret.append(data)
        return ret

if __name__ == '__main__':
    mdb = Mdb()

