# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slideshow'
        db.create_table(u'website_slideshow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['Slideshow'])

        # Adding model 'Sermon'
        db.create_table(u'website_sermon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('bible_verses', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('preacher', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('embed', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Sermon'])

        # Adding model 'Notice'
        db.create_table(u'website_notice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Notice'])

        # Adding model 'IthacaLife'
        db.create_table(u'website_ithacalife', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'website', ['IthacaLife'])

        # Adding model 'KoreanSchool'
        db.create_table(u'website_koreanschool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'website', ['KoreanSchool'])

        # Adding model 'Interview'
        db.create_table(u'website_interview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('college', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('grad_year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('q1', self.gf('django.db.models.fields.TextField')()),
            ('q2', self.gf('django.db.models.fields.TextField')()),
            ('q3', self.gf('django.db.models.fields.TextField')()),
            ('q4', self.gf('django.db.models.fields.TextField')()),
            ('q5', self.gf('django.db.models.fields.TextField')()),
            ('q6', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'website', ['Interview'])


    def backwards(self, orm):
        # Deleting model 'Slideshow'
        db.delete_table(u'website_slideshow')

        # Deleting model 'Sermon'
        db.delete_table(u'website_sermon')

        # Deleting model 'Notice'
        db.delete_table(u'website_notice')

        # Deleting model 'IthacaLife'
        db.delete_table(u'website_ithacalife')

        # Deleting model 'KoreanSchool'
        db.delete_table(u'website_koreanschool')

        # Deleting model 'Interview'
        db.delete_table(u'website_interview')


    models = {
        u'website.interview': {
            'Meta': {'object_name': 'Interview'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grad_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'q1': ('django.db.models.fields.TextField', [], {}),
            'q2': ('django.db.models.fields.TextField', [], {}),
            'q3': ('django.db.models.fields.TextField', [], {}),
            'q4': ('django.db.models.fields.TextField', [], {}),
            'q5': ('django.db.models.fields.TextField', [], {}),
            'q6': ('django.db.models.fields.TextField', [], {})
        },
        u'website.ithacalife': {
            'Meta': {'object_name': 'IthacaLife'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'website.koreanschool': {
            'Meta': {'object_name': 'KoreanSchool'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'website.notice': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Notice'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'website.sermon': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Sermon'},
            'bible_verses': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'embed': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'preacher': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'website.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['website']