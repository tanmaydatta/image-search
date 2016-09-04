from django.core.management import BaseCommand
import requests
import json
from search.image_module import *
from search.models import *

    #The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
# Show this when the user types help
    help = "Syncing data to mysql"

    # A command must define handle()
    def handle(self, *args, **options):
		self.stdout.write("Inserting image data in mysql")
		count = 0
		x = set([])
		for i in range(4):
			f = open("search/image_jsons/" + str(i+1) + ".json")
			json_obj = json.loads(f.read())
			for image in json_obj['data']:
				count = count + 1
				if count < 1495:
					continue
				url = image['assets']['preview']['url']
				try:
					tags = get_tags(url)
				except:
					tags = []
					print "error in tags " + str(count) 
					pass
				for tag in tags[:4]:
					x.add(tag)
				name = url.split('/')[-1]
				try:
					img = Image(name=name, url=url)
					img.save(tags[:4]) # only 4 tags per image beacuse free account only gives max 10000 records
				except:
					print "error in" + str(count+1)
					pass
				print count
			print 500*(i+1)
