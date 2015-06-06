from django.db import models
# from djangotoolbox.fields import ListField

# Create your models here.
class Tweets(models.Model):
	tweet = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True, null=True)

class Keyword(models.Model):
	keyword = models.CharField(max_length=64)
	count = models.IntegerField()
	notable = models.CharField(max_length=64)

