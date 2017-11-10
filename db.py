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

        client = MongoClient(conn_str)
        self.db = client['heroku_188g0kct']
        # self.db = client['webappdb'] # local db

    def indeed_scraper_data(self, title, location, sal, summary):
        try:
            rec= {
                'title': title,
                'location': location,
                'sal': sal,
                'summary': summary
            }
            self.db.indeed(rec)
        except Exception as exp:
            print '[IndeedScraper] :: Indeed_scraper_data() :: Got exception: %s' % exp
            print(traceback.format_exc())

    def google_news_data(self, headlines, subheadline):
        try:
            rec = {
                'headlines':headlines,
                'subheadline': subheadline
            }
            self.db.googlenews.insert(rec)
        except Exception as exp:
            print '[GoogleNewsScraper] :: google_news_data() :: Got exception: %s' % exp
            print(traceback.format_exc())

if __name__ == '__main__':
    mdb = Mdb()
