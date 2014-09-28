from django.contrib import admin
from django.forms import ModelForm

from suit_redactor.widgets import RedactorWidget

from simple_board.models import Board, Post

class BoardAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Board, BoardAdmin)


class PostForm(ModelForm):
	class Meta:
		widgets = {
			'content': RedactorWidget(editor_options={'lang':'kr'})
		}

class PostAdmin(admin.ModelAdmin):
	list_display = ('board', 'title', 'author', 'created',)
	form = PostForm

admin.site.register(Post, PostAdmin)