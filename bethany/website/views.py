from django.views.generic import TemplateView, ListView, CreateView, FormView, UpdateView, DeleteView
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from website.models import Sermon, IthacaLife, KoreanSchool, Notice, Interview, Slideshow
from simple_board.models import Board, Post
from website.forms import PostForm, UserLoginForm, UserRegistrationForm

import pdb


class HomeView(TemplateView):
	template_name = 'website/home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context = {}
		context['sermon'] = Sermon.objects.order_by('-created')[1]
		context['posts'] = Post.objects.order_by('-created')[:5]
		context['notices'] = Notice.objects.order_by('-created')[:5]
		context['slides'] = Slideshow.objects.order_by('-created')[:3]
		context['auth_form'] = UserLoginForm
		return context


class CommunityView(TemplateView):
	template_name = 'website/community.html'

	def get_context_data(self, **kwargs):
		context = super(CommunityView, self).get_context_data(**kwargs)
		context = {}
		context['object'] = IthacaLife.objects.get(id=1)
		context['page'] = 'community'
		context['auth_form'] = UserLoginForm
		return context


class StudentTipView(TemplateView):
	template_name = 'website/student.html'

	def get_context_data(self, **kwargs):
		context = {}
		context['page'] = 'community'
		context['subpage'] = 'student'
		context['auth_form'] = UserLoginForm
		context['interviews'] = Interview.objects.all().order_by('major')
		return context


class KoreanSchoolView(TemplateView):
	template_name = 'website/korean_school.html'

	def get_context_data(self, **kwargs):
		context = super(KoreanSchoolView, self).get_context_data(**kwargs)
		context = {}
		context['object'] = KoreanSchool.objects.get(id=1)
		context['auth_form'] = UserLoginForm
		context['page'] = 'korean'
		return context


class ContactView(TemplateView):
	template_name = 'website/contact.html'

	def get_context_data(self, **kwargs):
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'contact'
		return context


class BoardView(TemplateView):
	template_name = 'website/board.html'

	def get_context_data(self, **kwargs):
		context = super(BoardView, self).get_context_data(**kwargs)
		context = {}
		context['page'] = 'board'
		boards = Board.objects.all()
		posts = []
		for board in boards:
			posts.append(Post.objects.filter(board=board)[:5])
		context['notices'] = Notice.objects.all()[:5]
		context['board1'] = boards[0]
		context['board2'] = boards[1]
		context['posts1'] = posts[0]
		context['posts2'] = posts[1]
		context['auth_form'] = UserLoginForm
		return context


class BoardDetailView(TemplateView):
	template_name = 'website/board_detail.html'

	def get_context_data(self, **kwargs):
		context = super(BoardDetailView, self).get_context_data(**kwargs)
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'board'
		board = Board.objects.get(pk=kwargs['pk'])
		post_list = Post.objects.filter(board=board)
		context['board'] = board
		paginator = Paginator(post_list, 20)
		page = self.request.GET.get('pages')
		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page
			posts = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			posts = paginator.page(paginator.num_pages)

		context['posts'] = posts
		context['current_page'] = posts.number
		context['total_pages'] = [i for i in range(1, paginator.num_pages+1)]
		return context


class NoticeDetailView(TemplateView):
	template_name = 'website/board_detail.html'

	def get_context_data(self, **kwargs):
		context = super(NoticeDetailView, self).get_context_data(**kwargs)
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'board'
		notice_list = Notice.objects.all()
		paginator = Paginator(notice_list, 20)
		page = self.request.GET.get('pages')
		try:
			notices = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page
			notices = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			notices = paginator.page(paginator.num_pages)

		context['posts'] = notices
		context['current_page'] = notices.number
		context['total_pages'] = [i for i in range(1, paginator.num_pages+1)]
		context['notice'] = 1
		return context

class NoticePostView(TemplateView):
	template_name = 'website/post.html'

	def get_context_data(self, **kwargs):
		context = super(NoticePostView, self).get_context_data(**kwargs)
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'board'

		post = Notice.objects.get(pk=kwargs['pk'])
		post.views += 1
		post.save()

		if post.attachment:
			attach_name = post.attachment.path.split('/')
			print attach_name
			context['attachment_name'] = attach_name[len(attach_name)-1]

		context['post'] = post
		return context


