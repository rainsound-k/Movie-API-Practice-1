from rest_framework import generics
from rest_framework.response import Response

from utils.pagination import CustomPagination
from ..serializers import MovieSerializer
from ..models import Movie


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination

    def get_paginated_response(self, data):
        return Response({
            'status': 'ok',
            'status_message': 'Query was successful',
            'data': {
                'movie_count': self.queryset.count(),
                'limit': self.request.query_params.get('limit', '20'),
                'page_number': self.request.query_params.get('page', '1'),
                'movies': data,
            }
        })
