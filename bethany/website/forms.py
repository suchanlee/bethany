import re

from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User

from suit_redactor.widgets import RedactorWidget

from simple_board.models import Post


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		widgets = {
			'content': RedactorWidget(editor_options={'lang':'kr'})
		}


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password',]
		widgets = {
			'password': PasswordInput
		}


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(min_length=6, widget=forms.PasswordInput())


class UserRegistrationForm(forms.Form):
	username = forms.CharField(max_length=25)
	password1 = forms.CharField(min_length=6, help_text='Minimum 6 characters', widget=forms.PasswordInput())
	password2 = forms.CharField(min_length=6, help_text='Minimum 6 characters', widget=forms.PasswordInput())
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)

	def clean(self):
		cleaned_data = super(UserRegistrationForm, self).clean()
		pw1 = cleaned_data.get('password1')
		pw2 = cleaned_data.get('password2')
		username = cleaned_data.get('username')

		if not (pw1 and pw2):
			raise forms.ValidationError("You must enter a valid password at least 6 characters long with at least one uppercase letter.")

		if pw1 and pw2:
			if pw1 != pw2:
				raise forms.ValidationError("The passwords do not match")

		if (User.objects.filter(email=cleaned_data.get('email').lower()).count() > 0):
			raise forms.ValidationError("This email has already been used")

		if (User.objects.filter(username=cleaned_data.get('username').lower()).count() > 0):
			raise forms.ValidationError("This username has been taken")

		#Username only alphanumeric characters and underscores
		check_username = re.sub('[\W]','',username)
		if  (username != check_username):
			raise forms.ValidationError("Username can only contain alphanumeric characters and underscore ('_').")

		if (re.sub('_','',username) == ''):
			raise forms.ValidationError("Username cannot contain just underscores.")

		if (re.sub('[0-9_]','',username) == ''):
			raise forms.ValidationError("Username must contain at least one letter")

		return cleaned_data