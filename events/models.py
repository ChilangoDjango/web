from django.db import models

from places.models import Place

class Event(models.Model):
	name = models.CharField(max_length=1000)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	place = models.ForeignKey(Place)