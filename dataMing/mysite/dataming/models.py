from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	dataSource = models.IntegerField()
	levelOneClassType = models.IntegerField()
	sentimentType = models.IntegerField()
	labeled = models.BooleanField()
	username = models.CharField(max_length=30)


