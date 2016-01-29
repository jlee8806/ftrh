from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

class user(models.Model):
	username = models.CharField(max_length=15)
	email = models.EmailField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	steamusername = models.CharField(max_length=30, blank=True)

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)
class game(models.Model):

	title = models.CharField(max_length=40)
	image = models.ImageField(upload_to = upload_location, null=True, blank=True, height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	video = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	linearity = models.IntegerField(default = 0)
	replayability = models.IntegerField(default = 0)
	learning_curve = models.IntegerField(default = 0)
	story = models.IntegerField(default = 0)
	sound = models.IntegerField(default = 0)
	graphic_dependency = models.IntegerField(default = 0)
	review = models.TextField(max_length=1000)

	def get_absolute_url(self):
		return reverse("games:detail", kwargs={'id': self.id})
