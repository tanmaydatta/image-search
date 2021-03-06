from django.core.management import BaseCommand
import requests
import json
from search.image_module import *
from search.models import *

    #The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
# Show this when the user types help
    help = "Syncing data to algolia"

    # A command must define handle()
    def handle(self, *args, **options):
		self.stdout.write("Inserting image data in algolia")
		images = ImageTagMap.objects.all()
		tags = set([])
		count = 0
		for img in images:
			img.save()
			tags.add(img.tag)
			count = count + 1
			print count
		add_tags(tags)

