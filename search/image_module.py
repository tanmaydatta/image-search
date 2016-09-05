from algoliasearch import algoliasearch
from artifacia.settings import *
import requests
import ipdb

client = algoliasearch.Client(APP_ID, API_KEY)
index = client.init_index("images")
tag_index = client.init_index("tags")

def create_or_update(image):
	index.save_object({"tag": image.tag, 
                  "id": image.id, 
                  "url": image.image.url,
                  "objectID": image.id})

def delete_record(id):
	index.delete_object(id)

def get_tags(url):
	url = "https://api.clarifai.com/v1/tag/?url=" + url + "&access_token=" + ACCESS_TOKEN
	res = requests.get(url).json()
	return res['results'][0]['result']['tag']['classes']

def add_tags(tags):
	for tag in tags:
		tag_index.add_object({"tag": tag})

def get(query, page=0, rows=6):
	res = index.search(query,{"page":page, "hitsPerPage":rows})
	return res['hits']