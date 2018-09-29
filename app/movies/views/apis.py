from rest_framework import generics

from ..serializers import MovieSerializer
from ..models import Movie


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
