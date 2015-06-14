from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.movie_list),
	url(r'^movie/search$', views.movie_search),
	url(r'^movie/(?P<pk>[0-9]+)/$', views.movie_detail),
	url(r'^movie/new/$', views.movie_new, name='movie_new'),
	url(r'^movie/(?P<pk>[0-9]+)/edit/$',	views.movie_edit,	name='movie_edit'),
	url(r'^movie/(?P<pk>[0-9]+)/remove/$',	views.movie_remove,	name='movie_remove'),

	]