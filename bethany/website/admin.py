from django.contrib import admin
from django.forms import ModelForm
from django import forms

from suit_redactor.widgets import RedactorWidget

from website.models import Sermon, Notice, IthacaLife, KoreanSchool, Interview, Slideshow


class SlideshowAdmin(admin.ModelAdmin):
	list_display = ('created', 'image')
	fields = ('image',)

admin.site.register(Slideshow, SlideshowAdmin)


class SermonAdmin(admin.ModelAdmin):
	fields = ('link', 'title', 'bible_verses', 'preacher', 'date')
	list_display = ('title',)
	date_hierarchy = 'created'

admin.site.register(Sermon, SermonAdmin)


class NoticeForm(ModelForm):

	NOTICE_TYPES = (
		('notice', 'Regular Notice'),
		('program', 'Worship Program'),
	)

	notice_type = forms.ChoiceField(required=True, choices=NOTICE_TYPES)

	class Meta:
		widgets = {
			'content': RedactorWidget(editor_options={'lang':'en'})
		}

class NoticeAdmin(admin.ModelAdmin):
	form = NoticeForm
	list_display = ('title', 'created')
	date_hierarchy = 'created'

admin.site.register(Notice, NoticeAdmin)


class InterviewAdmin(admin.ModelAdmin):
	list_display = ('major', 'college', 'grad_year')

admin.site.register(Interview, InterviewAdmin)


class IthacaLifeForm(ModelForm):
	class Meta:
		widgets = {
			'content': RedactorWidget(editor_options={'lang':'en'})
		}

class IthacaLifeAdmin(admin.ModelAdmin):
	form = IthacaLifeForm

admin.site.register(IthacaLife, IthacaLifeAdmin)


class KoreanSchoolForm(ModelForm):
	class Meta:
		widgets = {
			'content': RedactorWidget(editor_options={'lang':'en'})
		}

class KoreanSchoolAdmin(admin.ModelAdmin):
	form = KoreanSchoolForm

admin.site.register(KoreanSchool, KoreanSchoolAdmin)