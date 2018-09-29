from rest_framework import generics, exceptions
from rest_framework.response import Response

from utils.pagination import CustomPagination
from ..serializers import MovieSerializer
from ..models import Movie


class MovieListCreateView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Movie.objects.all()
        quality = self.request.query_params.get('quality', '')
        try:
            minimum_rating = int(self.request.query_params.get('minimum_rating', 0))
            if minimum_rating > 9:
                error = {
                    'status': 'error',
                    'status_message': 'minimum_rating 은 0 이상 9 이하의 정수만 가능합니다.',
                }
                raise exceptions.ValidationError(error)
        except ValueError:
            error = {
                'status': 'error',
                'status_message': 'minimum_rating 은 0 이상 9 이하의 정수만 가능합니다.',
            }
            raise exceptions.ValidationError(error)
        query_term = self.request.query_params.get('query_term', '')
        genre = self.request.query_params.get('genre', '')

        if quality and not genre:
            queryset = queryset.filter(
                torrents__quality__contains=quality,
                rating__gte=minimum_rating,
                title__contains=query_term,
            )
        elif genre and not quality:
            queryset = queryset.filter(
                rating__gte=minimum_rating,
                title__contains=query_term,
                genres__name__contains=genre,
            )
        elif not genre and not quality:
            queryset = queryset.filter(
                rating__gte=minimum_rating,
                title__contains=query_term,
            )
        else:
            queryset = queryset.filter(
                torrents__quality__contains=quality,
                rating__gte=minimum_rating,
                title__contains=query_term,
                genres__name__contains=genre,
            )
        order_by = self.request.query_params.get('order_by', 'desc')
        sort_by = self.request.query_params.get('sort_by', '')

        if sort_by:
            if sort_by == 'peers':
                sort_by = 'torrents__peers'
            elif sort_by == 'seeds':
                sort_by = 'torrents__seeds'
            elif sort_by == 'date_added':
                sort_by = 'date_uploaded'

            if order_by == 'desc':
                queryset = queryset.order_by(sort_by)
            else:
                queryset = queryset.order_by('-' + sort_by)

        return queryset

    def get_paginated_response(self, data):
        if not self.get_queryset():
            return Response({
                'status': 'ok',
                'status_message': 'Query was successful',
                'data': {
                    'movie_count': self.get_queryset().count(),
                    'limit': int(self.request.query_params.get('limit', 20)),
                    'page_number': int(self.request.query_params.get('page', 1)),
                }
            })
        else:
            return Response({
                'status': 'ok',
                'status_message': 'Query was successful',
                'data': {
                    'movie_count': self.get_queryset().count(),
                    'limit': int(self.request.query_params.get('limit', 20)),
                    'page_number': int(self.request.query_params.get('page', 1)),
                    'movies': data,
                }
            })
