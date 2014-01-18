from django.db import models

import pdb


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


class Notice(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	attachment = models.FileField(upload_to='notice/attachments/', blank=True)
	views = models.IntegerField(blank=True, null=True, default=0)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __unicode(self):
		return self.title


class IthacaLife(models.Model):
	content = models.TextField()


class KoreanSchool(models.Model):
	content = models.TextField()

