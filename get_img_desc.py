from random import random
import time
from requests import get
from bs4 import BeautifulSoup
from tqdm import tqdm

from app import db, Recipe

request_headers = {
    "User-Agent": 'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)'
}

recipes = db.session.query(Recipe).all()

updated_recipes = []

for recipe in tqdm(recipes):
    if recipe.img_file == None or recipe.desc == None:
        try:
            res = get(recipe.url, headers=request_headers)
        except:
            print('failed to get res for ' + recipe.url)
        else:
            soup = BeautifulSoup(res.content,"html.parser") 

            #get image
            if recipe.img_file == None:
                try:
                    img_url = soup.find('div', attrs={'class':'recipe-header__media'}).div.img['src']
                except:
                    print('Error getting img_url from ' + recipe.url)
                    img_url = None
                else:
                    img_file = './static/img/' + str(recipe.id) + '.jpg'
                    try:
                        img = get('http:' + img_url, headers=request_headers)
                    except:
                        print('failed to get res for ' + img_url)
                    else:
                        with open(img_file, 'wb') as f:
                            f.write(img.content)
                        recipe.img_file = img_file
                        db.session.commit()
            #get desc
            if recipe.desc == None:
                try:
                    desc = soup.find('div', attrs={'class':'recipe-header__description'}).contents[0].get_text()
                except:
                    print('Error getting desc from ' + recipe.url)
                else:
                    recipe.desc = desc
                    db.session.commit()

    
    


