from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from website import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^visit/$', views.VisitView.as_view(), name='visit'),
    url(r'^community/$', views.CommunityView.as_view(), name='community'),
    url(r'^korean/$', views.KoreanSchoolView.as_view(), name='korean_school'),
    url(r'^board/$', views.BoardView.as_view(), name='board'),
    url(r'^board/(?P<pk>\d+)/$', views.BoardDetailView.as_view(), name='board_detail'),
    url(r'^board/post/(?P<board_pk>\d+)/(?P<post_pk>\d+)/$', views.PostView.as_view(), name='post_detail'),
    url(r'^board/post/(?P<board_pk>\d+)/create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^board/post/update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^board/post/delete/(?P<pk>\d+)/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^board/notice/$', views.NoticeDetailView.as_view(), name='notice_detail'),
    url(r'^board/post/notice/(?P<pk>\d+)/$', views.NoticePostView.as_view(), name='notice_post'),
    url(r'^sermons/$', views.SermonView.as_view(), name='sermons'),
    url(r'^sermons/(?P<pk>\d+)/$', views.SermonDetailView.as_view(), name='sermons'),
    url(r'^register/$', views.user_register_view, name='create_user'),
    url(r'^login/$', views.user_login, name='login_user'),

    (r'', include('django.contrib.auth.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

