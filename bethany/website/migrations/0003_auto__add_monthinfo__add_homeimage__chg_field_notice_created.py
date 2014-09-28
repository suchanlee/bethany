# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MonthInfo'
        db.create_table(u'website_monthinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('month_text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('month_verse', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('month_verse_text', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['MonthInfo'])

        # Adding model 'HomeImage'
        db.create_table(u'website_homeimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('image_source', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'website', ['HomeImage'])


        # Changing field 'Notice.created'
        db.alter_column(u'website_notice', 'created', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):
        # Deleting model 'MonthInfo'
        db.delete_table(u'website_monthinfo')

        # Deleting model 'HomeImage'
        db.delete_table(u'website_homeimage')


        # Changing field 'Notice.created'
        db.alter_column(u'website_notice', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None))

    models = {
        u'website.homeimage': {
            'Meta': {'object_name': 'HomeImage'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_source': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
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
        u'website.monthinfo': {
            'Meta': {'object_name': 'MonthInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'month_text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'month_verse': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'month_verse_text': ('django.db.models.fields.TextField', [], {})
        },
        u'website.notice': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Notice'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notice_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
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