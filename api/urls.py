from django.conf.urls import patterns, url
from api.views import MovieSearch
urlpatterns = patterns(
    'api.views',
    url(r'^movie/$', 'movie_list', name='movie_list'),
     url(r'^movie/add/$', 'movie_add', name='movie_add'),
    url(r'^movie/(?P<pk>[0-9]+)$', 'movie_detail', name='movie_detail'),
    url(r'^movie/search/$',MovieSearch.as_view(),name='movie_search'),
)