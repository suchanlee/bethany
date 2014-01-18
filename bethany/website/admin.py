from django.contrib import admin
from django.forms import ModelForm

from suit_redactor.widgets import RedactorWidget

from website.models import Sermon, Notice, IthacaLife, KoreanSchool


class SermonAdmin(admin.ModelAdmin):
	fields = ('link', 'title', 'bible_verses', 'preacher', 'date')
	list_display = ('title',)
	date_hierarchy = 'created'

admin.site.register(Sermon, SermonAdmin)


class NoticeForm(ModelForm):
	class Meta:
		widgets = {
			'content': RedactorWidget(editor_options={'lang':'en'})
		}

class NoticeAdmin(admin.ModelAdmin):
	form = NoticeForm
	list_display = ('title', 'created')
	date_hierarchy = 'created'

admin.site.register(Notice, NoticeAdmin)


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