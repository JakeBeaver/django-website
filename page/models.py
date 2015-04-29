from django.db import models

# Create your models here.

class posts(models.Model):
	body = models.CharField(max_length = 180)
	timestamp = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.username + ": " + self.body [0:20]
