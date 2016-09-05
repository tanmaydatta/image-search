from __future__ import unicode_literals

from django.db import models
from image_module import *

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=1500)

    def create(self):
        tags = get_tags(self.url)
        add_tags(tags[:4])
        self.save(tags[:4])

    def save(self, tags):
    	super(Image, self).save()
    	for tag in tags:
    		img_map = ImageTagMap(image=self, tag=tag)
    		img_map.save()

    def delete(self):
        map_data = self.imagetagmap_set.all()
        for obj in map_data:
            obj.delete()
        super(Image, self).delete()

class ImageTagMap(models.Model):
    image = models.ForeignKey(Image)
    tag = models.CharField(max_length=50)

    def save(self):
        super(ImageTagMap, self).save()
        # sync to algolia
        create_or_update(self)

    def delete(self):
    	id = self.id
    	super(ImageTagMap, self).delete()
    	# remove from algolia
    	delete_record(id)
