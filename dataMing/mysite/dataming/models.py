from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=50)

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	dataSource = models.IntegerField()
	levelOneClassType = models.IntegerField()
	sentimentType = models.IntegerField()
	labeled = models.BooleanField()
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)


