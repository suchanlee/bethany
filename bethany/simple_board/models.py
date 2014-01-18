from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=250, blank=True)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name


class Post(models.Model):
	board = models.ForeignKey(Board)
	title = models.CharField(max_length=250)
	author = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	views = models.IntegerField(blank=True, null=True, default=0)


	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title


# class Comment(models.Model):
# 	author = models.ForeignKey(User)
# 	post = models.ForeignKey(Post)
# 	text = models.TextField()
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
