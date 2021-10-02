## Helper script to update the urls on the postgres database to new ones, using a json file.
#
#  Both the base_url for each recipe, and the img_url require updating to the latest values.
#  The db_string value needs to be set from postgres database credentials on heroku.
#  
#  recipes_bbcgf_new.json - contains the full recipes, which links the new_urls to the new img_urls.
#  url_pairs_temp.json    - contains the old and new main url pairs as old_url, new_url. 


import json
from multiprocessing.pool import ThreadPool

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData


class Updater:
    def __init__(self, db_string):
        self.db = create_engine(db_string)   
        meta = MetaData(self.db)
        self.recipe_table = Table('recipe', meta,  
                        Column('url', String),
                        Column('img_url', String))

    def _process_url(self, url_pair):
        json_old_url = url_pair['old_url']
        json_new_url = url_pair['new_url']

        with self.db.connect() as conn:
            update_statement = self.recipe_table.update().where(self.recipe_table.c.url==json_old_url).values(url = json_new_url)
            conn.execute(update_statement)
        return None

    def _process_img_url(self, json_recipe):
        json_url = json_recipe['URL']
        json_img_url = json_recipe['img_URL']

        with self.db.connect() as conn:
            update_statement = self.recipe_table.update().where(self.recipe_table.c.url==json_url).values(img_url = json_img_url)
            conn.execute(update_statement)
        return None
    
    def _load_to_threadpools(self, function, jsonfile_name):
        with open(jsonfile_name, encoding='UTF-8') as json_file:
            data_to_process = json.load(json_file)

        pool = ThreadPool(8)
        _ = pool.map(function, data_to_process)

        pool.close()
        pool.join()

    # Primary functions to be called in script
    def update_urls(self, jsonfile_name):
        self._load_to_threadpools(self._process_url, jsonfile_name)

    def update_img_urls(self, jsonfile_name):
        self._load_to_threadpools(self._process_img_url, jsonfile_name)


if __name__ == '__main__':

    db_string = "postgresql://string"
    updater = Updater(db_string)

    print("Updating main urls..")
    updater.update_urls('url_pairs_temp.json')

    print("Updating image urls..")
    updater.update_img_urls('recipes_bbcgf_new.json')
