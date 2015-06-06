from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.
class Tweets(models.Model):
	tweet = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True, null=True)