class PostView(TemplateView):
	template_name = 'website/post.html'

	def get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'board'

		post = Post.objects.get(pk=kwargs['post_pk'])
		post.views += 1
		post.save()

		context['post'] = post
		return context


class PostCreateView(LoginRequiredMixin, CreateView):
	template_name = 'website/post_form.html'
	form_class = PostForm
	success_url = '/board/'

	def get_initial(self):
		initial = super(PostCreateView, self).get_initial()
		initial = initial.copy()
		initial['views'] = 0
		initial['author'] = self.request.user
		board = Board.objects.get(pk=self.kwargs['board_pk'])
		initial['board'] = board
		return initial

	def get_context_data(self, **kwargs):
		context = super(PostCreateView, self).get_context_data(**kwargs)
		context['auth_form'] = UserLoginForm
		return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'website/post_form.html'
	form_class = PostForm
	model = Post
	success_url = '/board/'

	def get_context_data(self, **kwargs):
		context = super(PostUpdateView, self).get_context_data(**kwargs)
		post = context['object']
		if post.author != self.request.user:
			raise Http404
		context['auth_form'] = UserLoginForm
		return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'website/post_delete.html'
	model = Post
	success_url = '/board/'

	def get_context_data(self, **kwargs):
		context = super(PostDeleteView, self).get_context_data(**kwargs)
		post = context['object']
		if post.author != self.request.user:
			raise Http404
		context['auth_form'] = UserLoginForm
		return context


class AboutView(TemplateView):
	template_name = 'website/about.html'

	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'about'
		return context


class VisitView(TemplateView):
	template_name = 'website/visit.html'

	def get_context_data(self, **kwargs):
		context = super(VisitView, self).get_context_data(**kwargs)
		context = {}
		context['auth_form'] = UserLoginForm
		context['page'] = 'visit'
		return context


class SermonView(TemplateView):
	template_name = 'website/sermons.html'

	def get_context_data(self, **kwargs):
		context = super(SermonView, self).get_context_data(**kwargs)
		context['auth_form'] = UserLoginForm
		sermon_list = Sermon.objects.all()
		context['page'] = 'sermons'

		paginator = Paginator(sermon_list, 6)
		page = self.request.GET.get('pages')
		try:
			sermons = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page
			sermons = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			sermons = paginator.page(paginator.num_pages)

		context['sermons'] = sermons
		context['current_page'] = sermons.number
		context['total_pages'] = [i for i in range(1, paginator.num_pages+1)]

		return context


class SermonDetailView(TemplateView):
	template_name = 'website/sermon_detail.html'

	def get_context_data(self, **kwargs):
		context = super(SermonDetailView, self).get_context_data(**kwargs)
		context['sermon'] = Sermon.objects.get(pk=kwargs['pk'])
		context['page'] = 'sermons'
		context['auth_form'] = UserLoginForm
		return context


def user_login(request):

	template_name = 'registration/login_page.html'

	form = UserLoginForm()

	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			try:
				user = authenticate(username=cleaned_data['username'].lower(),
									password=cleaned_data['password'])
				login(request, user)
				return redirect('home')
			except:
				pass

	context = {
		'auth_form': form,
	}
	return render_to_response(template_name,
		context_instance = RequestContext(request, context))


def user_register_view(request):
	template_name = 'registration/register.html'

	form = UserRegistrationForm()

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			user = User.objects.create(username = cleaned_data['username'].lower(),
									   first_name = cleaned_data['first_name'].lower(),
									   last_name = cleaned_data['last_name'].lower(),
									   email = cleaned_data['email'].lower())
			user.set_password(cleaned_data['password1'])
			user.save()
			try:
				user = authenticate(username=cleaned_data['username'], password=cleaned_data['password1'])
				login(request, user)
			except:
				pass # raise proper exception
			template_name = 'registration/register_success.html'
			context = {
				'form': form,
				'auth_form': UserLoginForm(),
			}
			return TemplateResponse(request, template_name, context, current_app=None)


	context = {
		'form': form,
		'auth_form': UserLoginForm(),
	}
	return render_to_response(template_name,
		context_instance = RequestContext(request, context))

