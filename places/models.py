from django.db import models

class Place(models.Model):
	name = models.CharField(max_length=500)
	latitude = models.IntegerField(default=0)
	longitude = models.IntegerField(default=0)
	facebook = models.URLField(null=True)
	twitter = models.URLField(null=True)
	site = models.URLField(null=True)