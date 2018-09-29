from django.urls import path

from .views import apis

app_name = 'movies'
urlpatterns = [
    path('list/', apis.MovieListCreateView.as_view(), name='movies_list'),
]
