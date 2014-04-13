import os, datetime

from django.db import models

import pdb


class Slideshow(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	image = models.FileField(upload_to='slide_images/')


class Sermon(models.Model):
	link = models.URLField()
	title = models.CharField(max_length=250)
	bible_verses = models.CharField(max_length=100)
	preacher = models.CharField(max_length=100, blank=True)
	date = models.DateTimeField()
	embed = models.CharField(max_length=500, blank=True)
	thumbnail = models.URLField(blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __unicode(self):
		return self.title

	def save(self, *args, **kwargs):
		'''
		Get and save the embed code
		'''
		try:
			vid_id = self.link.split('watch?v=')[1]
			self.embed = '<iframe class="sermon-embed" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen></iframe>'.format(vid_id)
			self.thumbnail = 'http://img.youtube.com/vi/{}/hqdefault.jpg'.format(vid_id)
		except:
			print 'Sermon save failed'

		super(Sermon, self).save(*args, **kwargs)


def get_upload_path(instance, filename):
	return os.path.join('notice/attachments', '{}'.format(filename.encode('ascii', 'ignore')))


class Notice(models.Model):
	notice_type = models.CharField(max_length=25)
	title = models.CharField(max_length=250)
	content = models.TextField()
	attachment = models.FileField(upload_to=get_upload_path, blank=True)
	views = models.IntegerField(blank=True, null=True, default=0)
	created = models.DateTimeField(blank=True, null=True)

	class Meta:
		ordering = ['-created']

	def __unicode(self):
		return self.title

	def save(self, *args, **kwargs):
		# add created datetime
		if not self.created:
			self.created = datetime.datetime.now()

		super(Notice, self).save(*args, **kwargs)


class IthacaLife(models.Model):
	content = models.TextField()


class KoreanSchool(models.Model):
	content = models.TextField()


class Interview(models.Model):
	major = models.CharField(max_length=100)
	college = models.CharField(max_length=50)
	grad_year = models.CharField(max_length=4)
	q1 = models.TextField()
	q2 = models.TextField()
	q3 = models.TextField()
	q4 = models.TextField()
	q5 = models.TextField()
	q6 = models.TextField()




