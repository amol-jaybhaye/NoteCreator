from django.db import models

# Create your models here.
class Topic(models.Model):
	tagline = models.CharField(max_length=200)
	text = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)


	def _str_(self):
		return self.topic_name