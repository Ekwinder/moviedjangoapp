from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=300)
	desc = models.TextField(max_length=1000)
	rating = models.IntegerField(default= 0)

	def rate(self):
		self.rating = self.rating + 1

	def __unicode__(self):
		return self.title

